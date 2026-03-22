from typing import Optional
from sqlmodel import SQLModel


class Echo(SQLModel):
    name: str
    description: str
    base_cost: int
    image: str
    health: Optional[int] = None
    attack_dmg: Optional[int] = None
    size: str
    height: int
    type: str
