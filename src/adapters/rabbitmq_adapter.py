import pika


class RabbitMQAdapter:
    def __init__(self, host: str, port: int, user: str, password: str):

        self.pika = pika
        self.connection = None
        self.channel = None
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def connect(self):
        credentials = self.pika.PlainCredentials(self.user, self.password)
        parameters = self.pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            credentials=credentials,
            heartbeat=600,
            blocked_connection_timeout=300,
        )

        try:
            self.connection = self.pika.BlockingConnection(parameters=parameters)
            self.channel = self.connection.channel()
        except Exception as e:
            raise ConnectionError(f"Failed to connect to RabbitMQ: {e}")

    def is_connected(self):
        return self.connection and self.connection.is_open

    def reconnect(self):
        self.close()
        self.connect()

    def close(self):
        if self.connection and self.connection.is_open:
            self.connection.close()
