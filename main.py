import json
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session, select

from app.database import create_db, engine
from app.models import Echo
from app.routers import echoes

echo_data_file = "data/echoes.json"

def load_seed_data(echo_data_file: str) -> None:
    with Session(engine) as session:
        exists = session.exec(select(Echo).limit(1)).first()
        if exists:
            return
        with open(echo_data_file, encoding="utf-8") as f:
            echoes_list = json.load(f)
        for echo_dict in echoes_list:
            session.add(Echo(**echo_dict))
        session.commit()

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    load_seed_data(echo_data_file)
    yield

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(echoes.router)

