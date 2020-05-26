# Problem Statement
Read messages from Kafka using Counting Semaphore

1. Read 3 messages by 3 threads,
2. Once permit is available, another thread starts reading the message

2020-05-25 17:36:20.934  INFO 26055 --- [nio-9000-exec-1] c.e.d.SemaphoreKafkaApplication$Producer : #### -> Producing message -> 1 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:20.934  INFO 26055 --- [nio-9000-exec-1] c.e.d.SemaphoreKafkaApplication$Producer : #### -> Producing message -> 2 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:20.934  INFO 26055 --- [nio-9000-exec-1] c.e.d.SemaphoreKafkaApplication$Producer : #### -> Producing message -> 3 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:20.934  INFO 26055 --- [nio-9000-exec-1] c.e.d.SemaphoreKafkaApplication$Producer : #### -> Producing message -> 4 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:20.934  INFO 26055 --- [nio-9000-exec-1] c.e.d.SemaphoreKafkaApplication$Producer : #### -> Producing message -> 5 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:20.935  INFO 26055 --- [nio-9000-exec-1] c.e.d.SemaphoreKafkaApplication$Producer : #### -> Producing message -> 6 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:20.935  INFO 26055 --- [nio-9000-exec-1] c.e.d.SemaphoreKafkaApplication$Producer : #### -> Producing message -> 7 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:20.935  INFO 26055 --- [nio-9000-exec-1] c.e.d.SemaphoreKafkaApplication$Producer : #### -> Producing message -> 8 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:20.935  INFO 26055 --- [nio-9000-exec-1] c.e.d.SemaphoreKafkaApplication$Producer : #### -> Producing message -> 9 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:20.956  INFO 26055 --- [     Thread-128] aphoreKafkaApplication$ConsumerSemaphore : #### -> Started Consumed message -> 1 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:20.957  INFO 26055 --- [     Thread-129] aphoreKafkaApplication$ConsumerSemaphore : #### -> Started Consumed message -> 2 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:20.957  INFO 26055 --- [     Thread-130] aphoreKafkaApplication$ConsumerSemaphore : #### -> Started Consumed message -> 3 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:27.523  INFO 26055 --- [     Thread-128] aphoreKafkaApplication$ConsumerSemaphore : #### -> Completed Consumed message -> 1 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:27.524  INFO 26055 --- [     Thread-131] aphoreKafkaApplication$ConsumerSemaphore : #### -> Started Consumed message -> 4 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:29.116  INFO 26055 --- [     Thread-129] aphoreKafkaApplication$ConsumerSemaphore : #### -> Completed Consumed message -> 2 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:29.117  INFO 26055 --- [     Thread-132] aphoreKafkaApplication$ConsumerSemaphore : #### -> Started Consumed message -> 5 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:30.508  INFO 26055 --- [     Thread-130] aphoreKafkaApplication$ConsumerSemaphore : #### -> Completed Consumed message -> 3 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:30.508  INFO 26055 --- [     Thread-133] aphoreKafkaApplication$ConsumerSemaphore : #### -> Started Consumed message -> 6 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:34.137  INFO 26055 --- [     Thread-131] aphoreKafkaApplication$ConsumerSemaphore : #### -> Completed Consumed message -> 4 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:34.138  INFO 26055 --- [     Thread-127] aphoreKafkaApplication$ConsumerSemaphore : #### -> Started Consumed message -> 0 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:36.279  INFO 26055 --- [     Thread-133] aphoreKafkaApplication$ConsumerSemaphore : #### -> Completed Consumed message -> 6 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:36.280  INFO 26055 --- [     Thread-134] aphoreKafkaApplication$ConsumerSemaphore : #### -> Started Consumed message -> 7 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:37.019  INFO 26055 --- [     Thread-132] aphoreKafkaApplication$ConsumerSemaphore : #### -> Completed Consumed message -> 5 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:37.019  INFO 26055 --- [     Thread-135] aphoreKafkaApplication$ConsumerSemaphore : #### -> Started Consumed message -> 8 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:39.570  INFO 26055 --- [     Thread-127] aphoreKafkaApplication$ConsumerSemaphore : #### -> Completed Consumed message -> 0 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:39.570  INFO 26055 --- [     Thread-136] aphoreKafkaApplication$ConsumerSemaphore : #### -> Started Consumed message -> 9 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:44.044  INFO 26055 --- [     Thread-134] aphoreKafkaApplication$ConsumerSemaphore : #### -> Completed Consumed message -> 7 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:45.302  INFO 26055 --- [     Thread-136] aphoreKafkaApplication$ConsumerSemaphore : #### -> Completed Consumed message -> 9 > testMon May 25 17:36:20 PDT 2020
2020-05-25 17:36:46.076  INFO 26055 --- [     Thread-135] aphoreKafkaApplication$ConsumerSemaphore : #### -> Completed Consumed message -> 8 > testMon May 25 17:36:20 PDT 2020

## Start Kafka
https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html

## Curl command
curl -X POST -F 'message=test' http://localhost:9000/kafka/publish

# Required
## Sender Microservice

https://www.youtube.com/watch?v=bBTPZ9NdSk8&t=874s