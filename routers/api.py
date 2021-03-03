from fastapi import APIRouter, Depends
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
router = APIRouter()


engine = create_engine(
    "mssql+pyodbc://sa:gjghj,eqgjl,thb@172.16.4.58:1433/General?driver=ODBC+Driver+17+for+SQL+Server")
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    return Session()


@router.get("/")
async def an_endpoint_using_sql(db=Depends(get_db)):
    # ...
    # do some SQLAlchemy
    # ...
    return {"msg": "an exceptionally successful operation!"}


@router.get("/getCities/region-id={region_id}/")
async def get_city(region_id: int, db=Depends(get_db)):
    return db.execute(f"SELECT id, name FROM General.dbo.vCities WHERE id_region = {region_id}").fetchall()


@router.get("/getCities/")
async def get_cities(db=Depends(get_db)):
    return db.execute("SELECT id, name FROM General.dbo.vCities").fetchall()


@router.get("/getAddress/city-id={city_id}/")
async def get_address(city_id: int, db=Depends(get_db)):
    return db.execute(f"EXEC General.dbo.getAddress @city_id = {city_id}").fetchall()


@router.get("/getRegions/")
async def get_regions(db=Depends(get_db)):
    return db.execute(f"SELECT id, name FROM General.dbo.vRegions").fetchall()
