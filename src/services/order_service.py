from typing import List

from src.extensions import db
from src.models.order import Order
from src.models.outbox import Outbox
from src.repositories.order_repository import OrderRepository
from src.repositories.outbox_repository import OutboxRepository
from src.services.message_service import MessageService


class OrderService:

    def __init__(self, repository=None):
        self.repository = repository or OrderRepository()

    def get_all_orders(self) -> List[Order]:
        orders = self.repository.list()
        return [order.to_dict() for order in orders]

    def create(self, order_data: dict) -> Order:
        order = self.repository.create(order_data=order_data)
        outbox_repository = OutboxRepository()
        outbox_repository.create(order.to_dict())

        db.session.commit()

        return order.to_dict()
