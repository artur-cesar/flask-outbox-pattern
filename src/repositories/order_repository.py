from typing import List
from uuid import uuid4

from src.extensions import db
from src.models.order import Order


class OrderRepository:

    def list(self) -> List[Order]:
        return Order.query.all()

    def create(self, order_data: dict) -> Order:
        order = Order(
            id=uuid4(),
            customer_name=order_data["customer_name"],
            price=order_data["price"],
        )

        db.session.add(order)

        return order
