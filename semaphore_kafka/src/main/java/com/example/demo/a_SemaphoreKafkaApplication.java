package com.example.demo;

import lombok.AllArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.Date;
import java.util.concurrent.Semaphore;
import java.util.concurrent.ThreadLocalRandom;

//@SpringBootApplication
public class a_SemaphoreKafkaApplication {

    public static void main(String[] args) {
        SpringApplication.run(a_SemaphoreKafkaApplication.class, args);
    }

    @RestController
    @RequestMapping(value = "/kafka")
    public class KafkaController {

        private final Producer producer;

        @Autowired
        KafkaController(Producer producer) {
            this.producer = producer;
        }

        @PostMapping(value = "/publish")
        public void sendMessageToKafkaTopic(@RequestParam("message") String message) {

            for (int i = 0; i < 10; i++) {
                this.producer.sendMessage(i + " > " + message + (new Date()).toString());
            }
        }
    }

    @AllArgsConstructor
    public class User {
        String name;
        String age;
    }

    @Service
    public class Producer {

        private final Logger logger = LoggerFactory.getLogger(Producer.class);
        private static final String TOPIC = "users";

        @Autowired
        private KafkaTemplate<String, String> kafkaTemplate;

        public void sendMessage(String message) {
            logger.info(String.format("#### -> Producing message -> %s", message));
            this.kafkaTemplate.send(TOPIC, message);
        }
    }

    @Service
    public class ConsumerSemaphore {

        private String name;
        private final Logger logger = LoggerFactory.getLogger(ConsumerSemaphore.class);

        @KafkaListener(topics = "users", groupId = "group_id")
        public void consume(String message) throws IOException, InterruptedException {
            new CellPhone(message).start();
        }
    }

    private static Semaphore charger = new Semaphore(3);

    public class CellPhone extends Thread {

        private String message;
        private final Logger logger = LoggerFactory.getLogger(ConsumerSemaphore.class);

        public CellPhone(String message) {
            this.message = message;
        }

        public void run() {

            try {
                charger.acquire();
                logger.info(String.format("#### -> Started Consumed message -> %s", message));
                Thread.sleep(ThreadLocalRandom.current().nextInt(5000, 10000));
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                logger.info(String.format("#### -> Completed Consumed message -> %s", message));
                charger.release();
            }

        }

    }


	/*@Service
	public class Consumer {

		private final Logger logger = LoggerFactory.getLogger(Consumer.class);

		@KafkaListener(topics = "users", groupId = "group_id")
		public void consume(String message) throws IOException, InterruptedException {

			Thread.sleep(ThreadLocalRandom.current().nextInt(1000, 10000));
			logger.info(String.format("#### -> Consumed message -> %s", message));
		}
	}*/

}
