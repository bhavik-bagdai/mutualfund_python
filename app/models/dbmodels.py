from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from app.db.database import metadata


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email",String, unique=True, nullable=False),
    Column("password", String, nullable=False),
)

portfolios = Table(
    "portfolios",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("scheme_name", String, nullable=False),
    Column("invested_amount",Float, nullable=False),
    Column("current_value",Float,nullable=False),
)