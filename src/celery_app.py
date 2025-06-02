import os

from celery import Celery


def make_celery() -> Celery:
    rabbitmq_user = os.getenv("RABBITMQ_USER", "guest")
    rabbitmq_pass = os.getenv("RABBITMQ_PASS", "guest")
    rabbitmq_host = os.getenv("RABBITMQ_HOST", "localhost")
    rabbitmq_port = os.getenv("RABBITMQ_PORT", 5672)

    broker_url = (
        f"amqp://{rabbitmq_user}:{rabbitmq_pass}@{rabbitmq_host}:{rabbitmq_port}//"
    )

    celery = Celery("tasks", broker=broker_url)

    celery.conf.update(
        task_serializer="json",
        result_serializer="json",
        accept_content=["json"],
        timezone="UTC",
        enable_utc=True,
        beat_schedule={
            "process-outbox-every-5-seconds": {
                "task": "process_outbox",
                "schedule": 5.0,
            },
        },
    )

    import src.tasks  # import tasks to ensure they are registered with Celery

    return celery


celery_app = make_celery()
