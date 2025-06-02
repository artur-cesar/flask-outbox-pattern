from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from src.requests.order_request import OrderRequest
from src.services.order_service import OrderService
from src.tasks import process_outbox

order_bp = Blueprint("order", __name__)
order_service = OrderService()


@order_bp.get("/orders")
def get_orders():
    return order_service.get_all_orders()


@order_bp.post("/orders")
def create_order():
    try:
        validate = OrderRequest(**request.json)
        return order_service.create(validate.dict())
    except ValidationError as e:
        return jsonify(e.errors()), 400
