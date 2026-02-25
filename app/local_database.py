"""Database setup for Echoes of Wisdom API.

Provides the SQLModel engine and a helper to create database tables.
"""

from sqlalchemy.engine import Engine
from sqlmodel import SQLModel, create_engine

engine: Engine = create_engine("sqlite:///database.db")


def create_db() -> None:
    """Create database tables from SQLModel metadata.

    This will create all tables on the configured engine (the local SQLite file).
    """
    SQLModel.metadata.create_all(engine)
