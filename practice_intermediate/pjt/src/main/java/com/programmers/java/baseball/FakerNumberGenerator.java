package com.programmers.java.baseball;

import com.github.javafaker.Faker;
import com.programmers.java.baseball.engine.NumberGenerator;
import com.programmers.java.baseball.engine.model.Numbers;

import java.util.stream.Stream;

public class FakerNumberGenerator implements NumberGenerator {

    @Override
    public Numbers generate(int count) {
        final Faker faker = new Faker();
        return new Numbers(
            Stream.generate(() -> faker.number().randomDigitNotZero())
                    .limit(count)
                    .distinct()
                    .toArray(Integer[]::new)
        );
    }
}
