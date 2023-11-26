from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.onprem.database import Cassandra
from diagrams.onprem.compute import Server
from diagrams import Cluster, Diagram, Edge
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

graph_attr = {
    "fontsize": "24",
    #"bgcolor": "transparent",
    "constraint":"False",
    "splines":"spline",
}

edge_attr = {
    "splines":"spline",
    "concentrate":"True"
}
with Diagram("High Level", direction="LR", show=True, graph_attr=graph_attr):

    with Cluster("User"):
        user = EC2("User")

    with Cluster("Database"):
        primary_db = RDS("Primary DB")
        replica_db1 = RDS("Replica DB 1")
        replica_db2 = RDS("Replica DB 2")
        replica_db3 = RDS("Replica DB 3")

    with Cluster("Load Balancer"):
        lb = ELB("Load Balancer")

    with Cluster("Search Service"):
        search_service = EC2("Search Service")
        search_service >> [replica_db1, replica_db2, replica_db3]

    with Cluster("Business Service"):
        business_service = EC2("Business Service")

        business_service >> primary_db
        primary_db >> Edge(label="replicate") >> [replica_db1, replica_db2, replica_db3]

    user >> lb >> [business_service, search_service]

