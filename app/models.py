from typing import Optional

from sqlmodel import Field, SQLModel


class Echo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    base_cost: int
    image: str
    hp: Optional[int] = None
    attack_dmg: Optional[int] = None
    size: str
    height: int
    type: str
