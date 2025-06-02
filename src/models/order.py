import uuid
from typing import Optional

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.extensions import db


class Order(db.Model):
    __tablename__ = "orders"

    id: Mapped[sa.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    customer_name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    price: Mapped[Optional[float]] = mapped_column(db.Float(precision=2))
    outbox = relationship(
        "Outbox",
        back_populates="order",
        cascade="all, delete-orphan",
    )
    created_at: Mapped[sa.DateTime] = mapped_column(
        sa.DateTime(timezone=True), server_default=sa.func.now()
    )

    def __init__(self, id, customer_name, price):
        self.id = id
        self.customer_name = customer_name
        self.price = price

    def __repr__(self):
        return f"Order(id={self.id}, customer_name={self.customer_name}, price={self.price})"

    def to_dict(self):
        return {
            "id": self.id,
            "customer_name": self.customer_name,
            "price": round(self.price, 2),
            "outbox": [outbox.to_dict() for outbox in self.outbox],
        }
