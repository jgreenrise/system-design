from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import APIGateway
from diagrams.aws.network import ELB
from diagrams.aws.compute import ECS
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Mongodb
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import Kafka

graph_attr = {
    "fontsize": "24",
    #"bgcolor": "transparent",
    "constraint":"False",
    "splines":"spline",
}

#with Diagram("Location History System", graph_attr=graph_attr):
with Diagram("Assume user A comes online", direction = "TB", graph_attr=graph_attr):

    with Cluster("Users"):
        user_a = Server("User A")
        user_b = Server("User B")
        user_c = Server("User C")
        user_d = Server("User D")

    api_gateway = APIGateway("API Gateway")
    load_balancer = ELB("Load Balancer")

    with Cluster("Web Socket Servers"):
        session_service_1 = ECS("Node 1")
        session_service_2 = ECS("Node 2")
        session_service_3 = ECS("Node 3")
        session_service_4 = ECS("Node 4")

    with Cluster("Databases"):
        mongodB = Mongodb("Mongo DB")

    with Cluster("Messaging"):
        kafka_sns_sqs = Kafka("Kafka/SNS + SQS")

    outbound_message_worker = Server("Mssg Outbound svc")
    last_seen_service = Server("Last Seen svc")
    location_history_service = Server("Location hist svc")
    nearby_service = Server("Nearby Service")

    distributed_cache = Redis("Distributed Redis")

    user_a >> Edge(xlabel="1", color="darkGreen", style="bold", minLen="4") >> api_gateway
    api_gateway >> Edge(xlabel="12", color="darkBlue", style="bold", minLen="4") >> user_b

    api_gateway >> Edge(xlabel="2", color="darkGreen", style="bold", minLen="4") >> load_balancer
    load_balancer >> Edge(xlabel="11", color="darkBlue", style="bold", minLen="4") >> api_gateway

    load_balancer >> Edge(xlabel="3.", color="darkGreen", style="bold", minLen="4") >> session_service_2
    session_service_1 >> Edge(xlabel="10", color="darkBlue", style="bold", minLen="4") >> load_balancer

    session_service_2 >> Edge(xlabel="4.0", color="darkGreen", style="bold", minLen="10") >> [distributed_cache]
    session_service_2 >> Edge(xlabel="4.1", color="darkGreen", style="bold", minLen="10") >> kafka_sns_sqs

    outbound_message_worker >> Edge(xlabel="9", color="darkBlue", style="bold", minLen="4") >> [session_service_1]

    kafka_sns_sqs >> Edge(xlabel="8", color="darkBlue", style="bold", minLen="4") >> outbound_message_worker
    kafka_sns_sqs >> Edge(xlabel="5.1.", color="darkGreen", style="bold", minLen="4") >> last_seen_service
    kafka_sns_sqs >> Edge(xlabel="5.2", color="darkGreen", style="bold", minLen="4") >> location_history_service
    kafka_sns_sqs >> Edge(xlabel="5.3", color="darkGreen", style="bold", minLen="4") >> nearby_service
    nearby_service >> Edge(xlabel="7", color="darkBlue", style="bold", minLen="4") >> kafka_sns_sqs


    location_history_service >> mongodB
    last_seen_service >> mongodB

    nearby_service >> Edge(xlabel="6.", color="darkGreen", style="bold", minLen="2") >> distributed_cache