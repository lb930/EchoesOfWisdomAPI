from typing import Sequence

from fastapi import APIRouter, HTTPException, Query

from ..crud import get_echo_by_name, get_echo_by_id, get_all_echoes, get_object_echoes, get_monster_echoes
from ..models import Echo

router = APIRouter(prefix="/echoes")


@router.get("/name/{echo_name}")
def get_echo_endpoint(echo_name: str) -> Echo:
    """Return a single echo by name.

    Lookup is case-insensitive. Returns the echo or raises HTTP 404 if not found.
    """
    echo = get_echo_by_name(echo_name)
    if not echo:
        raise HTTPException(status_code=404, detail="Echo not found")
    return echo


@router.get("/id/{echo_id}")
def get_echo_by_id_endpoint(echo_id: str) -> Echo:
    """Return a single echo by id.

    Returns the echo or raises HTTP 404 if not found.
    """
    echo = get_echo_by_id(echo_id)
    if not echo:
        raise HTTPException(status_code=404, detail="Echo not found")
    return echo


@router.get("/all/")
def get_all_echoes_endpoint(
    offset: int = 0, limit: int = Query(default=50, le=50)
) -> Sequence[Echo]:
    """Return all echoes.

    Returns a list of all echoes.
    """
    return get_all_echoes(offset=offset, limit=limit)


@router.get("/objects/")
def get_object_echoes_endpoint(
    offset: int = 0, limit: int = Query(default=50, le=50)
) -> Sequence[Echo]:
    """Return echoes of type "object".

    Returns echoes representing inanimate objects.
    """
    return get_object_echoes(offset=offset, limit=limit)


@router.get("/monsters/")
def get_monster_echoes_endpoint(
    offset: int = 0, limit: int = Query(default=50, le=50)
) -> Sequence[Echo]:
    """Return echoes of type "monster".

    Returns echoes representing monsters.
    """
    return get_monster_echoes(offset=offset, limit=limit)

