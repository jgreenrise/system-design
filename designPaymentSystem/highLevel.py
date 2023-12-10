from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.onprem.database import Cassandra
from diagrams.onprem.compute import Server
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.queue import Kafka
from diagrams.onprem.client import Users

graph_attr = {
    "bgcolor": "transparent",
}
with Diagram("", show=True):

    buyer = Users("Buyer")
    seller = Users("Seller")
    eCommerceWebApp = EC2("E Commerce Web App (Bank Account)")

    """
    data_aggregation = EC2("Data Aggregation Service")
    query_service = EC2("Query Service")
    raw_database = Cassandra("Raw dB")
    aggregated_dB = Cassandra("Aggregated dB")
    kafka_1 = Kafka("Message Queue")
    kafka_2 = Kafka("Message Queue")
    database_writer_1 = EC2("Database Writer")
    database_writer_2 = EC2("Database Writer")
    """

    buyer - Edge(label="Pay in flow") >> eCommerceWebApp
    eCommerceWebApp - Edge(label="Pay out flow") >> seller
