# Problems
1. Read messages from Kafka using Counting Semaphore.
2. Increase PERMITS, during increase in load 

## 1 Read messages from Kafka using Counting Semaphore

1. Read 3 messages by 3 threads,
2. Once permit is available, another thread starts reading the message

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

## 2. Increase PERMITS, during increase in load 

`if(charger.availablePermits()  == 0)
         charger.release(10);`
         
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
                     
### Start Kafka
https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html

### Curl command
curl -X POST -F 'message=test' http://localhost:9000/kafka/publish

### Required
#### Sender Microservice

https://www.youtube.com/watch?v=bBTPZ9NdSk8&t=874s