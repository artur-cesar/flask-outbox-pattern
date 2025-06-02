import json
import os
from typing import List

import pika

from src.celery_app import celery_app
from src.enums.event_status import EventStatus
from src.extensions import db
from src.models.outbox import Outbox
from src.repositories.outbox_repository import OutboxRepository
from src.services.message_service import MessageService


@celery_app.task(name="process_outbox")
def process_outbox():

    from src import create_app

    app = (
        create_app()
    )  # Ensure the app is created before using it, but only when the task is called

    with app.app_context():
        try:
            message_service = MessageService()
            outbox_repository = OutboxRepository()

            pending_events: List[Outbox] = outbox_repository.list_pending()

            for event in pending_events:
                try:
                    message_service.publish(
                        message=event.to_dict(),
                        queue="order.created",
                        topic="order_exchange",
                    )
                    print(f"Published event: {event.id} to RabbitMQ")
                    outbox_repository.update_status(event, EventStatus.COMPLETED)
                except Exception as e:
                    print(f"Failed to publish event {event.id}: {e}")

            print("All pending events have been processed and published to RabbitMQ.")
            db.session.commit()
        except Exception as e:
            print(f"Failed to connect/send to RabbitMQ: {e}")
            db.session.rollback()
        finally:
            if message_service:
                try:
                    message_service.close()
                except Exception as e:
                    print(f"Failed to close RabbitMQ connection: {e}")
