from typing import Sequence

from sqlalchemy import func
from sqlmodel import Session, select

from app.database import engine
from app.models import Echo


def get_echo_by_name(name: str) -> Echo | None:
    """Return a single echo by name.

    Lookup is case-insensitive and underscores in the provided name are treated as spaces.

    Args:
        name: The name of the echo to find (underscores required between words).

    Returns:
        Echo | None: The first matching Echo instance, or None if not found.
    """
    with Session(engine) as session:
        name = name.replace("_", " ")

        statement = select(Echo).where(func.lower(Echo.name) == name.lower())

        return session.exec(statement).first()


def get_echo_by_id(id: str) -> Echo | None:
    """Return a single echo by id.

    Args:
        id: The id of the echo to find.

    Returns:
        Echo | None: The first matching Echo instance, or None if not found.
    """
    with Session(engine) as session:
        statement = select(Echo).where(Echo.id == id)

        return session.exec(statement).first()


def get_all_echoes(offset: int, limit: int) -> Sequence[Echo]:
    """Return all echoes.

    Returns:
        Sequence[Echo]: All Echo records from the database.
    """
    with Session(engine) as session:
        statement = select(Echo).offset(offset).limit(limit)
        return session.exec(statement).all()


def get_monster_echoes(offset: int, limit: int) -> Sequence[Echo]:
    """Return echoes of type "monster".

    Returns:
        Sequence[Echo]: Echo records whose type is "monster".
    """
    with Session(engine) as session:
        statement = (
            select(Echo).where(Echo.type == "monster").offset(offset).limit(limit)
        )
        return session.exec(statement).all()


def get_object_echoes(offset: int, limit: int) -> Sequence[Echo]:
    """Return echoes of type "object".

    Returns:
        Sequence[Echo]: Echo records whose type is "object".
    """
    with Session(engine) as session:
        statement = (
            select(Echo).where(Echo.type == "object").offset(offset).limit(limit)
        )
        return session.exec(statement).all()
