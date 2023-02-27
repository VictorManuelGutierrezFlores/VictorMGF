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
Country(code='ABW',name='Aruba',continent='North America',region='Caribbean',surface_area=193,independence_year=0,population=103000,life_expectancy=78.4,gnp=828,gnp_old=793,local_name='Aruba',government_form='Nonmetropolitan Territory of The Netherlands',head_of_state='Willem-Alexander',capital=129,code2='AW'), 
Country(code='AIA',name='Anguilla',continent='North America',region='Caribbean',surface_area=96,independence_year=0,population=8000,life_expectancy=76.1,gnp=63.2,gnp_old=0,local_name='Anguilla',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=62,code2='AI'), 
Country(code='ANT',name='Netherlands Antilles',continent='North America',region='Caribbean',surface_area=800,independence_year=0,population=217000,life_expectancy=74.7,gnp=1941,gnp_old=0,local_name='Nederlandse Antillen',government_form='Nonmetropolitan Territory of The Netherlands',head_of_state='Willem-Alexander',capital=33,code2='AN'), 
Country(code='ATG',name='Antigua and Barbuda',continent='North America',region='Caribbean',surface_area=442,independence_year=1981,population=68000,life_expectancy=70.5,gnp=612,gnp_old=584,local_name='Antigua and Barbuda',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=63,code2='AG'), 
Country(code='BLZ',name='Belize',continent='North America',region='Central America',surface_area=22696,independence_year=1981,population=241000,life_expectancy=70.9,gnp=630,gnp_old=616,local_name='Belize',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=185,code2='BZ'), 
Country(code='BLZ',name='Belize',continent='North America',region='Central America',surface_area=22696,independence_year=1981,population=241000,life_expectancy=70.9,gnp=630,gnp_old=616,local_name='Belize',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=185,code2='BZ'), 
Country(code='BMu',name='Bermuda',continent='North America',region='North America',surface_area=53,independence_year=0,population=65000,life_expectancy=76.9,gnp=2328,gnp_old=2190,local_name='Bermuda',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=191,code2='BM'), 
Country(code='BRB',name='Barbados',continent='North America',region='Caribbean',surface_area=430,independence_year=1966,population=270000,life_expectancy=73,gnp=2223,gnp_old=2186,local_name='Barbados',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=174,code2='BB'), 
Country(code='CAN',name='Canada',continent='North America',region='North America',surface_area=9970610,independence_year=1867,population=31147000,life_expectancy=79.4,gnp=598862,gnp_old=625626,local_name='Canada',government_form='Constitutional Monarchy, Federation',head_of_state='Elisabeth II',capital=1822,code2='CA'), 
Country(code='CRI',name='Costa Rica',continent='North America',region='Central America',surface_area=51100,independence_year=1821,population=4023000,life_expectancy=75.8,gnp=10226,gnp_old=9757,local_name='Costa Rica',government_form='Republic',head_of_state='Miguel angel RodrIguez EcheverrIa',capital=584,code2='CR'), 
Country(code='CuB',name='Cuba',continent='North America',region='Caribbean',surface_area=110861,independence_year=1902,population=11201000,life_expectancy=76.2,gnp=17843,gnp_old=18862,local_name='Cuba',government_form='Socialistic Republic',head_of_state='Fidel Castro Ruz',capital=2413,code2='Cu'), 
Country(code='CYM',name='Cayman Islands',continent='North America',region='Caribbean',surface_area=264,independence_year=0,population=38000,life_expectancy=78.9,gnp=1263,gnp_old=1186,local_name='Cayman Islands',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=553,code2='KY'), 
Country(code='DMA',name='Dominica',continent='North America',region='Caribbean',surface_area=751,independence_year=1978,population=71000,life_expectancy=73.4,gnp=256,gnp_old=243,local_name='Dominica',government_form='Republic',head_of_state='Vernon Shaw',capital=586,code2='DM'), 
Country(code='DOM',name='Dominican Republic',continent='North America',region='Caribbean',surface_area=48511,independence_year=1844,population=8495000,life_expectancy=73.2,gnp=15846,gnp_old=15076,local_name='Republica Dominicana',government_form='Republic',head_of_state='Hipolito MejIa DomInguez',capital=587,code2='DO'), 
Country(code='GLP',name='Guadeloupe',continent='North America',region='Caribbean',surface_area=1705,independence_year=0,population=456000,life_expectancy=77,gnp=3501,gnp_old=0,local_name='Guadeloupe',government_form='Overseas Department of France',head_of_state='Jacques Chirac',capital=919,code2='GP'), 
Country(code='GRD',name='Grenada',continent='North America',region='Caribbean',surface_area=344,independence_year=1974,population=94000,life_expectancy=64.5,gnp=318,gnp_old=0,local_name='Grenada',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=916,code2='GD'), 
Country(code='GRL',name='Greenland',continent='North America',region='North America',surface_area=2166090,independence_year=0,population=56000,life_expectancy=68.1,gnp=0,gnp_old=0,local_name='Kalaallit Nunaat/Gronland',government_form='Part of Denmark',head_of_state='Margrethe II',capital=917,code2='GL'), 
Country(code='GTM',name='Guatemala',continent='North America',region='Central America',surface_area=108889,independence_year=1821,population=11385000,life_expectancy=66.2,gnp=19008,gnp_old=17797,local_name='Guatemala',government_form='Republic',head_of_state='Alfonso Portillo Cabrera',capital=922,code2='GT'), 
Country(code='HND',name='Honduras',continent='North America',region='Central America',surface_area=112088,independence_year=1838,population=6485000,life_expectancy=69.9,gnp=5333,gnp_old=4697,local_name='Honduras',government_form='Republic',head_of_state='Carlos Roberto Flores Facusse',capital=933,code2='HN'), 
Country(code='HTI',name='Haiti',continent='North America',region='Caribbean',surface_area=27750,independence_year=1804,population=8222000,life_expectancy=49.2,gnp=3459,gnp_old=3107,local_name='Haiti/Dayti',government_form='Republic',head_of_state='Jean-Bertrand Aristide',capital=929,code2='HT'), 
Country(code='JAM',name='Jamaica',continent='North America',region='Caribbean',surface_area=10990,independence_year=1962,population=2583000,life_expectancy=75.2,gnp=6871,gnp_old=6722,local_name='Jamaica',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=1530,code2='JM'), 
Country(code='KNA',name='Saint Kitts and Nevis',continent='North America',region='Caribbean',surface_area=261,independence_year=1983,population=38000,life_expectancy=70.7,gnp=299,gnp_old=0,local_name='Saint Kitts and Nevis',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=3064,code2='KN'), 
Country(code='LCA',name='Saint Lucia',continent='North America',region='Caribbean',surface_area=622,independence_year=1979,population=154000,life_expectancy=72.3,gnp=571,gnp_old=0,local_name='Saint Lucia',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=3065,code2='LC'), 
Country(code='MEX',name='Mexico',continent='North America',region='Central America',surface_area=1958201,independence_year=1810,population=98881000,life_expectancy=71.5,gnp=414972,gnp_old=401461,local_name='Mexico',government_form='Federal Republic',head_of_state='Vicente Fox Quesada',capital=2515,code2='MX'), 
Country(code='MSR',name='Montserrat',continent='North America',region='Caribbean',surface_area=102,independence_year=0,population=11000,life_expectancy=78,gnp=109,gnp_old=0,local_name='Montserrat',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=2697,code2='MS'), 
Country(code='MTQ',name='Martinique',continent='North America',region='Caribbean',surface_area=1102,independence_year=0,population=395000,life_expectancy=78.3,gnp=2731,gnp_old=2559,local_name='Martinique',government_form='Overseas Department of France',head_of_state='Jacques Chirac',capital=2508,code2='MQ'), 
Country(code='NIC',name='Nicaragua',continent='North America',region='Central America',surface_area=130000,independence_year=1838,population=5074000,life_expectancy=68.7,gnp=1988,gnp_old=2023,local_name='Nicaragua',government_form='Republic',head_of_state='Arnoldo Aleman Lacayo',capital=2734,code2='NI'), 
Country(code='PAN',name='Panama',continent='North America',region='Central America',surface_area=75517,independence_year=1903,population=2856000,life_expectancy=75.5,gnp=9131,gnp_old=8700,local_name='Panama',government_form='Republic',head_of_state='Mireya Elisa Moscoso RodrIguez',capital=2882,code2='PA'), 
Country(code='PRI',name='Puerto Rico',continent='North America',region='Caribbean',surface_area=8875,independence_year=0,population=3869000,life_expectancy=75.6,gnp=34100,gnp_old=32100,local_name='Puerto Rico',government_form='Commonwealth of the uS',head_of_state='George W. Bush',capital=2919,code2='PR'), 
Country(code='SLV',name='El Salvador',continent='North America',region='Central America',surface_area=21041,independence_year=1841,population=6276000,life_expectancy=69.7,gnp=11863,gnp_old=11203,local_name='El Salvador',government_form='Republic',head_of_state='Francisco Guillermo Flores Perez',capital=645,code2='SV'), 
Country(code='SPM',name='Saint Pierre and Miquelon',continent='North America',region='North America',surface_area=242,independence_year=0,population=7000,life_expectancy=77.6,gnp=0,gnp_old=0,local_name='Saint-Pierre-et-Miquelon',government_form='Territorial Collectivity of France',head_of_state='Jacques Chirac',capital=3067,code2='PM'), 
Country(code='TCA',name='Turks and Caicos Islands',continent='North America',region='Caribbean',surface_area=430,independence_year=0,population=17000,life_expectancy=73.3,gnp=96,gnp_old=0,local_name='The Turks and Caicos Islands',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=3423,code2='TC'), 
Country(code='TTO',name='Trinidad and Tobago',continent='North America',region='Caribbean',surface_area=5130,independence_year=1962,population=1295000,life_expectancy=68,gnp=6232,gnp_old=5867,local_name='Trinidad and Tobago',government_form='Republic',head_of_state='Arthur N. R. Robinson',capital=3336,code2='TT'), 
Country(code='uSA',name='united States',continent='North America',region='North America',surface_area=9363520,independence_year=1776,population=278357000,life_expectancy=77.1,gnp=8510700,gnp_old=8110900,local_name='united States',government_form='Federal Republic',head_of_state='George W. Bush',capital=3813,code2='uS'), 
Country(code='VCT',name='Saint Vincent and the Grenadines',continent='North America',region='Caribbean',surface_area=388,independence_year=1979,population=114000,life_expectancy=72.3,gnp=285,gnp_old=0,local_name='Saint Vincent and the Grenadines',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=3066,code2='VC'), 
Country(code='VGB',name='Virgin Islands, British',continent='North America',region='Caribbean',surface_area=151,independence_year=0,population=21000,life_expectancy=75.4,gnp=612,gnp_old=573,local_name='British Virgin Islands',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=537,code2='VG'), 
Country(code='VIR',name='Virgin Islands, u.S.',continent='North America',region='Caribbean',surface_area=347,independence_year=0,population=93000,life_expectancy=78.1,gnp=0,gnp_old=0,local_name='Virgin Islands of the united States',government_form='uS Territory',head_of_state='George W. Bush',capital=4067,code2='VI'), 

]


# CREACION DE GET METHOD


@router.get("/North America/", status_code=200)
async def country():
    return (countries_list)


@router.get("/North America/{ID}")
async def country(ID: str):
    country = filter(lambda Country: Country.code == ID,
                     countries_list)  # Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code=404, detail="PAIS NO EXISTENTE")

# CREACION DE POST METHOD


@router.post("/North America/", status_code=201)
async def country(country: Country):
    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == country.code or saved_user.code == country.code2:
            raise HTTPException(status_code=409, detail="PAIS YA REGISTRADO")
    else:
        countries_list.append(country)
        return country
# http://127.0.0.1:8000/North America/

# CREACION DE PUT METHOD


@router.put("/North America/", status_code=200)
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


@router.delete("/North America/{id}", status_code=200)
async def country(id: str):

    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == id or saved_user.code2 == id:
            del countries_list[index]
            found = True
            return "PAIS ELIMINADO"

    if not found:
        raise HTTPException(status_code=401, detail="PAIS NO ENCONTRADO")
