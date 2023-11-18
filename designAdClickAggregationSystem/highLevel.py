from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.onprem.database import Cassandra
from diagrams.onprem.compute import Server
from diagrams import Cluster, Diagram, Edge

with Diagram("High Level", show=False):

    logwatcher = Server("Logwatcher")
    data_aggregation = EC2("Data Aggregation Service")
    query_service = EC2("Query Service")

    cassandra_db = Cassandra("dB")

    logwatcher - Edge(label="Push Data") >> data_aggregation
    data_aggregation - Edge(label="(Ad count (Aggregate data for every min))") >> cassandra_db
    data_aggregation - Edge(label="Top 100 most clicked ads (Aggregated every minute)") >> cassandra_db
    cassandra_db - Edge(label="Query Data") << query_service