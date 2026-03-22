import json
from typing import Sequence
from app.models import Echo

with open("data/echoes.json", encoding="utf-8") as f:
    _data = [Echo(**e) for e in json.load(f)]


def get_echo_by_name(name: str) -> Echo | None:
    """Return a single echo by name.

    Lookup is case-insensitive and underscores in the provided name are treated as spaces.

    Args:
        name: The name of the echo to find (underscores required between words).

    Returns:
        Echo | None: The first matching Echo instance, or None if not found.
    """
    name = name.replace("_", " ")
    return next((e for e in _data if e.name.lower() == name.lower()), None)


def get_echo_by_id(id: str) -> Echo | None:
    """Return a single echo by id.

    Args:
        id: The id of the echo to find.

    Returns:
        Echo | None: The first matching Echo instance, or None if not found.
    """
    return next((e for e in _data if str(e.id) == id), None)


def get_all_echoes(offset: int, limit: int) -> Sequence[Echo]:
    """Return all echoes.

    Returns:
        Sequence[Echo]: All Echo records from the database.
    """
    return _data[offset:limit]


def get_monster_echoes(offset: int, limit: int) -> Sequence[Echo]:
    """Return echoes of type "monster".

    Returns:
        Sequence[Echo]: Echo records whose type is "monster".
    """
    return [e for e in _data if e.type == "monster"][offset:limit]


def get_object_echoes(offset: int, limit: int) -> Sequence[Echo]:
    """Return echoes of type "object".

    Returns:
        Sequence[Echo]: Echo records whose type is "object".
    """
    return [e for e in _data if e.type == "object"][offset:limit]
