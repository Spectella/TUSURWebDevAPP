from datetime import datetime, timezone
from sqlalchemy import MetaData, Table, Integer, String, TIMESTAMP, ForeignKey, Column, JSON, func, Boolean

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

# class Roles(metadata):
#     __tablename__ = "roles"
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     permissions = Column(JSON)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)

# class Users(metadata):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True)
#     email = Column(String, nullable=False)
#     username = Column(String, nullable=False)
#     password = Column(String, nullable=False)
#     registered_at = Column(TIMESTAMP, default=datetime.utcnow)
#     role_id = Column(Integer, ForeignKey("roles.id"))

