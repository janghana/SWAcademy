package com.programmers.java.lambda;

public class Main {
    public static void main(String[] args) {

        MySupplier<String> s = () -> "Hello World";
        MyMapper<String, Integer> m = String::length;
        MyMapper<Integer, Integer> m2 = i -> i * i;
        MyMapper<Integer, String> m3 = Integer::toHexString;
        MyConsumer<String> c = System.out::println;


        MyRunnable r = () ->
                c.consume(
                        m3.map(
                                m2.map(
                                        m.map(
                                                s.supply()
                                        )
                                )
                        )
                );

        r.run();
    }
}
