"""add_processed_at_timestamp

Revision ID: 009e52eafc11
Revises: e8ddec1badf4
Create Date: 2025-06-02 18:50:57.361703

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "009e52eafc11"
down_revision = "e8ddec1badf4"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("outbox", schema=None) as batch_op:
        batch_op.add_column(sa.Column("processed_at", sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column("attempts", sa.Integer(), nullable=False))


def downgrade():
    with op.batch_alter_table("outbox", schema=None) as batch_op:
        batch_op.drop_column("attempts")
        batch_op.drop_column("processed_at")
