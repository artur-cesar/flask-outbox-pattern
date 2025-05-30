from typing import List

from src.models.order import Order


class OrderRepository:

    def list(self) -> List[Order]:
        return Order.query.all()
