"""relation_between_outbox_order

Revision ID: a8cceb0a4adf
Revises: 009e52eafc11
Create Date: 2025-06-02 22:43:16.368671

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a8cceb0a4adf"
down_revision = "009e52eafc11"
branch_labels = None
depends_on = None


def upgrade():

    with op.batch_alter_table("outbox", schema=None) as batch_op:
        batch_op.add_column(sa.Column("order_id", sa.UUID(), nullable=False))
        batch_op.create_foreign_key(None, "orders", ["order_id"], ["id"])


def downgrade():
    with op.batch_alter_table("outbox", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_column("order_id")
