from diagrams.onprem.compute import Server

from diagrams import Diagram
from diagrams.aws.compute import ECS

with Diagram("Consistent Hashing", show=False):
    # Create four servers
    server1 = Server("Server 1")
    server2 = Server("Server 2")
    server3 = Server("Server 3")
    server4 = Server("Server 4")
    server5 = Server("Server 5")
    server6 = Server("Server 6")

    collector1 = ECS("Collector 1")
    collector2 = ECS("Collector 2")
    collector3 = ECS("Collector 3")
    collector4 = ECS("Collector 4")

    # Connect servers to the consistent hashing ring
    server6 - collector1 - server1 - server5 - collector2 - server2 - server4 - collector3 - server3 - collector4 - server6
