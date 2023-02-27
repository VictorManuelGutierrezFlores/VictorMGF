# Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI, HTTPException
# Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
from fastapi import APIRouter


# Creamos un objeto a partir de la clase FastAPI
router = APIRouter()


# CREACION DEL BASEMODEL
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


# CREACION DE LISTA
# Country(code="", name="", continent="",region="", surface_area= , independece_year=, population=, life_expectancy=, gnp=, gnp_old=, local_name="", government_form="", head_of_state="", capital=, code="")
countries_list = [
    Country(code='ARG', name='Argentina', continent='South America', region='South America', surface_area=2780400, independence_year=1816, population=37032000,
            life_expectancy=75.1, gnp=340238, gnp_old=323310, local_name='Argentina', government_form='Federal Republic', head_of_state='Fernando de la Rua', capital=69, code2='AR'),
    Country(code='BOL', name='Bolivia', continent='South America', region='South America', surface_area=1098581, independence_year=1825, population=8329000,
            life_expectancy=63.7, gnp=8571, gnp_old=7967, local_name='Bolivia', government_form='Republic', head_of_state='Hugo Banzer Suarez', capital=194, code2='BO'),
    Country(code='BRA', name='Brazil', continent='South America', region='South America', surface_area=8547403, independence_year=1822, population=170115000, life_expectancy=62.9,
            gnp=776739, gnp_old=804108, local_name='Brasil', government_form='Federal Republic', head_of_state='Fernando Henrique Cardoso', capital=211, code2='BR'),
    Country(code='CHL', name='Chile', continent='South America', region='South America', surface_area=756626, independence_year=1810, population=15211000,
            life_expectancy=75.7, gnp=72949, gnp_old=75780, local_name='Chile', government_form='Republic', head_of_state='Ricardo Lagos Escobar', capital=554, code2='CL'),
    Country(code='COL', name='Colombia', continent='South America', region='South America', surface_area=1138914, independence_year=1810, population=42321000,
            life_expectancy=70.3, gnp=102896, gnp_old=105116, local_name='Colombia', government_form='Republic', head_of_state='Andres Pastrana Arango', capital=2257, code2='CO'),
    Country(code='ECu', name='Ecuador', continent='South America', region='South America', surface_area=283561, independence_year=1822, population=12646000,
            life_expectancy=71.1, gnp=19770, gnp_old=19769, local_name='Ecuador', government_form='Republic', head_of_state='Gustavo Noboa Bejarano', capital=594, code2='EC'),
    Country(code='FLK', name='Falkland Islands', continent='South America', region='South America', surface_area=12173, independence_year=0, population=2000, life_expectancy=0,
            gnp=0, gnp_old=0, local_name='Falkland Islands', government_form='Dependent Territory of the uK', head_of_state='Elisabeth II', capital=763, code2='FK'),
    Country(code='GuF', name='French Guiana', continent='South America', region='South America', surface_area=90000, independence_year=0, population=181000, life_expectancy=76.1,
            gnp=681, gnp_old=0, local_name='Guyane francaise', government_form='Overseas Department of France', head_of_state='Jacques Chirac', capital=3014, code2='GF'),
    Country(code='GuY', name='Guyana', continent='South America', region='South America', surface_area=214969, independence_year=1966, population=861000,
            life_expectancy=64, gnp=722, gnp_old=743, local_name='Guyana', government_form='Republic', head_of_state='Bharrat Jagdeo', capital=928, code2='GY'),
    Country(code='PER', name='Peru', continent='South America', region='South America', surface_area=1285216, independence_year=1821, population=25662000, life_expectancy=70,
            gnp=64140, gnp_old=65186, local_name='Peru/Piruw', government_form='Republic', head_of_state='Valentin Paniagua Corazao', capital=2890, code2='PE'),
    Country(code='PRY', name='Paraguay', continent='South America', region='South America', surface_area=406752, independence_year=1811, population=5496000,
            life_expectancy=73.7, gnp=8444, gnp_old=9555, local_name='Paraguay', government_form='Republic', head_of_state='Luis angel Gonzalez Macchi', capital=2885, code2='PY'),
    Country(code='SuR', name='Suriname', continent='South America', region='South America', surface_area=163265, independence_year=1975, population=417000,
            life_expectancy=71.4, gnp=870, gnp_old=706, local_name='Suriname', government_form='Republic', head_of_state='Ronald Venetiaan', capital=3243, code2='SR'),
    Country(code='uRY', name='uruguay', continent='South America', region='South America', surface_area=175016, independence_year=1828, population=3337000,
            life_expectancy=75.2, gnp=20831, gnp_old=19967, local_name='uruguay', government_form='Republic', head_of_state='Jorge Batlle Ibanez', capital=3492, code2='uY'),
    Country(code='VEN', name='Venezuela', continent='South America', region='South America', surface_area=912050, independence_year=1811, population=24170000,
            life_expectancy=73.1, gnp=95023, gnp_old=88434, local_name='Venezuela', government_form='Federal Republic', head_of_state='Hugo Chavez FrIas', capital=3539, code2='VE'),
]


# CREACION DE GET METHOD
@router.get("/South America/", status_code=200)
async def country():
    return (countries_list)


@router.get("/South America/{ID}")
async def country(ID: str):
    country = filter(lambda Country: Country.code == ID,
                     countries_list)  # Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code=404, detail="PAIS NO EXISTENTE")

# CREACION DE POST METHOD


@router.post("/South America/", status_code=201)
async def country(country: Country):
    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == country.code or saved_user.code == country.code2:
            raise HTTPException(status_code=409, detail="PAIS YA REGISTRADO")
    else:
        countries_list.append(country)
        return country
# http://127.0.0.1:8000/South America/

# CREACION DE PUT METHOD


@router.put("/South America/", status_code=200)
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


@router.delete("/South America/{id}", status_code=200)
async def country(id: str):

    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == id or saved_user.code2 == id:
            del countries_list[index]
            found = True
            return "PAIS ELIMINADO"

    if not found:
        raise HTTPException(status_code=401, detail="PAIS NO ENCONTRADO")
