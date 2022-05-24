"""init

Revision ID: f84686cff6de
Revises:
Create Date: 2022-05-24 19:50:58.611063

"""
from alembic import op
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, BOOLEAN, DATETIME

from app.core.config import settings
from app.utils.date import get_now

# revision identifiers, used by Alembic.
revision = 'f84686cff6de'
down_revision = None
branch_labels = None
depends_on = None

env = settings.ENV
database = settings.MYSQL_DATABASE

print("Migration env:", env)
print("Affecting database:", database)


def upgrade():
    op.create_table(
        'user',
        Column('id', INTEGER(unsigned=True), primary_key=True, index=True, autoincrement=True),
        Column('email', VARCHAR(255), unique=True, nullable=False),
        Column('password', VARCHAR(255), nullable=False),
        Column('name', VARCHAR(255), nullable=True),
        Column('is_active', BOOLEAN, default=True),
        Column('is_superuser', BOOLEAN, default=False),
        Column('created_at', DATETIME, nullable=True, default=get_now),
        Column('updated_at', DATETIME, nullable=True, default=get_now, onupdate=get_now)
    )


def downgrade():
    if env not in ['prod', 'staging']:
        op.drop_table('user')

