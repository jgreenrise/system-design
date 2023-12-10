from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Nginx
from diagrams.onprem.database import MySQL
from diagrams.onprem.queue import RabbitMQ
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.network import Etcd

# Create a custom shape for etcd and ZooKeeper
with Diagram("Pull Metrics", show=False):
    metricsCollector = Server("Metrics Collector")

    with Cluster("Metrics Sources"):
        web_servers = Nginx("Web Servers")
        db_clusters = MySQL("DB Clusters")
        queue_clusters = RabbitMQ("Queue Clusters")
        cache_clusters = Redis("Cache Clusters")

    Edge(label="Pull Metrics") << web_servers << metricsCollector
    Edge(label="Pull Metrics") << db_clusters << metricsCollector
    Edge(label="Pull Metrics") << queue_clusters << metricsCollector
    Edge(label="Pull Metrics") << cache_clusters << metricsCollector

    with Cluster("Service Discovery"):
        service_directory = Etcd("Service Directory")
        zookeeper = Server("ZooKeeper")

    metricsCollector >> zookeeper