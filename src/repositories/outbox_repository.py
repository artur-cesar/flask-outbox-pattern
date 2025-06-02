from typing import List

from src.enums.event_status import EventStatus
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

    def list_pending(self) -> List[Outbox]:
        return Outbox.query.filter(Outbox.status == EventStatus.PENDING).all()

    def update_status(self, outbox: Outbox, status: EventStatus) -> None:
        outbox.status = status.value
        outbox.processed_at = db.func.now()
        outbox.attempts += 1

        db.session.add(outbox)
