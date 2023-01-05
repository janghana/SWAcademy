package com.programmers.java.func;

public class Main2 {
    public static void main(String[] args) {
        MyRunnable r1 = new MyRunnable() {
            @Override
            public void run() {
                System.out.println("Hello");
            }
        };

        // 익명 메소드를 사용해서 표현하는 방법 : 람다 표현식
        MyRunnable r2 = () -> System.out.println("Hello");

        MySupply s1 = () -> "Hello World ";



        MyRunnable r3 = () -> {
            MySupply s2 = () -> "Hello Hello Hello";
            System.out.println(s2.supply());
        };
        r3.run();
    }
}
