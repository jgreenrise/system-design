from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.onprem.database import Cassandra
from diagrams.onprem.compute import Server
from diagrams import Cluster, Diagram, Edge

graph_attr = {
    "bgcolor": "transparent",
}
with Diagram("High Level", show=True, graph_attr=graph_attr):

    svcA = Server("Service A")
    logwatcher = EC2("LogWatcher")
    data_aggregation = EC2("Data Aggregation Service")
    query_service = EC2("Query Service")
    raw_database = Cassandra("Raw dB")
    cassandra_db = Cassandra("Aggregated dB")

    svcA >> logwatcher
    logwatcher - Edge(xlabel="Push Data") >> data_aggregation
    data_aggregation - Edge(label="(Ad count by min)") >> cassandra_db
    data_aggregation - Edge(label="Top 100 most clicked ads (Aggregated every minute)") >> cassandra_db
    cassandra_db - Edge(label="Query Data") << query_service
    logwatcher - Edge(label="Raw Data") >> raw_database
