package com.example.demo;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.scheduling.annotation.Async;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.Executor;
import java.util.concurrent.ThreadLocalRandom;


// https://spring.io/guides/gs/async-method/

// The @EnableAsync annotation switches on Spring’s ability to run @Async methods in a background thread pool.
@EnableAsync
@SpringBootApplication
public class TaskExecutorApplication {

	public static void main(String[] args) {
		SpringApplication.run(TaskExecutorApplication.class, args);
	}

	@Component
	public class AppRunner implements CommandLineRunner {

		private final Logger logger = LoggerFactory.getLogger(AppRunner.class);
		@Autowired private GitHubLookupService gitHubLookupService;

		@Override
		public void run(String... args) throws Exception {
			// Start the clock
			long start = System.currentTimeMillis();

			// Kick of multiple, asynchronous lookups
			CompletableFuture<User> page1 = gitHubLookupService.sendMessagetoSubscriber("PivotalSoftware");
			CompletableFuture<User> page2 = gitHubLookupService.sendMessagetoSubscriber("CloudFoundry");
			CompletableFuture<User> page3 = gitHubLookupService.sendMessagetoSubscriber("Spring-Projects");

			// Wait until they are all done
			// With the help of the allOf factory method, we create an array of CompletableFuture objects.
			// By calling the join method, it is possible to wait for the completion of all of the CompletableFuture objects.
			CompletableFuture.allOf(page1,page2,page3).join();

			// Print results, including elapsed time
			logger.info("Elapsed time: " + (System.currentTimeMillis() - start));
			logger.info("--> " + page1.get());
			logger.info("--> " + page2.get());
			logger.info("--> " + page3.get());

		}

	}


	@Bean
	public Executor taskExecutor() {
		ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
		executor.setCorePoolSize(2);
		executor.setMaxPoolSize(2); // Limit concurrent threads to 2
		executor.setQueueCapacity(500);	// Queue size: 500
		executor.setThreadNamePrefix("GithubLookup-");
		executor.initialize();
		return executor;
	}

	// The sendMessagetoSubscriber method is flagged with Spring’s @Async annotation, indicating that it should run on a separate thread.
	//  The method’s return type is CompletableFuture<User> instead of User, a requirement for any asynchronous service.
	@Service
	public class GitHubLookupService {

		private final Logger logger = LoggerFactory.getLogger(GitHubLookupService.class);
		private final RestTemplate restTemplate;

		public GitHubLookupService(RestTemplateBuilder restTemplateBuilder) {
			this.restTemplate = restTemplateBuilder.build();
		}

		@Async
		public CompletableFuture<User> sendMessagetoSubscriber(String user) throws InterruptedException {
			logger.info("Looking up " + user);
			String url = String.format("https://api.github.com/users/%s", user);
			User results = restTemplate.getForObject(url, User.class);
			Thread.sleep(ThreadLocalRandom.current().nextInt(5000, 10000));
			return CompletableFuture.completedFuture(results);
		}

	}

}
