package com.programmers.java.poly;

public class UserService implements Login {

    private Login login;

    // 의존성을 외부에 맡긴다면, 의존도을 낮춘다.
    // 결합성 강하게 결합되죠. => 추상체와 결합을 하게 되면 => 결합도가 낮아졌다.
    // 의존성을 외부로 부터 전달받았다. => 의존성을 주입받았다.
    // 의존성 주입, Dependency Injection, DI
    // Dependency Inversion 되었습니다.
    public UserService(Login login) {
        this.login = login;
    }

    @Override
    public void login() {
        login.login();
    }
}
