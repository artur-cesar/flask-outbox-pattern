from src.extensions import db
from src.models.outbox import Outbox


class OutboxRepository:

    def create(self, order_data: dict) -> None:
        outbox = Outbox(
            event_type="OrderCreated",
            payload={
                "order_id": str(order_data["id"]),
                "customer_name": order_data["customer_name"],
                "price": order_data["price"],
            },
        )

        db.session.add(outbox)
