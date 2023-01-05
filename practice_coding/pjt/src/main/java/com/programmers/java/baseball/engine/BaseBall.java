package com.programmers.java.baseball.engine;

import com.programmers.java.baseball.engine.io.Input;
import com.programmers.java.baseball.engine.io.Output;
import com.programmers.java.baseball.engine.model.BallCount;
import com.programmers.java.baseball.engine.model.Numbers;
import lombok.AllArgsConstructor;

import java.util.Optional;
import java.util.concurrent.atomic.AtomicInteger;

@AllArgsConstructor
public class BaseBall implements Runnable {
    private final int COUNT_OF_NUMBERS = 4;

    private NumberGenerator generator;
    private Input input;
    private Output output;


    @Override
    public void run() {
        Numbers answer = generator.generate(COUNT_OF_NUMBERS);

        while (true) {
            String inputString = input.input("숫자를 맞춰보세요. :");
            Optional<Numbers> inputNumbers = parse(inputString);

            if(inputNumbers.isEmpty()) {
                output.inputError();
                continue;
            }

            BallCount bc = ballCount(answer, inputNumbers.get());
            output.ballCount(bc);
            if (bc.getStrike() == COUNT_OF_NUMBERS) {
                output.correct();
                break;
            }

        }
    }

    private BallCount ballCount(Numbers answer, Numbers inputNumbers) {
        AtomicInteger strike = new AtomicInteger(); // 아래를 사용하려면 동기화 기능을 추가함.
        AtomicInteger ball = new AtomicInteger();

        answer.indexedForEach((a,i) -> {
            inputNumbers.indexedForEach((n,j) -> {
                if(a != n) return;
                if(i.equals(j)) strike.addAndGet(1); // getAndAdd와 같은 것도 있음.
                else ball.addAndGet(1);
                // scope 밖의 strike, ball 동작은 하지만 이렇게 하면 안 됨. read는 가능, write는 불가.
                // 만약, multi thread라면 race condition이 일어날 수도 있음.
            });
        });
        return new BallCount(strike.get(), ball.get());
    }

    private Optional<Numbers> parse(String inputString) {
        if(inputString.length() != COUNT_OF_NUMBERS) return Optional.empty();
        long count = inputString.chars() // string
                .filter(Character::isDigit) // 숫자인 것
                .map(Character::getNumericValue) // 숫자 값으로 바꿈
                .filter(i -> i > 0)
                .distinct() // 중복 제거
                .count();
        // 여러 처리 후에 COUNT_OF_NUMBERS와 다르다는 것은 걸러진 것.
        if (count != COUNT_OF_NUMBERS) return Optional.empty();

        return Optional.of(
                new Numbers(
                        inputString.chars()
                                .map(Character::getNumericValue)
                                .boxed() // Stream<Integer>
                                .toArray(Integer[]::new) //
                )
        );// Optional로 감싸서 전달
    }

}
