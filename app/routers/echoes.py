from typing import Any

from fastapi import APIRouter, HTTPException, Query, Request

import app.crud as crud
from app.models import Echo

router = APIRouter(prefix="/echoes")


def _add_base_url(echo: Echo, request: Request) -> dict[str, Any]:
    """Add the base URL to the echo's image path.

    Args:
        echo (Echo): The echo object.
        request (Request): The request object.

    Returns:
        dict[str, Any]: The echo dictionary with the updated image path.
    """
    echo_dict = echo.model_dump()
    echo_dict["image"] = str(request.base_url) + echo_dict["image"]
    return echo_dict


@router.get("/name/{echo_name}")
def get_echo_by_name_endpoint(echo_name: str, request: Request) -> dict[str, Any]:
    """Return a single echo by name.

    Lookup is case-insensitive.

    Args:
        echo_name (str): The name of the echo.
        request (Request): The request object.

    Returns:
        dict[str, Any]: The echo data.

    Raises:
        HTTPException: If the echo is not found.
    """
    echo = crud.get_echo_by_name(echo_name)
    if not echo:
        raise HTTPException(status_code=404, detail="Echo not found")
    return _add_base_url(echo, request)


@router.get("/all/")
def get_all_echoes_endpoint(
    request: Request, offset: int = 0, limit: int = Query(default=50, le=50)
) -> list[dict[str, Any]]:
    """Return all echoes.

    Args:
        request (Request): The request object.
        offset (int): The offset for pagination.
        limit (int): The limit for pagination.

    Returns:
        list[dict[str, Any]]: A list of all echoes.
    """
    return [
        _add_base_url(e, request)
        for e in crud.get_all_echoes(offset=offset, limit=limit)
    ]


@router.get("/objects/")
def get_object_echoes_endpoint(
    request: Request, offset: int = 0, limit: int = Query(default=50, le=50)
) -> list[dict[str, Any]]:
    """Return echoes of type "object".

    Returns echoes representing inanimate objects.

    Args:
        request (Request): The request object.
        offset (int): The offset for pagination.
        limit (int): The limit for pagination.

    Returns:
        list[dict[str, Any]]: A list of object echoes.
    """
    return [
        _add_base_url(e, request)
        for e in crud.get_object_echoes(offset=offset, limit=limit)
    ]


@router.get("/monsters/")
def get_monster_echoes_endpoint(
    request: Request, offset: int = 0, limit: int = Query(default=50, le=50)
) -> list[dict[str, Any]]:
    """Return echoes of type "monster".

    Returns echoes representing monsters.

    Args:
        request (Request): The request object.
        offset (int): The offset for pagination.
        limit (int): The limit for pagination.

    Returns:
        list[dict[str, Any]]: A list of monster echoes.
    """
    return [
        _add_base_url(e, request)
        for e in crud.get_monster_echoes(offset=offset, limit=limit)
    ]
