from typing import Annotated
from fastapi import HTTPException
from sqlmodel import Session, select, create_engine
from models import Hero
from fastapi import APIRouter, Query, Depends

# Подключение/создание базы данных (Дубль)
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{ sqlite_file_name }"

connect_args = {"check_same_thread": False}

engine = create_engine(sqlite_url, connect_args=connect_args)
def get_session():
    with Session(engine) as session:
        yield session




def get_session():
    with Session(engine) as session:
        yield session



router = APIRouter()
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/heroes/")
def create_hero(hero: Hero, session: SessionDep) -> Hero:
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


# @router.get("/heroes/")
# def read_heroes(
#     session: SessionDep,
#     offset: int = 0,
#     limit: Annotated[int, Query(le=100)] = 100,
# ) -> list[Hero]:
#     heroes = session.exec(select(Hero))

#     return heroes


from collections import OrderedDict
@router.get("/heroes/", response_model=list[Hero])
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    fields = [field for field in Hero.model_fields.keys()]
    print(fields)
    result = []
    for hero in heroes:
        hero_dict = OrderedDict((field, getattr(hero, field)) for field in fields)
        result.append(hero_dict)
    return result


@router.get("/heroes/{hero_id}")
def read_hero(hero_id: int, session: SessionDep) -> Hero:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@router.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}