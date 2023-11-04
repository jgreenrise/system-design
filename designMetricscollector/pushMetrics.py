from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.aws.network import ELB
from diagrams.aws.compute import ECS
from diagrams.aws.compute import EC2
from diagrams.gcp.iot import IotCore

with Diagram("Push Metrics", show=False):
    with Cluster("Metrics Source"):
        with Cluster("Collection Agent"):
            metrics1 = IotCore("Metrics 1")
            metrics2 = IotCore("Metrics 2")
            metrics3 = IotCore("Metrics 3")
        webServers = Server("Web Servers")

    loadBalancer = ELB("Load Balancer")

    # Note the "Push messages" between Collection Agent and Load Balancer
    Edge(label="Push messages") >> metrics2 >> loadBalancer

    # Web Servers push messages to the Collection Agent
    webServers >> metrics2

    with Cluster("Metrics collector"):
        svc_group = [EC2("worker1"),
                     EC2("worker2"),
                     EC2("worker3")]

    loadBalancer >> svc_group