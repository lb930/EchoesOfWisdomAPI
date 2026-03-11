import os
from sqlmodel import SQLModel, create_engine

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable must be set")

engine = create_engine(DATABASE_URL, echo=True)

def create_db() -> None:
    SQLModel.metadata.create_all(engine)

