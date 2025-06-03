# 📨 Python Outbox Pattern with Flask, PostgreSQL, RabbitMQ and Celery

![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)
![Flask](https://img.shields.io/badge/flask-API-blue?logo=flask)
![PostgreSQL](https://img.shields.io/badge/postgresql-db-blue?logo=postgresql)
![RabbitMQ](https://img.shields.io/badge/rabbitmq-broker-orange?logo=rabbitmq)
![Celery](https://img.shields.io/badge/celery-tasks-green?logo=celery)

This project is a prototype of the **[Transactional Outbox Pattern](https://microservices.io/patterns/data/transactional-outbox.html)** implemented using:
- **Flask** for the HTTP API
- **PostgreSQL** as the relational database
- **RabbitMQ** as the message broker
- **Celery** for asynchronous task processing
- **Celery Beat** for periodic task scheduling

---

## 📚 What is the Outbox Pattern?

The **Transactional Outbox** pattern ensures reliable event delivery in distributed systems by saving events in an **outbox** table within the same database transaction as the business operation, reducing the risk of inconsistencies between the database and messaging system.

> **Learn more**: [https://microservices.io/patterns/data/transactional-outbox.html](https://microservices.io/patterns/data/transactional-outbox.html)

---

## 🧩 Service Architecture

The project is divided into the following components:

| Service    | Description                                                                  |
|------------|------------------------------------------------------------------------------|
| `api`      | Flask REST API exposing endpoints for creating and listing orders.           |
| `database` | PostgreSQL database storing Orders and the Outbox table.                     |
| `rabbitmq` | RabbitMQ message broker with management UI.                                  |
| `worker`   | Celery Worker responsible for consuming tasks and processing Outbox events.  |
| `beat`     | Celery Beat scheduler that periodically triggers the Outbox processing task. |

---

## ⚙️ Technologies Used

- Python 3.11
- Flask
- SQLAlchemy
- PostgreSQL
- RabbitMQ
- Celery
- Celery Beat
- Alembic (for database migrations)
- Docker and Docker Compose

---

## 🚀 How to Run the Project

### 1. Prerequisites
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/) installed.

### 2. Clone the repository
```bash
git clone https://github.com/your-username/python-outbox-pattern.git
cd python-outbox-pattern
```

### 3. Start the containers
```bash
docker compose up --build

```
This will start:
- API at `http://localhost:5000`
- PostgreSQL at `localhost:5432`
- RabbitMQ Management at `http://localhost:15672` (user: `guest`, password: `guest`)

### 4. Run the migrations
In other terminal
```bash
docker compose exec api flask db upgrade

```
Algo if you want to work inside de container, there is a Make file with some commands. Just give a check up.

### 5. Using the API
Create a new order
```bash
POST http://localhost:5000/orders
Content-Type: application/json

{
  "customer_name": "John Doe",
  "price": 99.90
}
```
List orders
```bash
GET http://localhost:5000/orders

## 🛠️ Project Structure
```bash
.
├── src/
│   ├── controllers/       # Flask Controllers
│   ├── models/             # SQLAlchemy Models (Order, Outbox)
│   ├── repositories/       # Database access logic
│   ├── services/           # Business logic and messaging services
│   ├── enums/              # Enum for event statuses
│   ├── extensions.py       # Flask Extensions (SQLAlchemy, Migrate)
│   ├── tasks.py            # Celery Tasks definition
│   ├── celery_app.py       # Celery Configuration
│   └── __init__.py         # Flask App Factory
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
``` 
## 🗓️ How does the Outbox Processing Work?
1. The API saves the Order and the event in the Outbox table within the same database transaction.
2. Celery Beat periodically triggers the process_outbox task.
3. The task reads pending events from the Outbox and publishes them to RabbitMQ.
4. On successful delivery, the event status is updated to COMPLETED.

## 🖥️ Web Interface and Observability
**This project provides:**
1. A simple HTML Web Interface at GET /:
  - Register new orders.
  - List all existing orders.
  - View the Outbox entries.
2. Through the web interface, you can:
  - Create orders easily via a form.
  - Visualize all orders and their details.
  - Track the Outbox Pattern in action:
    - Orders are created.
    - Outbox events are initially saved with status PENDING.
    - Celery workers publish the events to RabbitMQ.
    - After successful delivery, the Outbox status changes to COMPLETED.

**You can see the entire flow working live:**
- Fill and submit the form to create a new order.
- Monitor the transition of Outbox events from PENDING to COMPLETED automatically.

## 📎 Useful Links
[Transactional Outbox Pattern](https://microservices.io/patterns/data/transactional-outbox.html)
[Celery Documentation](https://docs.celeryq.dev/en/stable/)
[Flask Documentation](https://flask.palletsprojects.com/en/stable/)

## 🚀 Ready to test your distributed systems the right way!