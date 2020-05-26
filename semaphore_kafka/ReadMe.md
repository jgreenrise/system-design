# Problem Statement
Read messages from Kafka using Counting Semaphore

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

## Start Kafka
https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html

## Curl command
curl -X POST -F 'message=test' http://localhost:9000/kafka/publish

# Required
## Sender Microservice

https://www.youtube.com/watch?v=bBTPZ9NdSk8&t=874s