import os
import random
import sys
from uuid import uuid4

from faker import Faker

from src import create_app, db
from src.models.order import Order

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

fake = Faker()


def seed():
    orders = [
        Order(id=uuid4(), customer_name=fake.name(), price=random.uniform(10.0, 100.0)),
        Order(id=uuid4(), customer_name=fake.name(), price=random.uniform(10.0, 100.0)),
        Order(id=uuid4(), customer_name=fake.name(), price=random.uniform(10.0, 100.0)),
    ]

    db.session.bulk_save_objects(orders)
    db.session.commit()
    print("Database was seede successfully!")


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed()
