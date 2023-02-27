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
Country(code='ASM',name='American Samoa',continent='Oceania',region='Polynesia',surface_area=199,independence_year=0,population=68000,life_expectancy=75.1,gnp=334,gnp_old=0,local_name='Amerika Samoa',government_form='uS Territory',head_of_state='George W. Bush',capital=54,code2='AS'), 
Country(code='AuS',name='Australia',continent='Oceania',region='Australia and New Zealand',surface_area=7741220,independence_year=1901,population=18886000,life_expectancy=79.8,gnp=351182,gnp_old=392911,local_name='Australia',government_form='Constitutional Monarchy, Federation',head_of_state='Elisabeth II',capital=135,code2='Au'), 
Country(code='CCK',name='Cocos (Keeling) Islands',continent='Oceania',region='Australia and New Zealand',surface_area=14,independence_year=0,population=600,life_expectancy=0,gnp=0,gnp_old=0,local_name='Cocos (Keeling) Islands',government_form='Territory of Australia',head_of_state='Elisabeth II',capital=2317,code2='CC'), 
Country(code='COK',name='Cook Islands',continent='Oceania',region='Polynesia',surface_area=236,independence_year=0,population=20000,life_expectancy=71.1,gnp=100,gnp_old=0,local_name='The Cook Islands',government_form='Nonmetropolitan Territory of New Zealand',head_of_state='Elisabeth II',capital=583,code2='CK'), 
Country(code='CXR',name='Christmas Island',continent='Oceania',region='Australia and New Zealand',surface_area=135,independence_year=0,population=2500,life_expectancy=0,gnp=0,gnp_old=0,local_name='Christmas Island',government_form='Territory of Australia',head_of_state='Elisabeth II',capital=1791,code2='CX'), 
Country(code='FJI',name='Fiji Islands',continent='Oceania',region='Melanesia',surface_area=18274,independence_year=1970,population=817000,life_expectancy=67.9,gnp=1536,gnp_old=2149,local_name='Fiji Islands',government_form='Republic',head_of_state='Josefa Iloilo',capital=764,code2='FJ'), 
Country(code='FSM',name='Micronesia, Federated States of',continent='Oceania',region='Micronesia',surface_area=702,independence_year=1990,population=119000,life_expectancy=68.6,gnp=212,gnp_old=0,local_name='Micronesia',government_form='Federal Republic',head_of_state='Leo A. Falcam',capital=2689,code2='FM'), 
Country(code='GuM',name='Guam',continent='Oceania',region='Micronesia',surface_area=549,independence_year=0,population=168000,life_expectancy=77.8,gnp=1197,gnp_old=1136,local_name='Guam',government_form='uS Territory',head_of_state='George W. Bush',capital=921,code2='Gu'), 
Country(code='KIR',name='Kiribati',continent='Oceania',region='Micronesia',surface_area=726,independence_year=1979,population=83000,life_expectancy=59.8,gnp=40.7,gnp_old=0,local_name='Kiribati',government_form='Republic',head_of_state='Teburoro Tito',capital=2256,code2='KI'), 
Country(code='MHL',name='Marshall Islands',continent='Oceania',region='Micronesia',surface_area=181,independence_year=1990,population=64000,life_expectancy=65.5,gnp=97,gnp_old=0,local_name='Marshall Islands/Majol',government_form='Republic',head_of_state='Kessai Note',capital=2507,code2='MH'), 
Country(code='NCL',name='New Caledonia',continent='Oceania',region='Melanesia',surface_area=18575,independence_year=0,population=214000,life_expectancy=72.8,gnp=3563,gnp_old=0,local_name='Nouvelle-Caledonie',government_form='Nonmetropolitan Territory of France',head_of_state='Jacques Chirac',capital=3493,code2='NC'), 
Country(code='NFK',name='Norfolk Island',continent='Oceania',region='Australia and New Zealand',surface_area=36,independence_year=0,population=2000,life_expectancy=0,gnp=0,gnp_old=0,local_name='Norfolk Island',government_form='Territory of Australia',head_of_state='Elisabeth II',capital=2806,code2='NF'), 
Country(code='NIu',name='Niue',continent='Oceania',region='Polynesia',surface_area=260,independence_year=0,population=2000,life_expectancy=0,gnp=0,gnp_old=0,local_name='Niue',government_form='Nonmetropolitan Territory of New Zealand',head_of_state='Elisabeth II',capital=2805,code2='Nu'), 
Country(code='NRu',name='Nauru',continent='Oceania',region='Micronesia',surface_area=21,independence_year=1968,population=12000,life_expectancy=60.8,gnp=197,gnp_old=0,local_name='Naoero/Nauru',government_form='Republic',head_of_state='Bernard Dowiyogo',capital=2728,code2='NR'), 
Country(code='NZL',name='New Zealand',continent='Oceania',region='Australia and New Zealand',surface_area=270534,independence_year=1907,population=3862000,life_expectancy=77.8,gnp=54669,gnp_old=64960,local_name='New Zealand/Aotearoa',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=3499,code2='NZ'), 
Country(code='PCN',name='Pitcairn',continent='Oceania',region='Polynesia',surface_area=49,independence_year=0,population=50,life_expectancy=0,gnp=0,gnp_old=0,local_name='Pitcairn',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=2912,code2='PN'), 
Country(code='PLW',name='Palau',continent='Oceania',region='Micronesia',surface_area=459,independence_year=1994,population=19000,life_expectancy=68.6,gnp=105,gnp_old=0,local_name='Belau/Palau',government_form='Republic',head_of_state='Kuniwo Nakamura',capital=2881,code2='PW'), 
Country(code='PNG',name='Papua New Guinea',continent='Oceania',region='Melanesia',surface_area=462840,independence_year=1975,population=4807000,life_expectancy=63.1,gnp=4988,gnp_old=6328,local_name='Papua New Guinea/Papua Niugini',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=2884,code2='PG'), 
Country(code='PYF',name='French Polynesia',continent='Oceania',region='Polynesia',surface_area=4000,independence_year=0,population=235000,life_expectancy=74.8,gnp=818,gnp_old=781,local_name='Polynesie francaise',government_form='Nonmetropolitan Territory of France',head_of_state='Jacques Chirac',capital=3016,code2='PF'), 
Country(code='SLB',name='Solomon Islands',continent='Oceania',region='Melanesia',surface_area=28896,independence_year=1978,population=444000,life_expectancy=71.3,gnp=182,gnp_old=220,local_name='Solomon Islands',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=3161,code2='SB'), 
Country(code='TKL',name='Tokelau',continent='Oceania',region='Polynesia',surface_area=12,independence_year=0,population=2000,life_expectancy=0,gnp=0,gnp_old=0,local_name='Tokelau',government_form='Nonmetropolitan Territory of New Zealand',head_of_state='Elisabeth II',capital=3333,code2='TK'), 
Country(code='TON',name='Tonga',continent='Oceania',region='Polynesia',surface_area=650,independence_year=1970,population=99000,life_expectancy=67.9,gnp=146,gnp_old=170,local_name='Tonga',government_form='Monarchy',head_of_state="Taufa'ahau Tupou IV",capital=3334,code2='TO'), 
Country(code='TuV',name='Tuvalu',continent='Oceania',region='Polynesia',surface_area=26,independence_year=1978,population=12000,life_expectancy=66.3,gnp=6,gnp_old=0,local_name='Tuvalu',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=3424,code2='TV'), 
Country(code='uMI',name='united States Minor Outlying Islands',continent='Oceania',region='Micronesia/Caribbean',surface_area=16,independence_year=0,population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name='united States Minor Outlying Islands',government_form='Dependent Territory of the uS',head_of_state='George W. Bush',capital=0,code2='uM'), 
Country(code='VuT',name='Vanuatu',continent='Oceania',region='Melanesia',surface_area=12189,independence_year=1980,population=190000,life_expectancy=60.6,gnp=261,gnp_old=246,local_name='Vanuatu',government_form='Republic',head_of_state='John Bani',capital=3537,code2='Vu'), 
Country(code='WLF',name='Wallis and Futuna',continent='Oceania',region='Polynesia',surface_area=200,independence_year=0,population=15000,life_expectancy=0,gnp=0,gnp_old=0,local_name='Wallis-et-Futuna',government_form='Nonmetropolitan Territory of France',head_of_state='Jacques Chirac',capital=3536,code2='WF'), 
Country(code='WSM',name='Samoa',continent='Oceania',region='Polynesia',surface_area=2831,independence_year=1962,population=180000,life_expectancy=69.2,gnp=141,gnp_old=157,local_name='Samoa',government_form='Parlementary Monarchy',head_of_state='Malietoa Tanumafili II',capital=3169,code2='WS'), 

]


# CREACION DE GET METHOD


@router.get("/Oceania/", status_code=200)
async def country():
    return (countries_list)


@router.get("/Oceania/{ID}")
async def country(ID: str):
    country = filter(lambda Country: Country.code == ID,
                     countries_list)  # Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code=404, detail="PAIS NO EXISTENTE")

# CREACION DE POST METHOD


@router.post("/Oceania/", status_code=201)
async def country(country: Country):
    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == country.code or saved_user.code == country.code2:
            raise HTTPException(status_code=409, detail="PAIS YA REGISTRADO")
    else:
        countries_list.append(country)
        return country
# http://127.0.0.1:8000/Oceania/

# CREACION DE PUT METHOD


@router.put("/Oceania/", status_code=200)
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


@router.delete("/Oceania/{id}", status_code=200)
async def country(id: str):

    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == id or saved_user.code2 == id:
            del countries_list[index]
            found = True
            return "PAIS ELIMINADO"

    if not found:
        raise HTTPException(status_code=401, detail="PAIS NO ENCONTRADO")
