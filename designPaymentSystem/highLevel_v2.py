from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("highlevel_v2", direction="LR", graph_attr=graph_attr):
    customer = Person(
        name="Buyer", description="Credit Card."
    )

    bank_account_webApp = Container(
        name="Bank Account",
        description="E Commerce Website.",
    )

    bank_account_seller = Container(
        name="Bank Account",
        description="Seller",
    )

    customer >> Relationship("Pay-in") >> bank_account_webApp
    bank_account_webApp >> Relationship("Pay-out") >> bank_account_seller
