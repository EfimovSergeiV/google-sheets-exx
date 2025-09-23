from typing import Annotated
from sqlmodel import Field, Session, SQLModel
from fastapi import Depends, FastAPI, HTTPException, Query



class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str