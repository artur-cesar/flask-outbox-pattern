import datetime
import uuid

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.enums.event_status import EventStatus
from src.extensions import db


class Outbox(db.Model):
    __tablename__ = "outbox"

    id: Mapped[sa.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    event_type: Mapped[str] = mapped_column(db.String(50))
    payload: Mapped[dict] = mapped_column(db.JSON)
    status: Mapped[EventStatus] = mapped_column(
        db.Enum(EventStatus), default=EventStatus.PENDING, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        db.DateTime, server_default=db.func.now()
    )
