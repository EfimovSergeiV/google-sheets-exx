from typing import Union, Annotated
from fastapi import FastAPI, WebSocket, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import Session, SQLModel, select, create_engine

from models import Hero
from routes import sheets_route, socket_route


# Подключение/создание базы данных
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{ sqlite_file_name }"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)




app = FastAPI(
    title="Google sheets API",
    description="Google sheets API",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(socket_route.router)
app.include_router(sheets_route.router)


# Protected Routers
# app.include_router(
#     admin_route.router,
#     dependencies=[Depends(get_current_user)]
# )


###################################################
# Загрузка, сохранение данных в БД из Google Sheets
import gspread
from google.oauth2.service_account import Credentials

from methods.parsers import *
from methods.sheets import *
from conf import sheet_id

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)
workbook = client.open_by_key(sheet_id)

@app.get("/load_sheets/")
def load_sheets():
    print("load_sheets called")
    all_data = get_all_rows(workbook)
    with open("all_data.txt", "w", encoding="utf-8") as f:
        f.write(all_data.__str__())
    return {"status": "Data loaded successfully"}


@app.get("/write_sheets/")
def write_sheets():
    print("write_sheets called")
    import_data_from_file()
    return {"status": "Data written successfully"}

###################################################



# EXAMPLES

# @app.post("/heroes/")
# def create_hero(hero: Hero, session: SessionDep) -> Hero:
#     session.add(hero)
#     session.commit()
#     session.refresh(hero)
#     return hero


# @app.get("/heroes/")
# def read_heroes(
#     session: SessionDep,
#     offset: int = 0,
#     limit: Annotated[int, Query(le=100)] = 100,
# ) -> list[Hero]:
#     heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
#     return heroes


# @app.get("/heroes/{hero_id}")
# def read_hero(hero_id: int, session: SessionDep) -> Hero:
#     hero = session.get(Hero, hero_id)
#     if not hero:
#         raise HTTPException(status_code=404, detail="Hero not found")
#     return hero


# @app.delete("/heroes/{hero_id}")
# def delete_hero(hero_id: int, session: SessionDep):
#     hero = session.get(Hero, hero_id)
#     if not hero:
#         raise HTTPException(status_code=404, detail="Hero not found")
#     session.delete(hero)
#     session.commit()
#     return {"ok": True}