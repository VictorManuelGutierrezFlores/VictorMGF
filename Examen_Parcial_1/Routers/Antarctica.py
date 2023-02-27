# CREACION DEL BASEMODEL
# Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI, HTTPException
# Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
from fastapi import APIRouter


# Creamos un objeto a partir de la clase FastAPI
router = APIRouter()


class Country(BaseModel):
    code: str
    name: str
    continent: str
    region: str
    surface_area: int
    independence_year: int
    population: int
    life_expectancy: float
    gnp: int
    gnp_old: int
    local_name: str
    government_form: str
    head_of_state: str
    capital: int
    code2: str


countries_list = [
    Country(code='ATA', name='Antarctica', continent='Antarctica', region='Antarctica', surface_area=13120000, independence_year=0, population=0,
            life_expectancy=0, gnp=0, gnp_old=0, local_name='N/A', government_form='Co-administrated', head_of_state='', capital=0, code2='AQ'),
    Country(code='ATF', name='French Southern territories', continent='Antarctica', region='Antarctica', surface_area=7780, independence_year=0, population=0, life_expectancy=0,
            gnp=0, gnp_old=0, local_name='Terres australes francaises', government_form='Nonmetropolitan Territory of France', head_of_state='Jacques Chirac', capital=0, code2='TF'),
    Country(code='BVT', name='Bouvet Island', continent='Antarctica', region='Antarctica', surface_area=59, independence_year=0, population=0, life_expectancy=0,
            gnp=0, gnp_old=0, local_name='Bouvetoya', government_form='Dependent Territory of Norway', head_of_state='Harald V', capital=0, code2='BV'),
    Country(code='HMD', name='Heard Island and McDonald Islands', continent='Antarctica', region='Antarctica', surface_area=359, independence_year=0, population=0,
            life_expectancy=0, gnp=0, gnp_old=0, local_name='Heard and McDonald Islands', government_form='Territory of Australia', head_of_state='Elisabeth II', capital=0, code2='HM'),
    Country(code='SGS', name='South Georgia and the South Sandwich Islands', continent='Antarctica', region='Antarctica', surface_area=3903, independence_year=0, population=0, life_expectancy=0,
            gnp=0, gnp_old=0, local_name='South Georgia and the South Sandwich Islands', government_form='Dependent Territory of the uK', head_of_state='Elisabeth II', capital=0, code2='GS'),

]


# CREACION DE GET METHOD


@router.get("/Antarctica/", status_code=200)
async def country():
    return (countries_list)


@router.get("/Antarctica/{ID}")
async def country(ID: str):
    country = filter(lambda Country: Country.code == ID,
                     countries_list)  # Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code=404, detail="PAIS NO EXISTENTE")

# CREACION DE POST METHOD


@router.post("/Antarctica/", status_code=201)
async def country(country: Country):
    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == country.code or saved_user.code == country.code2:
            raise HTTPException(status_code=409, detail="PAIS YA REGISTRADO")
    else:
        countries_list.append(country)
        return country
# http://127.0.0.1:8000/Antarctica/

# CREACION DE PUT METHOD


@router.put("/Antarctica/", status_code=200)
async def country(country: Country):

    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == country.code or saved_user.code == country.code2:
            countries_list[index] = country
            found = True
    if not found:
        raise HTTPException(status_code=406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

# DELETE METHOD


@router.delete("/Antarctica/{id}", status_code=200)
async def country(id: str):

    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == id or saved_user.code2 == id:
            del countries_list[index]
            found = True
            return "PAIS ELIMINADO"

    if not found:
        raise HTTPException(status_code=401, detail="PAIS NO ENCONTRADO")
