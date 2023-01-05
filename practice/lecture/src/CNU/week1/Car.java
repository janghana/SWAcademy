package CNU.week1;

/*
자동차 객체를 만들 수 있게 설명해둔, 완성되었을 때기능을 말해주는 설계도
 */
//TODO Car class
public class Car {
    public static void main(String[] args) {
        Car car = new Car();
        car.ride();

        int wheel = 4;
    }

    void ride() { // 자동차가 객체가 되면, 이 기능을 가진다.
        System.out.println("씽씽씽");
    }

}