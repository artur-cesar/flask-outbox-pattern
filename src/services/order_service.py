from typing import List

from src.models.order import Order
from src.repositories.order_repository import OrderRepository


class OrderService:

    def __init__(self, repository=None):
        self.repository = repository or OrderRepository()

    def get_all_orders(self) -> List[Order]:
        orders = self.repository.list()
        return [order.to_dict() for order in orders]
