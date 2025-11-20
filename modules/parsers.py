
from time import sleep
from typing import Annotated
from sqlmodel import Session
from models import Hero, M1, M2, M3, M4, M5, MachineAbstract
from fastapi import Depends
from sqlmodel import Session, create_engine

from .sheets import *
from modules.database import create_db_and_tables, get_session, SessionDep, engine



def create_hero(hero: Hero, session: SessionDep) -> Hero:
    """ 
        Создание записи в базе HERO\n 
        FIXME: Тут нужно переименовать модель вместе с табл. на 'планировщик'
    """
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


def create_mashine(data: dict, session: SessionDep):
    """ 
        Создание записи в базе M1-M5\n
        Нет, вроде создаёт только таблицы в базе M1-M5
    """
    models = [M1, M2, M3, M4, M5]
    for model in models:
        obj = model(**data)
        session.add(obj)
    session.commit()
    return { "ok": True }


def export_data_to_file(workbook):
    """ Импорт данных из гугл таблицы в файл """
    all_data = get_all_rows(workbook)
    with open("all_data.txt", "w", encoding="utf-8") as f:
        f.write(all_data.__str__())


def import_data_from_file():
    """ Импорт данных из файла в базу """
    with open("all_data.txt", "r", encoding="utf-8") as f:
        all_data = eval(f.read())

    count = 0
    with Session(engine) as session:
        for data in all_data:
            count += 1
            print(f"\nROW { count } : lenght = { len(data) } : { data }\n\t-----")
            # Проверяем, что есть какие то данные и записываем в базу
            if len(data[0]) > 0 and len(data[1]) > 0:
                hero = Hero(
                    id=count, A=data[0], B=data[1], C=data[2], 
                    D=data[3], E=data[4], F=data[5], G=data[6], 
                    H=data[7], I=data[8], J=data[9], K=data[10], 
                    L=data[11], M=data[12], N=data[13], O=data[14], 
                    P=data[15], Q=data[16], R=data[17], S=data[18], 
                    T=data[19], U=data[20], V=data[21], W=data[22], 
                    X=data[23], Y=data[24], Z=data[25], AA=data[26], 
                    AB=data[27], AC=data[28], AD=data[29], AE=data[30], 
                    AF=data[31], AG=data[32], AH=data[33], AI=data[34], 
                    AJ=data[35], AK=data[36], AL=data[37], AM=data[38], 
                    AN=data[39], AO=data[40], AP=data[41], AQ=data[42], 
                    AR=data[43], AS=data[44], AT=data[45], AU=data[46], 
                    AV=data[47], AW=data[48], AX=data[49], AY=data[50], 
                    AZ=data[51], BA=data[52], BB=data[53], BC=data[54], 
                    BD=data[55], BE=data[56], BF=data[57], BG=data[58], 
                    BH=data[59], BI=data[60], BJ=data[61], BK=data[62], 
                    BL=data[63], BM=data[64], BN=data[65], BO=data[66], 
                    BP=data[67], BQ=data[68], BR=data[69], BS=data[70], 
                    BT=data[71], BU=data[72], BV=data[73], BW=data[74], 
                    BX=data[75], BY=data[76], BZ=data[77], CA=data[78], 
                    CB=data[79], CC=data[80], CD=data[81], CE=data[82], 
                    CF=data[83], CG=data[84], CH=data[85], CI=data[86], 
                    CJ=data[87], CK=data[88], CL=data[89], CM=data[90], 
                    CN=data[91], CO=data[92], CP=data[93])
                create_hero(hero, session=session)
