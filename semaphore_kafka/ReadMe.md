# Problems
1. How to concurrently read messages from Kafka using Counting Semaphore.?
2. How to increase PERMITS, when load is high. ?
3. What happens if one of the threads throws exceptions.?

## 1 Read messages from Kafka using Counting Semaphore

1. Read 3 messages by 3 threads,
2. Once permit is available, another thread starts reading the message.

### Solution

Project: a_SemaphoreKafkaApplication

#### Steps

1. 3 Threads starts take the permit
2. When permit is released by one of the thread, another idle thread acquires the permit and start consuming message.
3. At a time, only 3 threads can concurrently consume message.

#### Output

````2020-05-25 17:44:17 - #### -> Producing message -> 1 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:17 - #### -> Producing message -> 2 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:17 - #### -> Producing message -> 3 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:17 - #### -> Producing message -> 4 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:17 - #### -> Producing message -> 5 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:17 - #### -> Producing message -> 6 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:17 - #### -> Producing message -> 7 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:17 - #### -> Producing message -> 8 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:17 - #### -> Producing message -> 9 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:17 - #### -> Started Consumed message -> 0 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:17 - #### -> Started Consumed message -> 1 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:17 - #### -> Started Consumed message -> 2 > testMon May 25 17:44:17 PDT 2020
 
 2020-05-25 17:44:22 - #### -> Completed Consumed message -> 0 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:22 - #### -> Started Consumed message -> 3 > testMon May 25 17:44:17 PDT 2020
 
 2020-05-25 17:44:25 - #### -> Completed Consumed message -> 1 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:25 - #### -> Started Consumed message -> 4 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:25 - #### -> Completed Consumed message -> 2 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:25 - #### -> Started Consumed message -> 5 > testMon May 25 17:44:17 PDT 2020
 
 2020-05-25 17:44:30 - #### -> Completed Consumed message -> 4 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:30 - #### -> Started Consumed message -> 6 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:31 - #### -> Completed Consumed message -> 3 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:31 - #### -> Started Consumed message -> 7 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:35 - #### -> Completed Consumed message -> 5 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:35 - #### -> Started Consumed message -> 8 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:36 - #### -> Completed Consumed message -> 7 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:36 - #### -> Started Consumed message -> 9 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:38 - #### -> Completed Consumed message -> 6 > testMon May 25 17:44:17 PDT 2020
 2020-05-25 17:44:41 - #### -> Completed Consumed message -> 8 > testMon May 25 17:44:17 PDT 2020`
````

## 2. Increase PERMITS

`if(charger.availablePermits()  == 0)
         charger.release(10);`
         
### Solution

Project: b_SemaphoreKafka_WhenLoadIncreases

#### Steps

1. 3 Threads starts take the permit
2. When permit is released any thread, request is made to increase the permit by 10.
3. With this, we can use more idle threads during peak load.

###Output

`2020-05-25 17:56:06 - [Producer clientId=producer-1] Cluster ID: 4Px6U1o3QMOhliYMBTkLfg
2020-05-25 17:56:06 - #### -> Producing message -> 1 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 2 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 3 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 4 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 5 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 6 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 7 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 8 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 9 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 10 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 11 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 12 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 13 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 14 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 15 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 16 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 17 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 18 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 19 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 20 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 21 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 22 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 23 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 24 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 25 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 26 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 27 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 28 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 29 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 30 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 31 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 32 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 33 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 34 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 35 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 36 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 37 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 38 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Producing message -> 39 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Started Consumed message -> 0 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Started Consumed message -> 1 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:06 - #### -> Started Consumed message -> 2 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:12 - #### -> Completed Consumed message -> 0 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:12 - #### -> Started Consumed message -> 3 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:12 - #### -> Started Consumed message -> 4 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:12 - #### -> Started Consumed message -> 5 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:12 - #### -> Started Consumed message -> 6 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:12 - #### -> Started Consumed message -> 7 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:12 - #### -> Started Consumed message -> 8 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:12 - #### -> Started Consumed message -> 9 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:12 - #### -> Started Consumed message -> 10 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:12 - #### -> Started Consumed message -> 11 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:12 - #### -> Started Consumed message -> 12 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:14 - #### -> Completed Consumed message -> 2 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:14 - #### -> Started Consumed message -> 13 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:14 - #### -> Started Consumed message -> 15 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:14 - #### -> Started Consumed message -> 16 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:14 - #### -> Started Consumed message -> 14 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:14 - #### -> Started Consumed message -> 17 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:14 - #### -> Started Consumed message -> 18 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:14 - #### -> Started Consumed message -> 19 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:14 - #### -> Started Consumed message -> 20 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:14 - #### -> Started Consumed message -> 21 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:14 - #### -> Started Consumed message -> 22 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:16 - #### -> Completed Consumed message -> 1 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:16 - #### -> Started Consumed message -> 23 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:16 - #### -> Started Consumed message -> 24 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:16 - #### -> Started Consumed message -> 25 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:16 - #### -> Started Consumed message -> 26 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:16 - #### -> Started Consumed message -> 27 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:16 - #### -> Started Consumed message -> 28 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:16 - #### -> Started Consumed message -> 29 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:16 - #### -> Started Consumed message -> 30 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:16 - #### -> Started Consumed message -> 31 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:16 - #### -> Started Consumed message -> 32 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:17 - #### -> Completed Consumed message -> 5 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:17 - #### -> Started Consumed message -> 33 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:17 - #### -> Started Consumed message -> 35 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:17 - #### -> Started Consumed message -> 34 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:17 - #### -> Started Consumed message -> 36 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:17 - #### -> Started Consumed message -> 37 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:17 - #### -> Started Consumed message -> 38 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:17 - #### -> Started Consumed message -> 39 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:18 - #### -> Completed Consumed message -> 12 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:18 - #### -> Completed Consumed message -> 9 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:18 - #### -> Completed Consumed message -> 7 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:19 - #### -> Completed Consumed message -> 3 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:19 - #### -> Completed Consumed message -> 6 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:19 - #### -> Completed Consumed message -> 11 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:19 - #### -> Completed Consumed message -> 8 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:20 - #### -> Completed Consumed message -> 17 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:20 - #### -> Completed Consumed message -> 20 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:20 - #### -> Completed Consumed message -> 13 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:21 - #### -> Completed Consumed message -> 21 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:21 - #### -> Completed Consumed message -> 29 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:21 - #### -> Completed Consumed message -> 26 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:21 - #### -> Completed Consumed message -> 10 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:21 - #### -> Completed Consumed message -> 4 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:21 - #### -> Completed Consumed message -> 31 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:22 - #### -> Completed Consumed message -> 27 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:22 - #### -> Completed Consumed message -> 16 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:22 - #### -> Completed Consumed message -> 14 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:22 - #### -> Completed Consumed message -> 36 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:22 - #### -> Completed Consumed message -> 32 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:22 - #### -> Completed Consumed message -> 15 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:23 - #### -> Completed Consumed message -> 18 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:23 - #### -> Completed Consumed message -> 23 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:23 - #### -> Completed Consumed message -> 19 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:23 - #### -> Completed Consumed message -> 22 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:24 - #### -> Completed Consumed message -> 24 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:24 - #### -> Completed Consumed message -> 35 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:24 - #### -> Completed Consumed message -> 39 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:24 - #### -> Completed Consumed message -> 33 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:25 - #### -> Completed Consumed message -> 37 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:25 - #### -> Completed Consumed message -> 34 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:26 - #### -> Completed Consumed message -> 25 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:26 - #### -> Completed Consumed message -> 28 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:26 - #### -> Completed Consumed message -> 30 > testMon May 25 17:56:06 PDT 2020
2020-05-25 17:56:26 - #### -> Completed Consumed message -> 38 > testMon May 25 17:56:06 PDT 2020`

## 3. What happens if one of the threads throws exceptions.?

Steps
1. Kafka will retry consuming the message.
2. After X attempts, it will stop reset the offset and move to next item.

### Output

`2020-05-26 13:26:33 - [Producer clientId=producer-1] Cluster ID: 4Px6U1o3QMOhliYMBTkLfg
2020-05-26 13:26:33 - #### -> Producing message -> 1 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:33 - #### -> Producing message -> 2 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:33 - #### -> Producing message -> 3 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:33 - #### -> Producing message -> 4 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:33 - #### -> Producing message -> 5 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:33 - #### -> Producing message -> 6 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:33 - #### -> Producing message -> 7 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:33 - #### -> Producing message -> 8 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:33 - #### -> Producing message -> 9 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:33 - #### -> Started Consumed message -> 0 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:33 - #### -> Started Consumed message -> 1 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:33 - #### -> Started Consumed message -> 2 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:38 - #### -> Started Consumed message -> 3 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:41 - Exceptiion: 4 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:41 - [Consumer clientId=consumer-group_id-1, groupId=group_id] Seeking to offset 2215 for partition users-0
2020-05-26 13:26:41 - Error handler threw an exception
org.springframework.kafka.KafkaException: Seek to current after exception; nested exception is org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.SeekUtils.seekOrRecover(SeekUtils.java:157)
	at org.springframework.kafka.listener.SeekToCurrentErrorHandler.handle(SeekToCurrentErrorHandler.java:103)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeErrorHandler(KafkaMessageListenerContainer.java:1867)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1773)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeWithRecords(KafkaMessageListenerContainer.java:1701)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeRecordListener(KafkaMessageListenerContainer.java:1599)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeListener(KafkaMessageListenerContainer.java:1330)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.pollAndInvoke(KafkaMessageListenerContainer.java:1062)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.run(KafkaMessageListenerContainer.java:970)
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:515)
	at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.decorateException(KafkaMessageListenerContainer.java:1879)
	... 10 common frames omitted
Caused by: java.lang.IllegalArgumentException: null
	at com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(c_SemaphoreKafka_Exception.java:82)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:171)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.invoke(InvocableHandlerMethod.java:120)
	at org.springframework.kafka.listener.adapter.HandlerAdapter.invoke(HandlerAdapter.java:48)
	at org.springframework.kafka.listener.adapter.MessagingMessageListenerAdapter.invokeHandler(MessagingMessageListenerAdapter.java:334)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:86)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:51)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeOnMessage(KafkaMessageListenerContainer.java:1834)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeOnMessage(KafkaMessageListenerContainer.java:1817)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1760)
	... 8 common frames omitted
2020-05-26 13:26:50 - Exceptiion: 4 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:26:50 - [Consumer clientId=consumer-group_id-1, groupId=group_id] Seeking to offset 2215 for partition users-0
2020-05-26 13:26:50 - Error handler threw an exception
org.springframework.kafka.KafkaException: Seek to current after exception; nested exception is org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.SeekUtils.seekOrRecover(SeekUtils.java:157)
	at org.springframework.kafka.listener.SeekToCurrentErrorHandler.handle(SeekToCurrentErrorHandler.java:103)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeErrorHandler(KafkaMessageListenerContainer.java:1867)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1773)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeWithRecords(KafkaMessageListenerContainer.java:1701)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeRecordListener(KafkaMessageListenerContainer.java:1599)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeListener(KafkaMessageListenerContainer.java:1330)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.pollAndInvoke(KafkaMessageListenerContainer.java:1062)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.run(KafkaMessageListenerContainer.java:970)
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:515)
	at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.decorateException(KafkaMessageListenerContainer.java:1879)
	... 10 common frames omitted
Caused by: java.lang.IllegalArgumentException: null
	at com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(c_SemaphoreKafka_Exception.java:82)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:171)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.invoke(InvocableHandlerMethod.java:120)
	at org.springframework.kafka.listener.adapter.HandlerAdapter.invoke(HandlerAdapter.java:48)
	at org.springframework.kafka.listener.adapter.MessagingMessageListenerAdapter.invokeHandler(MessagingMessageListenerAdapter.java:334)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:86)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:51)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeOnMessage(KafkaMessageListenerContainer.java:1834)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeOnMessage(KafkaMessageListenerContainer.java:1817)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1760)
	... 8 common frames omitted
2020-05-26 13:27:00 - Exceptiion: 4 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:27:00 - [Consumer clientId=consumer-group_id-1, groupId=group_id] Seeking to offset 2215 for partition users-0
2020-05-26 13:27:00 - Error handler threw an exception
org.springframework.kafka.KafkaException: Seek to current after exception; nested exception is org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.SeekUtils.seekOrRecover(SeekUtils.java:157)
	at org.springframework.kafka.listener.SeekToCurrentErrorHandler.handle(SeekToCurrentErrorHandler.java:103)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeErrorHandler(KafkaMessageListenerContainer.java:1867)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1773)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeWithRecords(KafkaMessageListenerContainer.java:1701)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeRecordListener(KafkaMessageListenerContainer.java:1599)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeListener(KafkaMessageListenerContainer.java:1330)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.pollAndInvoke(KafkaMessageListenerContainer.java:1062)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.run(KafkaMessageListenerContainer.java:970)
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:515)
	at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.decorateException(KafkaMessageListenerContainer.java:1879)
	... 10 common frames omitted
Caused by: java.lang.IllegalArgumentException: null
	at com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(c_SemaphoreKafka_Exception.java:82)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:171)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.invoke(InvocableHandlerMethod.java:120)
	at org.springframework.kafka.listener.adapter.HandlerAdapter.invoke(HandlerAdapter.java:48)
	at org.springframework.kafka.listener.adapter.MessagingMessageListenerAdapter.invokeHandler(MessagingMessageListenerAdapter.java:334)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:86)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:51)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeOnMessage(KafkaMessageListenerContainer.java:1834)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeOnMessage(KafkaMessageListenerContainer.java:1817)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1760)
	... 8 common frames omitted
2020-05-26 13:27:08 - Exceptiion: 4 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:27:08 - [Consumer clientId=consumer-group_id-1, groupId=group_id] Seeking to offset 2215 for partition users-0
2020-05-26 13:27:08 - Error handler threw an exception
org.springframework.kafka.KafkaException: Seek to current after exception; nested exception is org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.SeekUtils.seekOrRecover(SeekUtils.java:157)
	at org.springframework.kafka.listener.SeekToCurrentErrorHandler.handle(SeekToCurrentErrorHandler.java:103)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeErrorHandler(KafkaMessageListenerContainer.java:1867)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1773)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeWithRecords(KafkaMessageListenerContainer.java:1701)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeRecordListener(KafkaMessageListenerContainer.java:1599)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeListener(KafkaMessageListenerContainer.java:1330)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.pollAndInvoke(KafkaMessageListenerContainer.java:1062)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.run(KafkaMessageListenerContainer.java:970)
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:515)
	at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.decorateException(KafkaMessageListenerContainer.java:1879)
	... 10 common frames omitted
Caused by: java.lang.IllegalArgumentException: null
	at com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(c_SemaphoreKafka_Exception.java:82)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:171)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.invoke(InvocableHandlerMethod.java:120)
	at org.springframework.kafka.listener.adapter.HandlerAdapter.invoke(HandlerAdapter.java:48)
	at org.springframework.kafka.listener.adapter.MessagingMessageListenerAdapter.invokeHandler(MessagingMessageListenerAdapter.java:334)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:86)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:51)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeOnMessage(KafkaMessageListenerContainer.java:1834)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeOnMessage(KafkaMessageListenerContainer.java:1817)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1760)
	... 8 common frames omitted
2020-05-26 13:27:14 - Exceptiion: 4 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:27:14 - [Consumer clientId=consumer-group_id-1, groupId=group_id] Seeking to offset 2215 for partition users-0
2020-05-26 13:27:14 - Error handler threw an exception
org.springframework.kafka.KafkaException: Seek to current after exception; nested exception is org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.SeekUtils.seekOrRecover(SeekUtils.java:157)
	at org.springframework.kafka.listener.SeekToCurrentErrorHandler.handle(SeekToCurrentErrorHandler.java:103)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeErrorHandler(KafkaMessageListenerContainer.java:1867)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1773)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeWithRecords(KafkaMessageListenerContainer.java:1701)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeRecordListener(KafkaMessageListenerContainer.java:1599)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeListener(KafkaMessageListenerContainer.java:1330)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.pollAndInvoke(KafkaMessageListenerContainer.java:1062)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.run(KafkaMessageListenerContainer.java:970)
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:515)
	at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.decorateException(KafkaMessageListenerContainer.java:1879)
	... 10 common frames omitted
Caused by: java.lang.IllegalArgumentException: null
	at com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(c_SemaphoreKafka_Exception.java:82)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:171)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.invoke(InvocableHandlerMethod.java:120)
	at org.springframework.kafka.listener.adapter.HandlerAdapter.invoke(HandlerAdapter.java:48)
	at org.springframework.kafka.listener.adapter.MessagingMessageListenerAdapter.invokeHandler(MessagingMessageListenerAdapter.java:334)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:86)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:51)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeOnMessage(KafkaMessageListenerContainer.java:1834)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeOnMessage(KafkaMessageListenerContainer.java:1817)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1760)
	... 8 common frames omitted
2020-05-26 13:27:20 - Exceptiion: 4 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:27:20 - [Consumer clientId=consumer-group_id-1, groupId=group_id] Seeking to offset 2215 for partition users-0
2020-05-26 13:27:20 - Error handler threw an exception
org.springframework.kafka.KafkaException: Seek to current after exception; nested exception is org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.SeekUtils.seekOrRecover(SeekUtils.java:157)
	at org.springframework.kafka.listener.SeekToCurrentErrorHandler.handle(SeekToCurrentErrorHandler.java:103)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeErrorHandler(KafkaMessageListenerContainer.java:1867)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1773)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeWithRecords(KafkaMessageListenerContainer.java:1701)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeRecordListener(KafkaMessageListenerContainer.java:1599)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeListener(KafkaMessageListenerContainer.java:1330)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.pollAndInvoke(KafkaMessageListenerContainer.java:1062)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.run(KafkaMessageListenerContainer.java:970)
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:515)
	at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.decorateException(KafkaMessageListenerContainer.java:1879)
	... 10 common frames omitted
Caused by: java.lang.IllegalArgumentException: null
	at com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(c_SemaphoreKafka_Exception.java:82)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:171)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.invoke(InvocableHandlerMethod.java:120)
	at org.springframework.kafka.listener.adapter.HandlerAdapter.invoke(HandlerAdapter.java:48)
	at org.springframework.kafka.listener.adapter.MessagingMessageListenerAdapter.invokeHandler(MessagingMessageListenerAdapter.java:334)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:86)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:51)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeOnMessage(KafkaMessageListenerContainer.java:1834)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeOnMessage(KafkaMessageListenerContainer.java:1817)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1760)
	... 8 common frames omitted
2020-05-26 13:27:27 - Exceptiion: 4 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:27:27 - [Consumer clientId=consumer-group_id-1, groupId=group_id] Seeking to offset 2215 for partition users-0
2020-05-26 13:27:27 - Error handler threw an exception
org.springframework.kafka.KafkaException: Seek to current after exception; nested exception is org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.SeekUtils.seekOrRecover(SeekUtils.java:157)
	at org.springframework.kafka.listener.SeekToCurrentErrorHandler.handle(SeekToCurrentErrorHandler.java:103)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeErrorHandler(KafkaMessageListenerContainer.java:1867)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1773)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeWithRecords(KafkaMessageListenerContainer.java:1701)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeRecordListener(KafkaMessageListenerContainer.java:1599)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeListener(KafkaMessageListenerContainer.java:1330)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.pollAndInvoke(KafkaMessageListenerContainer.java:1062)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.run(KafkaMessageListenerContainer.java:970)
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:515)
	at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.decorateException(KafkaMessageListenerContainer.java:1879)
	... 10 common frames omitted
Caused by: java.lang.IllegalArgumentException: null
	at com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(c_SemaphoreKafka_Exception.java:82)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:171)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.invoke(InvocableHandlerMethod.java:120)
	at org.springframework.kafka.listener.adapter.HandlerAdapter.invoke(HandlerAdapter.java:48)
	at org.springframework.kafka.listener.adapter.MessagingMessageListenerAdapter.invokeHandler(MessagingMessageListenerAdapter.java:334)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:86)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:51)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeOnMessage(KafkaMessageListenerContainer.java:1834)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeOnMessage(KafkaMessageListenerContainer.java:1817)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1760)
	... 8 common frames omitted
2020-05-26 13:27:36 - Exceptiion: 4 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:27:36 - [Consumer clientId=consumer-group_id-1, groupId=group_id] Seeking to offset 2215 for partition users-0
2020-05-26 13:27:36 - Error handler threw an exception
org.springframework.kafka.KafkaException: Seek to current after exception; nested exception is org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.SeekUtils.seekOrRecover(SeekUtils.java:157)
	at org.springframework.kafka.listener.SeekToCurrentErrorHandler.handle(SeekToCurrentErrorHandler.java:103)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeErrorHandler(KafkaMessageListenerContainer.java:1867)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1773)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeWithRecords(KafkaMessageListenerContainer.java:1701)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeRecordListener(KafkaMessageListenerContainer.java:1599)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeListener(KafkaMessageListenerContainer.java:1330)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.pollAndInvoke(KafkaMessageListenerContainer.java:1062)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.run(KafkaMessageListenerContainer.java:970)
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:515)
	at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.decorateException(KafkaMessageListenerContainer.java:1879)
	... 10 common frames omitted
Caused by: java.lang.IllegalArgumentException: null
	at com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(c_SemaphoreKafka_Exception.java:82)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:171)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.invoke(InvocableHandlerMethod.java:120)
	at org.springframework.kafka.listener.adapter.HandlerAdapter.invoke(HandlerAdapter.java:48)
	at org.springframework.kafka.listener.adapter.MessagingMessageListenerAdapter.invokeHandler(MessagingMessageListenerAdapter.java:334)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:86)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:51)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeOnMessage(KafkaMessageListenerContainer.java:1834)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeOnMessage(KafkaMessageListenerContainer.java:1817)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1760)
	... 8 common frames omitted
2020-05-26 13:27:43 - Exceptiion: 4 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:27:43 - [Consumer clientId=consumer-group_id-1, groupId=group_id] Seeking to offset 2215 for partition users-0
2020-05-26 13:27:43 - Error handler threw an exception
org.springframework.kafka.KafkaException: Seek to current after exception; nested exception is org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.SeekUtils.seekOrRecover(SeekUtils.java:157)
	at org.springframework.kafka.listener.SeekToCurrentErrorHandler.handle(SeekToCurrentErrorHandler.java:103)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeErrorHandler(KafkaMessageListenerContainer.java:1867)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1773)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeWithRecords(KafkaMessageListenerContainer.java:1701)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeRecordListener(KafkaMessageListenerContainer.java:1599)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeListener(KafkaMessageListenerContainer.java:1330)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.pollAndInvoke(KafkaMessageListenerContainer.java:1062)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.run(KafkaMessageListenerContainer.java:970)
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:515)
	at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.decorateException(KafkaMessageListenerContainer.java:1879)
	... 10 common frames omitted
Caused by: java.lang.IllegalArgumentException: null
	at com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(c_SemaphoreKafka_Exception.java:82)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:171)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.invoke(InvocableHandlerMethod.java:120)
	at org.springframework.kafka.listener.adapter.HandlerAdapter.invoke(HandlerAdapter.java:48)
	at org.springframework.kafka.listener.adapter.MessagingMessageListenerAdapter.invokeHandler(MessagingMessageListenerAdapter.java:334)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:86)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:51)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeOnMessage(KafkaMessageListenerContainer.java:1834)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeOnMessage(KafkaMessageListenerContainer.java:1817)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1760)
	... 8 common frames omitted
2020-05-26 13:27:50 - Exceptiion: 4 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:27:50 - Backoff FixedBackOff{interval=0, currentAttempts=10, maxAttempts=9} exhausted for ConsumerRecord(topic = users, partition = 0, leaderEpoch = 0, offset = 2215, CreateTime = 1590524793268, serialized key size = -1, serialized value size = 36, headers = RecordHeaders(headers = [], isReadOnly = false), key = null, value = 4 > testTue May 26 13:26:33 PDT 2020)
org.springframework.kafka.listener.ListenerExecutionFailedException: Listener method 'public void com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(java.lang.String) throws java.io.IOException,java.lang.InterruptedException' threw exception; nested exception is java.lang.IllegalArgumentException; nested exception is java.lang.IllegalArgumentException
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.decorateException(KafkaMessageListenerContainer.java:1879)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeErrorHandler(KafkaMessageListenerContainer.java:1867)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1773)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeWithRecords(KafkaMessageListenerContainer.java:1701)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeRecordListener(KafkaMessageListenerContainer.java:1599)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeListener(KafkaMessageListenerContainer.java:1330)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.pollAndInvoke(KafkaMessageListenerContainer.java:1062)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.run(KafkaMessageListenerContainer.java:970)
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:515)
	at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: java.lang.IllegalArgumentException: null
	at com.example.demo.c_SemaphoreKafka_Exception$ConsumerSemaphore.consume(c_SemaphoreKafka_Exception.java:82)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:171)
	at org.springframework.messaging.handler.invocation.InvocableHandlerMethod.invoke(InvocableHandlerMethod.java:120)
	at org.springframework.kafka.listener.adapter.HandlerAdapter.invoke(HandlerAdapter.java:48)
	at org.springframework.kafka.listener.adapter.MessagingMessageListenerAdapter.invokeHandler(MessagingMessageListenerAdapter.java:334)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:86)
	at org.springframework.kafka.listener.adapter.RecordMessagingMessageListenerAdapter.onMessage(RecordMessagingMessageListenerAdapter.java:51)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeOnMessage(KafkaMessageListenerContainer.java:1834)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.invokeOnMessage(KafkaMessageListenerContainer.java:1817)
	at org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.doInvokeRecordListener(KafkaMessageListenerContainer.java:1760)
	... 8 common frames omitted
2020-05-26 13:27:50 - [Consumer clientId=consumer-group_id-1, groupId=group_id] Seeking to offset 2216 for partition users-0
2020-05-26 13:27:50 - #### -> Started Consumed message -> 5 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:27:50 - #### -> Started Consumed message -> 6 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:27:50 - #### -> Started Consumed message -> 7 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:27:55 - #### -> Started Consumed message -> 8 > testTue May 26 13:26:33 PDT 2020
2020-05-26 13:27:55 - #### -> Started Consumed message -> 9 > testTue May 26 13:26:33 PDT 2020`

### Start Kafka
https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html

### Curl command
curl -X POST -F 'message=test' http://localhost:9000/kafka/publish

### Required
#### Sender Microservice

https://www.youtube.com/watch?v=bBTPZ9NdSk8&t=874s