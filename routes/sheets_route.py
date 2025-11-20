from typing import Annotated
from fastapi import HTTPException
from sqlmodel import Session, select, create_engine
from models import Hero, M1, M2, M3, M4, M5, MachineAbstract 
from fastapi import APIRouter, Query, Depends
from fastapi.responses import HTMLResponse
from modules.database import create_db_and_tables, get_session, SessionDep


router = APIRouter()



@router.post("/heroes/")
def create_hero(hero: Hero, session: SessionDep) -> Hero:
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


from collections import OrderedDict
def normalize_keys(model_keys, data) -> list[dict]:
    """ Нормализация ключей в ответе API """
    fields = [field for field in model_keys]
    result = []

    for row in data:
        row_dict = OrderedDict((field, getattr(row, field)) for field in fields)
        result.append(row_dict)

    return result


@router.get("/heroes/", response_model=list[Hero])
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    # limit: Annotated[int, Query(le=100)] = 100, # Задать лимит на запрос к БД
    ) -> list[Hero]:

    # heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()  # Применить лимит на запрос к БД
    data = session.exec(select(Hero).offset(offset)).all()
    return normalize_keys(Hero.model_fields.keys(), data)


@router.get("/heroes/{hero_id}")
def read_hero(hero_id: int, session: SessionDep) -> Hero:
    data = session.get(Hero, hero_id)
    if not data:
        raise HTTPException(status_code=404, detail="Hero not found")
    return normalize_keys(Hero.model_fields.keys(), [data])[0]


@router.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return { "ok": True }



from modules.parsers import create_mashine

@router.get("/init-m/")
async def get(session: SessionDep):

    data = {
        "id": 1,
        "A": "Название машины",
        "B": "Номер заказа",
        "C": "Чертёж",
        "D": "Наименование",
        "E": "Количество",
        "F": "Дата начала (план)",
        "G": "Дата окончания (план)",
        "H": "Дата начала (факт)",
        "I": "Дата окончания (факт)",
        "J": "Следующая операция",
        "K": "Трудоёмкость",
        "L": "Необх. дата сдачи на сборку"
    }
    create_mashine(data, session=session)
    return HTMLResponse("Записали, если ошибка, значит уже записано")


@router.get("/m/{id}")
def read_m1(id: int, session: SessionDep) -> MachineAbstract:
    """ one id M"""
    data = session.get(M1, id)
    if not data:
        raise HTTPException(status_code=404, detail="M1 not found")
    return normalize_keys(MachineAbstract.model_fields.keys(), [data])[0]


@router.get("/m/all/")
def read_all_m(session: SessionDep, offset: int = 0):
    """ all id M """
    custom_json = { "M1": [], "M2": [], "M3": [], "M4": [], "M5": [] }
    for model in [ M1, M2, M3, M4, M5 ]:
        data = session.exec(select(model).offset(offset)).all()
        custom_json[model.__name__] = normalize_keys(MachineAbstract.model_fields.keys(), data)

    return custom_json