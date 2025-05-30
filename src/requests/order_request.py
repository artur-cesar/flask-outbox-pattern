from pydantic import BaseModel, ValidationError


class OrderRequest(BaseModel):
    customer_name: str
    price: float
