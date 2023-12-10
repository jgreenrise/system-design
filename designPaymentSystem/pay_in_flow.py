from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("Pay-in flow", direction="LR", graph_attr=graph_attr):
    customer = Person(
        name="Buyer", description="When a user clicks the place order button, a payment event is generated and sent to the payment service."
    )

    with SystemBoundary("Internet Banking System"):
        payment_service = Container(
            name="Payment Service",
            technology = "J2EE Service",
            description="Orchestrate Payment Events, Conducts Risk Assessment, etc"
        )

        database = Database(
            name="Payment Event Database",
            technology="Oracle Database Schema",
            description="Stores payment event",
        )

        payment_executor = Container(
            name="Payment Executor",
            technology = "J2EE Service",
            description="The payment executor executes a single payment order via the payment service provider.",
        )

        database_paymentExecutor = Database(
            name="Payment Order Database",
            technology="Oracle Database Schema",
            description="The payment executor stores the payment order in the database.",
        )

        merchant_wallet_service = Container(
            name="Merchant Wallet",
            technology = "J2EE Service",
            description="Wallet server stores the merchant’s balance information",
        )

        database_merchant_wallet = Database(
            name="Merchant Wallet dB",
            technology="Oracle Database Schema",
            description="Wallet server stores the merchant’s balance information",
        )

        ledger_Service = Container(
            name="Ledger Service",
            technology = "J2EE Service",
            description="Applies double-entry accounting principle to maintain accurate and balanced records for effective financial management.",
        )

        database_ledger = Database(
            name="Ledger Database",
            technology="Oracle Database Schema",
            description="that records and organizes financial transactions",
        )

    with SystemBoundary("External Systems"):
        payment_service_provider = System(
            name="Payment Service Provider",
            description="Paypal, Stripe, etc",
            external=True
        )

        card_schemes = System(
            name="Card Schemes",
            description="VISA, MasterCard, etc",
            external=True
        )

    customer >> Relationship("1. Process Payment Event") >> payment_service
    payment_service >> Relationship("2. Stores the payment event in the database") >> database

    payment_service >> Relationship("3. Executes a single payment order via the payment service provide") >> payment_executor
    payment_executor >> Relationship("4. Stores payment order") >> database_paymentExecutor

    payment_executor >> Relationship("5. Calls an external PSP to process the credit card payment.") >> payment_service_provider
    payment_service_provider >> card_schemes

    payment_service >> Relationship("6. After successful payment processing, update wallet") >> merchant_wallet_service
    merchant_wallet_service >> Relationship("Update the merchant's wallet") >> database_merchant_wallet

    payment_service >> Relationship("7. The ledger service opens the new ledger information to the database.") >> ledger_Service
    ledger_Service >> Relationship("Update ledger dB") >> database_ledger

