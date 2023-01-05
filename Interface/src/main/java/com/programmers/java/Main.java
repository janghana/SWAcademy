package com.programmers.java;

interface MyRunnable {
    void myRun();
}

interface YourRunnable {
    void yourRun();
}

public class Main implements MyRunnable, YourRunnable {
    public static void main(String[] args) {
        YourRunnable m = new Main();
//        m.myRun();
        m.yourRun();
    }

    @Override
    public void myRun() {
        System.out.println("Hello myRun");
    }

    @Override
    public void yourRun() {
        System.out.println("Hello yourRun");
    }
}
