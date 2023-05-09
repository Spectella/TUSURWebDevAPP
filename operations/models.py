from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()

operations = Table(
    "operation",
    metadata,
    Column("id", )
)