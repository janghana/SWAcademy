package com.programmers.java.def;

interface MyInterface {
    void method1(); // 구현이 X : 추상 메소드

    default void sayHello() { // 구현이 O
        System.out.println("Hello World");
    }
}

public class Main implements MyInterface {
    public static void main(String[] args)
        new Main().sayHello();
    }

    @Override
    public void method1() {
        throw new RuntimeException();
    }
}
