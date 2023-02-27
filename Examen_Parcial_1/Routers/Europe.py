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
    Country(code='ALB', name='Albania', continent='Europe', region='Southern Europe', surface_area=28748, independence_year=1912, population=3401200,
           life_expectancy=71.6, gnp=3205, gnp_old=2500, local_name='Shqiperia', government_form='Republic', head_of_state='Rexhep Mejdani', capital=34, code2='AL'),
    Country(code='AND', name='Andorra', continent='Europe', region='Southern Europe', surface_area=468, independence_year=1278, population=78000,
           life_expectancy=83.5, gnp=1630, gnp_old=0, local_name='Andorra', government_form='Parliamentary Coprincipality', head_of_state='', capital=55, code2='AD'),
    Country(code='AuT', name='Austria', continent='Europe', region='Western Europe', surface_area=83859, independence_year=1918, population=8091800, life_expectancy=77.7,
           gnp=211860, gnp_old=206025, local_name='osterreich', government_form='Federal Republic', head_of_state='Thomas Klestil', capital=1523, code2='AT'),
    Country(code='BEL', name='Belgium', continent='Europe', region='Western Europe', surface_area=30518, independence_year=1830, population=10239000, life_expectancy=77.8,
           gnp=249704, gnp_old=243948, local_name='Belgie/Belgique', government_form='Constitutional Monarchy, Federation', head_of_state='Albert II', capital=179, code2='BE'),
    Country(code='BGR', name='Bulgaria', continent='Europe', region='Eastern Europe', surface_area=110994, independence_year=1908, population=8190900,
           life_expectancy=70.9, gnp=12178, gnp_old=10169, local_name='Balgarija', government_form='Republic', head_of_state='Petar Stojanov', capital=539, code2='BG'),
    Country(code='BIH', name='Bosnia and Herzegovina', continent='Europe', region='Southern Europe', surface_area=51197, independence_year=1992, population=3972000,
           life_expectancy=71.5, gnp=2841, gnp_old=0, local_name='Bosna i Hercegovina', government_form='Federal Republic', head_of_state='Ante Jelavic', capital=201, code2='BA'),
    Country(code='BLR', name='Belarus', continent='Europe', region='Eastern Europe', surface_area=207600, independence_year=1991, population=10236000,
           life_expectancy=68, gnp=13714, gnp_old=0, local_name='Belarus', government_form='Republic', head_of_state='Aljaksandr LukaSenka', capital=3520, code2='BY'),
    Country(code='CHE', name='Switzerland', continent='Europe', region='Western Europe', surface_area=41284, independence_year=1499, population=7160400, life_expectancy=79.6,
           gnp=264478, gnp_old=256092, local_name='Schweiz/Suisse/Svizzera/Svizra', government_form='Federation', head_of_state='Adolf Ogi', capital=3248, code2='CH'),
    Country(code='CZE', name='Czech Republic', continent='Europe', region='Eastern Europe', surface_area=78866, independence_year=1993, population=10278100,
           life_expectancy=74.5, gnp=55017, gnp_old=52037, local_name='esko', government_form='Republic', head_of_state='Vaclav Havel', capital=3339, code2='CZ'),
    Country(code='DEu', name='Germany', continent='Europe', region='Western Europe', surface_area=357022, independence_year=1955, population=82164700, life_expectancy=77.4,
           gnp=2133367, gnp_old=2102826, local_name='Deutschland', government_form='Federal Republic', head_of_state='Johannes Rau', capital=3068, code2='DE'),
    Country(code='DNK', name='Denmark', continent='Europe', region='Nordic Countries', surface_area=43094, independence_year=800, population=5330000, life_expectancy=76.5,
           gnp=174099, gnp_old=169264, local_name='Danmark', government_form='Constitutional Monarchy', head_of_state='Margrethe II', capital=3315, code2='DK'),
    Country(code='ESP', name='Spain', continent='Europe', region='Southern Europe', surface_area=505992, independence_year=1492, population=39441700, life_expectancy=78.8,
           gnp=553233, gnp_old=532031, local_name='Espana', government_form='Constitutional Monarchy', head_of_state='Juan Carlos I', capital=653, code2='ES'),
    Country(code='EST', name='Estonia', continent='Europe', region='Baltic Countries', surface_area=45227, independence_year=1991, population=1439200,
           life_expectancy=69.5, gnp=5328, gnp_old=3371, local_name='Eesti', government_form='Republic', head_of_state='Lennart Meri', capital=3791, code2='EE'),
    Country(code='FIN', name='Finland', continent='Europe', region='Nordic Countries', surface_area=338145, independence_year=1917, population=5171300,
           life_expectancy=77.4, gnp=121914, gnp_old=119833, local_name='Suomi', government_form='Republic', head_of_state='Tarja Halonen', capital=3236, code2='FI'),
    Country(code='FRA', name='France', continent='Europe', region='Western Europe', surface_area=551500, independence_year=843, population=59225700,
           life_expectancy=78.8, gnp=1424285, gnp_old=1392448, local_name='France', government_form='Republic', head_of_state='Jacques Chirac', capital=2974, code2='FR'),
    Country(code='FRO', name='Faroe Islands', continent='Europe', region='Nordic Countries', surface_area=1399, independence_year=0, population=43000,
           life_expectancy=78.4, gnp=0, gnp_old=0, local_name='Foroyar', government_form='Part of Denmark', head_of_state='Margrethe II', capital=901, code2='FO'),
    Country(code='GBR', name='united Kingdom', continent='Europe', region='British Islands', surface_area=242900, independence_year=1066, population=59623400, life_expectancy=77.7,
           gnp=1378330, gnp_old=1296830, local_name='united Kingdom', government_form='Constitutional Monarchy', head_of_state='Elisabeth II', capital=456, code2='GB'),
    Country(code='GIB', name='Gibraltar', continent='Europe', region='Southern Europe', surface_area=6, independence_year=0, population=25000, life_expectancy=79,
           gnp=258, gnp_old=0, local_name='Gibraltar', government_form='Dependent Territory of the uK', head_of_state='Elisabeth II', capital=915, code2='GI'),
    Country(code='GRC', name='Greece', continent='Europe', region='Southern Europe', surface_area=131626, independence_year=1830, population=10545700,
           life_expectancy=78.4, gnp=120724, gnp_old=119946, local_name='Ellada', government_form='Republic', head_of_state='Kostis Stefanopoulos', capital=2401, code2='GR'),
    Country(code='HRV', name='Croatia', continent='Europe', region='Southern Europe', surface_area=56538, independence_year=1991, population=4473000,
           life_expectancy=73.7, gnp=20208, gnp_old=19300, local_name='Hrvatska', government_form='Republic', head_of_state='Stipe Mesic', capital=2409, code2='HR'),
    Country(code='HuN', name='Hungary', continent='Europe', region='Eastern Europe', surface_area=93030, independence_year=1918, population=10043200,
           life_expectancy=71.4, gnp=48267, gnp_old=45914, local_name='Magyarorszag', government_form='Republic', head_of_state='Ferenc Madl', capital=3483, code2='Hu'),
    Country(code='IRL', name='Ireland', continent='Europe', region='British Islands', surface_area=70273, independence_year=1921, population=3775100,
           life_expectancy=76.8, gnp=75921, gnp_old=73132, local_name='Ireland/eire', government_form='Republic', head_of_state='Mary McAleese', capital=1447, code2='IE'),
    Country(code='ISL', name='Iceland', continent='Europe', region='Nordic Countries', surface_area=103000, independence_year=1944, population=279000,
           life_expectancy=79.4, gnp=8255, gnp_old=7474, local_name='Island', government_form='Republic', head_of_state='olafur Ragnar GrImsson', capital=1449, code2='IS'),
    Country(code='ITA', name='Italy', continent='Europe', region='Southern Europe', surface_area=301316, independence_year=1861, population=57680000, life_expectancy=79,
           gnp=1161755, gnp_old=1145372, local_name='Italia', government_form='Republic', head_of_state='Carlo Azeglio Ciampi', capital=1464, code2='IT'),
    Country(code='LTu', name='Lithuania', continent='Europe', region='Baltic Countries', surface_area=65301, independence_year=1991, population=3698500,
           life_expectancy=69.1, gnp=10692, gnp_old=9585, local_name='Lietuva', government_form='Republic', head_of_state='Valdas Adamkus', capital=2447, code2='LT'),
    Country(code='LuX', name='Luxembourg', continent='Europe', region='Western Europe', surface_area=2586, independence_year=1867, population=435700, life_expectancy=77.1,
           gnp=16321, gnp_old=15519, local_name='Luxembourg/Letzebuerg', government_form='Constitutional Monarchy', head_of_state='Henri', capital=2452, code2='Lu'),
    Country(code='LVA', name='Latvia', continent='Europe', region='Baltic Countries', surface_area=64589, independence_year=1991, population=2424200,
           life_expectancy=68.4, gnp=6398, gnp_old=5639, local_name='Latvija', government_form='Republic', head_of_state='Vaira Vike-Freiberga', capital=2434, code2='LV'),
    Country(code='MCO', name='Monaco', continent='Europe', region='Western Europe', surface_area=1.5, independence_year=1861, population=34000, life_expectancy=78.8,
           gnp=776, gnp_old=0, local_name='Monaco', government_form='Constitutional Monarchy', head_of_state='Rainier III', capital=2695, code2='MC'),
    Country(code='MDA', name='Moldova', continent='Europe', region='Eastern Europe', surface_area=33851, independence_year=1991, population=4380000,
           life_expectancy=64.5, gnp=1579, gnp_old=1872, local_name='Moldova', government_form='Republic', head_of_state='Vladimir Voronin', capital=2690, code2='MD'),
    Country(code='MKD', name='Macedonia', continent='Europe', region='Southern Europe', surface_area=25713, independence_year=1991, population=2024000,
           life_expectancy=73.8, gnp=1694, gnp_old=1915, local_name='Makedonija', government_form='Republic', head_of_state='Boris Trajkovski', capital=2460, code2='MK'),
    Country(code='MLT', name='Malta', continent='Europe', region='Southern Europe', surface_area=316, independence_year=1964, population=380200,
           life_expectancy=77.9, gnp=3512, gnp_old=3338, local_name='Malta', government_form='Republic', head_of_state='Guido de Marco', capital=2484, code2='MT'),
    Country(code='NLD', name='Netherlands', continent='Europe', region='Western Europe', surface_area=41526, independence_year=1581, population=15864000, life_expectancy=78.3,
           gnp=371362, gnp_old=360478, local_name='Nederland', government_form='Constitutional Monarchy', head_of_state='Willem-Alexander', capital=5, code2='NL'),
    Country(code='NOR', name='Norway', continent='Europe', region='Nordic Countries', surface_area=323877, independence_year=1905, population=4478500, life_expectancy=78.7,
           gnp=145895, gnp_old=153370, local_name='Norge', government_form='Constitutional Monarchy', head_of_state='Harald V', capital=2807, code2='NO'),
    Country(code='POL', name='Poland', continent='Europe', region='Eastern Europe', surface_area=323250, independence_year=1918, population=38653600, life_expectancy=73.2,
           gnp=151697, gnp_old=135636, local_name='Polska', government_form='Republic', head_of_state='Aleksander Kwasniewski', capital=2928, code2='PL'),
    Country(code='PRT', name='Portugal', continent='Europe', region='Southern Europe', surface_area=91982, independence_year=1143, population=9997600,
           life_expectancy=75.8, gnp=105954, gnp_old=102133, local_name='Portugal', government_form='Republic', head_of_state='Jorge Sampaio', capital=2914, code2='PT'),
    Country(code='ROM', name='Romania', continent='Europe', region='Eastern Europe', surface_area=238391, independence_year=1878, population=22455500,
           life_expectancy=69.9, gnp=38158, gnp_old=34843, local_name='Romania', government_form='Republic', head_of_state='Ion Iliescu', capital=3018, code2='RO'),
    Country(code='RuS', name='Russian Federation', continent='Europe', region='Eastern Europe', surface_area=17075400, independence_year=1991, population=146934000,
           life_expectancy=67.2, gnp=276608, gnp_old=442989, local_name='Rossija', government_form='Federal Republic', head_of_state='Vladimir Putin', capital=3580, code2='Ru'),
    Country(code='SJM', name='Svalbard and Jan Mayen', continent='Europe', region='Nordic Countries', surface_area=62422, independence_year=0, population=3200, life_expectancy=0,
           gnp=0, gnp_old=0, local_name='Svalbard og Jan Mayen', government_form='Dependent Territory of Norway', head_of_state='Harald V', capital=938, code2='SJ'),
    Country(code='SMR', name='San Marino', continent='Europe', region='Southern Europe', surface_area=61, independence_year=885, population=27000,
           life_expectancy=81.1, gnp=510, gnp_old=0, local_name='San Marino', government_form='Republic', head_of_state='0', capital=3171, code2='SM'),
    Country(code='SVK', name='Slovakia', continent='Europe', region='Eastern Europe', surface_area=49012, independence_year=1993, population=5398700,
           life_expectancy=73.7, gnp=20594, gnp_old=19452, local_name='Slovensko', government_form='Republic', head_of_state='Rudolf Schuster', capital=3209, code2='SK'),
    Country(code='SVN', name='Slovenia', continent='Europe', region='Southern Europe', surface_area=20256, independence_year=1991, population=1987800,
           life_expectancy=74.9, gnp=19756, gnp_old=18202, local_name='Slovenija', government_form='Republic', head_of_state='Milan Kucan', capital=3212, code2='SI'),
    Country(code='SWE', name='Sweden', continent='Europe', region='Nordic Countries', surface_area=449964, independence_year=836, population=8861400, life_expectancy=79.6,
           gnp=226492, gnp_old=227757, local_name='Sverige', government_form='Constitutional Monarchy', head_of_state='Carl XVI Gustaf', capital=3048, code2='SE'),
    Country(code='uKR', name='ukraine', continent='Europe', region='Eastern Europe', surface_area=603700, independence_year=1991, population=50456000,
           life_expectancy=66, gnp=42168, gnp_old=49677, local_name='ukrajina', government_form='Republic', head_of_state='Leonid KutSma', capital=3426, code2='uA'),
    Country(code='VAT', name='Holy See (Vatican City State)', continent='Europe', region='Southern Europe', surface_area=0.4, independence_year=1929, population=1000, life_expectancy=0,
           gnp=9, gnp_old=0, local_name='Santa Sede/Citta del Vaticano', government_form='Independent Church State', head_of_state='Johannes Paavali II', capital=3538, code2='VA'),
    Country(code='YuG', name='Yugoslavia', continent='Europe', region='Southern Europe', surface_area=102173, independence_year=1918, population=10640000,
           life_expectancy=72.4, gnp=17000, gnp_old=0, local_name='Jugoslavija', government_form='Federal Republic', head_of_state='Vojislav KoStunica', capital=1792, code2='Yu'),

]

# CREACION DE GET METHOD


@router.get("/Europe/", status_code=200)
async def country():
    return (countries_list)


@router.get("/Europe/{ID}")
async def country(ID: str):
    country = filter(lambda Country: Country.code == ID,
                     countries_list)  # Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code=404, detail="PAIS NO EXISTENTE")

# CREACION DE POST METHOD


@router.post("/Europe/", status_code=201)
async def country(country: Country):
    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == country.code or saved_user.code == country.code2:
            raise HTTPException(status_code=409, detail="PAIS YA REGISTRADO")
    else:
        countries_list.append(country)
        return country
# http://127.0.0.1:8000/Europe/

# CREACION DE PUT METHOD


@router.put("/Europe/", status_code=200)
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


@router.delete("/Europe/{id}", status_code=200)
async def country(id: str):

    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == id or saved_user.code2 == id:
            del countries_list[index]
            found = True
            return "PAIS ELIMINADO"

    if not found:
        raise HTTPException(status_code=401, detail="PAIS NO ENCONTRADO")
