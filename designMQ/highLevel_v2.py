from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("highlevel", direction="LR", graph_attr=graph_attr):

    producers = Container(
        name="Producer",
        description="E Commerce Website.",
    )

    bank_account_seller = Container(
        name="Bank Account",
        description="Seller",
    )

    customer >> Relationship("Pay-in") >> bank_account_webApp
    bank_account_webApp >> Relationship("Pay-out") >> bank_account_seller
