from diagrams import Diagram, Cluster, Sequence
from diagrams.onprem.database import MySQL
from diagrams.onprem.client import User

with Diagram("Sequence Diagram", show=False):
    with Sequence("User"):
        user = User("User")
        with Sequence("NewRecordService"):
            new_record_service = MySQL("NewRecordService")
            user >> new_record_service
            new_record_service >> MySQL("DataNode"): Save Record
            new_record_service << MySQL("DataNode"): Response

        with Sequence("SearchService"):
            search_service = MySQL("SearchService")
            user >> search_service
            search_service >> MySQL("Coordinator"): Calculate Shard ID
            MySQL("Coordinator") >> MySQL("DataNode"): Fetch Data
            MySQL("DataNode") >> search_service
            search_service << MySQL("Coordinator"): Shard ID
            search_service << user: Longest Orders
