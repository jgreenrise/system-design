from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.onprem.database import Cassandra
from diagrams.onprem.compute import Server
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.queue import Kafka

graph_attr = {
    "bgcolor": "transparent",
}
with Diagram("SuddenBurstTraffic", show=True):

    svcA = Server("Service A")
    logwatcher = EC2("LogWatcher")
    data_aggregation = EC2("Data Aggregation Service")
    query_service = EC2("Query Service")
    raw_database = Cassandra("Raw dB")
    aggregated_dB = Cassandra("Aggregated dB")
    kafka_1 = Kafka("Message Queue")
    kafka_2 = Kafka("Message Queue")
    database_writer_1 = EC2("Database Writer")
    database_writer_2 = EC2("Database Writer")

    svcA >> logwatcher
    logwatcher - Edge(xlabel="Push Data") >> kafka_1
    kafka_1 >> database_writer_1 >> raw_database
    kafka_1 >> data_aggregation
    data_aggregation - Edge(label="(Ad count by min)") >> kafka_2
    data_aggregation - Edge(label="Top 100 most clicked ads (Aggregated every minute)") >> kafka_2

    kafka_2 >> database_writer_2 >> aggregated_dB
    aggregated_dB - Edge(label="Query Data") << query_service
