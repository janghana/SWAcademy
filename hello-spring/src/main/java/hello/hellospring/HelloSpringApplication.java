package hello.hellospring;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

// 하단 main 문을 통해 SpringBootApplication이 실행 되면서 띄우며 tomcat이라는 웹서버 내장하는데,
// tomcat이라는 웹서버 자체적으로 띄우며 SpringBoot 같이 올라옴.
@SpringBootApplication
public class HelloSpringApplication {

	public static void main(String[] args) {
		SpringApplication.run(HelloSpringApplication.class, args);
	}

}
