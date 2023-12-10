from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

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

with Diagram("\n\nPay-in flow with hosted PSP", show=True, direction="LR", graph_attr=graph_attr) as diag:
#with Diagram("\n\nPay-in flow with hosted PSP", show=True, direction="LR", graph_attr=graph_attr, edge_attr=edge_attr, ) as diag:
#with Diagram("\n\nPay-in flow with hosted PSP", show=True, direction="LR") as diag:

    checkout_page = Container(
        name="Checkout Page",
        technology = "UI App",
        description="User clicks the checkout button in the client browser.",
        bgColor="Green"
    )

    payment_page = Container(
        name="Payment Page",
        technology = "UI App",
        description=""
    )

    payment_complete_page = Container(
        name="Payment Complete Page",
        technology = "UI App",
        description=""
    )

    payment_service = System(
        name="Payment Service",
        description="",
    )

    database_token = Database(
        name="Token Database",
        technology="Oracle Database Schema",
        description="Stores token",
    )

    psp = System(
        name="PSP",
        description="",
    )

    checkout_page >> Relationship("1. Payment order sent") >> payment_service
    payment_service >> Relationship("2. Sends payment registration request with NONCE") >> psp

    psp >> Relationship("3. Return payment token") >> payment_service
    payment_service >> Relationship("4. Stores payment token") >> database_token

    payment_service >> Relationship("5. Display PSP's Payment page with token & redirectURL") >> payment_page
    payment_page >> Relationship("6. Start Payment") >> psp
    psp >> Relationship("7. Payment result") >> payment_page

    payment_page >> Relationship("8. Redirect to completion Page") >> payment_complete_page
    psp >> Relationship("9. Webhook with completion result") >> payment_service