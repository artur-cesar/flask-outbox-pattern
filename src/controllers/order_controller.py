from flask import Blueprint

from src.services.order_service import OrderService

order_bp = Blueprint("order", __name__)


@order_bp.get("/orders")
def get_orders():
    order_service = OrderService()

    return order_service.get_all_orders()
