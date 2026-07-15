"""
RetailIQ Database Module

Provides reusable database connection functions.
"""

from urllib.parse import quote_plus
from sqlalchemy import create_engine

from src.config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)

def get_engine():
    """
    Create and return a SQLAlchemy engine.
    """

    encoded_password = quote_plus(DB_PASSWORD)

    connection_string = (
        f"postgresql+psycopg2://"
        f"{DB_USER}:{encoded_password}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    return create_engine(connection_string)



