import json
import os

import pika

from src.adapters.rabbitmq_adapter import RabbitMQAdapter


class MessageService:

    def __init__(self, broker_adapter=None):
        try:
            self.broker_adapter = broker_adapter or RabbitMQAdapter(
                host=os.getenv("RABBITMQ_HOST", "localhost"),
                port=int(os.getenv("RABBITMQ_PORT", 5672)),
                user=os.getenv("RABBITMQ_USER", "guest"),
                password=os.getenv("RABBITMQ_PASS", "guest"),
            )

        except Exception as e:
            raise Exception(f"Failed to connect to RabbitMQ: {e}")

    def publish(self, message: dict, queue: str, topic: str = ""):
        if not self.broker_adapter:
            raise Exception("Broker not connected")

        if not self.broker_adapter.is_connected():
            self.broker_adapter.reconnect()

        self.broker_adapter.channel.queue_declare(queue=queue, durable=True)
        self.broker_adapter.channel.basic_publish(
            exchange=topic,
            routing_key=queue,
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2),
        )

    def close(self):
        self.broker_adapter.close()

    def connection(self):
        return self.broker_adapter.connection
