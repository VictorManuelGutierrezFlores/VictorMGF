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
    Country(code='AGO', name='Angola', continent='Africa', region='Central Africa', surface_area=1246700, independence_year=1975, population=12878000,
           life_expectancy=38.3, gnp=6648, gnp_old=7984, local_name='Angola', government_form='Republic', head_of_state='Jose Eduardo dos Santos', capital=56, code2='AO'),
    Country(code='BDI', name='Burundi', continent='Africa', region='Eastern Africa', surface_area=27834, independence_year=1962, population=6695000,
           life_expectancy=46.2, gnp=903, gnp_old=982, local_name='Burundi/uburundi', government_form='Republic', head_of_state='Pierre Buyoya', capital=552, code2='BI'),
    Country(code='BEN', name='Benin', continent='Africa', region='Western Africa', surface_area=112622, independence_year=1960, population=6097000,
           life_expectancy=50.2, gnp=2357, gnp_old=2141, local_name='Benin', government_form='Republic', head_of_state='Mathieu Kerekou', capital=187, code2='BJ'),
    Country(code='BFA', name='Burkina Faso', continent='Africa', region='Western Africa', surface_area=274000, independence_year=1960, population=11937000,
           life_expectancy=46.7, gnp=2425, gnp_old=2201, local_name='Burkina Faso', government_form='Republic', head_of_state='Blaise Compaore', capital=549, code2='BF'),
    Country(code='BWA', name='Botswana', continent='Africa', region='Southern Africa', surface_area=581730, independence_year=1966, population=1622000,
           life_expectancy=39.3, gnp=4834, gnp_old=4935, local_name='Botswana', government_form='Republic', head_of_state='Festus G. Mogae', capital=204, code2='BW'),
    Country(code='CAF', name='Central African Republic', continent='Africa', region='Central Africa', surface_area=622984, independence_year=1960, population=3615000,
           life_expectancy=44, gnp=1054, gnp_old=993, local_name='Centrafrique/Be-Afrika', government_form='Republic', head_of_state='Ange-Felix Patasse', capital=1889, code2='CF'),
    Country(code='CIV', name='Cote dIvoire', continent='Africa', region='Western Africa', surface_area=322463, independence_year=1960, population=14786000,
           life_expectancy=45.2, gnp=11345, gnp_old=10285, local_name='Cote dIvoire', government_form='Republic', head_of_state='Laurent Gbagbo', capital=2814, code2='CI'),
    Country(code='CMR', name='Cameroon', continent='Africa', region='Central Africa', surface_area=475442, independence_year=1960, population=15085000,
           life_expectancy=54.8, gnp=9174, gnp_old=8596, local_name='Cameroun/Cameroon', government_form='Republic', head_of_state='Paul Biya', capital=1804, code2='CM'),
    Country(code='COD', name='Congo, The Democratic Republic of the', continent='Africa', region='Central Africa', surface_area=2344858, independence_year=1960, population=51654000,
           life_expectancy=48.8, gnp=6964, gnp_old=2474, local_name='Republique Democratique du Congo', government_form='Republic', head_of_state='Joseph Kabila', capital=2298, code2='CD'),
    Country(code='COG', name='Congo', continent='Africa', region='Central Africa', surface_area=342000, independence_year=1960, population=2943000,
           life_expectancy=47.4, gnp=2108, gnp_old=2287, local_name='Congo', government_form='Republic', head_of_state='Denis Sassou-Nguesso', capital=2296, code2='CG'),
    Country(code='COM', name='Comoros', continent='Africa', region='Eastern Africa', surface_area=1862, independence_year=1975, population=578000, life_expectancy=60,
           gnp=4401, gnp_old=4361, local_name='Komori/Comores', government_form='Republic', head_of_state='Azali Assoumani', capital=2295, code2='KM'),
    Country(code='CPV', name='Cape Verde', continent='Africa', region='Western Africa', surface_area=4033, independence_year=1975, population=428000, life_expectancy=68.9,
           gnp=435, gnp_old=420, local_name='Cabo Verde', government_form='Republic', head_of_state='Antonio Mascarenhas Monteiro', capital=1859, code2='CV'),
    Country(code='DJI', name='Djibouti', continent='Africa', region='Eastern Africa', surface_area=23200, independence_year=1977, population=638000, life_expectancy=50.8,
           gnp=382, gnp_old=373, local_name='Djibouti/Jibuti', government_form='Republic', head_of_state='Ismail Omar Guelleh', capital=585, code2='DJ'),
    Country(code='DZA', name='Algeria', continent='Africa', region='Northern Africa', surface_area=2381741, independence_year=1962, population=31471000, life_expectancy=69.7,
           gnp=49982, gnp_old=46966, local_name='Al-Jazair/Algerie', government_form='Republic', head_of_state='Abdelaziz Bouteflika', capital=35, code2='DZ'),
    Country(code='EGY', name='Egypt', continent='Africa', region='Northern Africa', surface_area=1001449, independence_year=1922, population=68470000,
           life_expectancy=63.3, gnp=82710, gnp_old=75617, local_name='Misr', government_form='Republic', head_of_state='Hosni Mubarak', capital=608, code2='EG'),
    Country(code='ERI', name='Eritrea', continent='Africa', region='Eastern Africa', surface_area=117600, independence_year=1993, population=3850000, life_expectancy=55.8,
           gnp=650, gnp_old=755, local_name='Ertra', government_form='Republic', head_of_state='Isayas Afewerki [Isaias Afwerki]', capital=652, code2='ER'),
    Country(code='ESH', name='Western Sahara', continent='Africa', region='Northern Africa', surface_area=266000, independence_year=0, population=293000, life_expectancy=49.8,
           gnp=60, gnp_old=0, local_name='As-Sahrawiya', government_form='Occupied by Marocco', head_of_state='Mohammed Abdel Aziz', capital=2453, code2='EH'),
    Country(code='ETH', name='Ethiopia', continent='Africa', region='Eastern Africa', surface_area=1104300, independence_year=-1000, population=62565000,
           life_expectancy=45.2, gnp=6353, gnp_old=6180, local_name='YeItyop iya', government_form='Republic', head_of_state='Negasso Gidada', capital=756, code2='ET'),
    Country(code='GAB', name='Gabon', continent='Africa', region='Central Africa', surface_area=267668, independence_year=1960, population=1226000,
           life_expectancy=50.1, gnp=5493, gnp_old=5279, local_name='Le Gabon', government_form='Republic', head_of_state='Omar Bongo', capital=902, code2='GA'),
    Country(code='GHA', name='Ghana', continent='Africa', region='Western Africa', surface_area=238533, independence_year=1957, population=20212000,
           life_expectancy=57.4, gnp=7137, gnp_old=6884, local_name='Ghana', government_form='Republic', head_of_state='John Kufuor', capital=910, code2='GH'),
    Country(code='GIN', name='Guinea', continent='Africa', region='Western Africa', surface_area=245857, independence_year=1958, population=7430000,
           life_expectancy=45.6, gnp=2352, gnp_old=2383, local_name='Guinee', government_form='Republic', head_of_state='Lansana Conte', capital=926, code2='GN'),
    Country(code='GMB', name='Gambia', continent='Africa', region='Western Africa', surface_area=11295, independence_year=1965, population=1305000,
           life_expectancy=53.2, gnp=320, gnp_old=325, local_name='The Gambia', government_form='Republic', head_of_state='Yahya Jammeh', capital=904, code2='GM'),
    Country(code='GNB', name='Guinea-Bissau', continent='Africa', region='Western Africa', surface_area=36125, independence_year=1974, population=1213000,
           life_expectancy=49, gnp=293, gnp_old=272, local_name='Guine-Bissau', government_form='Republic', head_of_state='Kumba Iala', capital=927, code2='GW'),
    Country(code='GNQ', name='Equatorial Guinea', continent='Africa', region='Central Africa', surface_area=28051, independence_year=1968, population=453000, life_expectancy=53.6,
           gnp=283, gnp_old=542, local_name='Guinea Ecuatorial', government_form='Republic', head_of_state='Teodoro Obiang Nguema Mbasogo', capital=2972, code2='GQ'),
    Country(code='IOT', name='British Indian Ocean Territory', continent='Africa', region='Eastern Africa', surface_area=78, independence_year=0, population=0, life_expectancy=0,
           gnp=0, gnp_old=0, local_name='British Indian Ocean Territory', government_form='Dependent Territory of the uK', head_of_state='Elisabeth II', capital=0, code2='IO'),
    Country(code='KEN', name='Kenya', continent='Africa', region='Eastern Africa', surface_area=580367, independence_year=1963, population=30080000,
           life_expectancy=48, gnp=9217, gnp_old=10241, local_name='Kenya', government_form='Republic', head_of_state='Daniel arap Moi', capital=1881, code2='KE'),
    Country(code='LBR', name='Liberia', continent='Africa', region='Western Africa', surface_area=111369, independence_year=1847, population=3154000,
           life_expectancy=51, gnp=2012, gnp_old=0, local_name='Liberia', government_form='Republic', head_of_state='Charles Taylor', capital=2440, code2='LR'),
    Country(code='LBY', name='Libyan Arab Jamahiriya', continent='Africa', region='Northern Africa', surface_area=1759540, independence_year=1951, population=5605000,
           life_expectancy=75.5, gnp=44806, gnp_old=40562, local_name='Libiya', government_form='Socialistic State', head_of_state='Muammar al-Qadhafi', capital=2441, code2='LY'),
    Country(code='LSO', name='Lesotho', continent='Africa', region='Southern Africa', surface_area=30355, independence_year=1966, population=2153000, life_expectancy=50.8,
           gnp=1061, gnp_old=1161, local_name='Lesotho', government_form='Constitutional Monarchy', head_of_state='Letsie III', capital=2437, code2='LS'),
    Country(code='MAR', name='Morocco', continent='Africa', region='Northern Africa', surface_area=446550, independence_year=1956, population=28351000, life_expectancy=69.1,
           gnp=36124, gnp_old=33514, local_name='Al-Maghrib', government_form='Constitutional Monarchy', head_of_state='Mohammed VI', capital=2486, code2='MA'),
    Country(code='MDG', name='Madagascar', continent='Africa', region='Eastern Africa', surface_area=587041, independence_year=1960, population=15942000, life_expectancy=55,
           gnp=3750, gnp_old=3545, local_name='Madagasikara/Madagascar', government_form='Federal Republic', head_of_state='Didier Ratsiraka', capital=2455, code2='MG'),
    Country(code='MLI', name='Mali', continent='Africa', region='Western Africa', surface_area=1240192, independence_year=1960, population=11234000,
           life_expectancy=46.7, gnp=2642, gnp_old=2453, local_name='Mali', government_form='Republic', head_of_state='Alpha Oumar Konare', capital=2482, code2='ML'),
    Country(code='MOZ', name='Mozambique', continent='Africa', region='Eastern Africa', surface_area=801590, independence_year=1975, population=19680000,
           life_expectancy=37.5, gnp=2891, gnp_old=2711, local_name='Mocambique', government_form='Republic', head_of_state='JoaquIm A. Chissano', capital=2698, code2='MZ'),
    Country(code='MRT', name='Mauritania', continent='Africa', region='Western Africa', surface_area=1025520, independence_year=1960, population=2670000, life_expectancy=50.8,
           gnp=998, gnp_old=1081, local_name='Muritaniya/Mauritanie', government_form='Republic', head_of_state='Maaouiya Ould Sid Ahmad Taya', capital=2509, code2='MR'),
    Country(code='MuS', name='Mauritius', continent='Africa', region='Eastern Africa', surface_area=2040, independence_year=1968, population=1158000,
           life_expectancy=71, gnp=4251, gnp_old=4186, local_name='Mauritius', government_form='Republic', head_of_state='Cassam uteem', capital=2511, code2='Mu'),
    Country(code='MWI', name='Malawi', continent='Africa', region='Eastern Africa', surface_area=118484, independence_year=1964, population=10925000,
           life_expectancy=37.6, gnp=1687, gnp_old=2527, local_name='Malawi', government_form='Republic', head_of_state='Bakili Muluzi', capital=2462, code2='MW'),
    Country(code='MYT', name='Mayotte', continent='Africa', region='Eastern Africa', surface_area=373, independence_year=0, population=149000, life_expectancy=59.5,
           gnp=0, gnp_old=0, local_name='Mayotte', government_form='Territorial Collectivity of France', head_of_state='Jacques Chirac', capital=2514, code2='YT'),
    Country(code='NAM', name='Namibia', continent='Africa', region='Southern Africa', surface_area=824292, independence_year=1990, population=1726000,
           life_expectancy=42.5, gnp=3101, gnp_old=3384, local_name='Namibia', government_form='Republic', head_of_state='Sam Nujoma', capital=2726, code2='NA'),
    Country(code='NER', name='Niger', continent='Africa', region='Western Africa', surface_area=1267000, independence_year=1960, population=10730000,
           life_expectancy=41.3, gnp=1706, gnp_old=1580, local_name='Niger', government_form='Republic', head_of_state='Mamadou Tandja', capital=2738, code2='NE'),
    Country(code='NGA', name='Nigeria', continent='Africa', region='Western Africa', surface_area=923768, independence_year=1960, population=111506000, life_expectancy=51.6,
           gnp=65707, gnp_old=58623, local_name='Nigeria', government_form='Federal Republic', head_of_state='Olusegun Obasanjo', capital=2754, code2='NG'),
    Country(code='REu', name='Reunion', continent='Africa', region='Eastern Africa', surface_area=2510, independence_year=0, population=699000, life_expectancy=72.7,
           gnp=8287, gnp_old=7988, local_name='Reunion', government_form='Overseas Department of France', head_of_state='Jacques Chirac', capital=3017, code2='RE'),
    Country(code='RWA', name='Rwanda', continent='Africa', region='Eastern Africa', surface_area=26338, independence_year=1962, population=7733000,
           life_expectancy=39.3, gnp=2036, gnp_old=1863, local_name='Rwanda/urwanda', government_form='Republic', head_of_state='Paul Kagame', capital=3047, code2='RW'),
    Country(code='SDN', name='Sudan', continent='Africa', region='Northern Africa', surface_area=2505813, independence_year=1956, population=29490000, life_expectancy=56.6,
           gnp=10162, gnp_old=0, local_name='As-Sudan', government_form='Islamic Republic', head_of_state='Omar Hassan Ahmad al-Bashir', capital=3225, code2='SD'),
    Country(code='SEN', name='Senegal', continent='Africa', region='Western Africa', surface_area=196722, independence_year=1960, population=9481000, life_expectancy=62.2,
           gnp=4787, gnp_old=4542, local_name='Senegal/Sounougal', government_form='Republic', head_of_state='Abdoulaye Wade', capital=3198, code2='SN'),
    Country(code='SHN', name='Saint Helena', continent='Africa', region='Western Africa', surface_area=314, independence_year=0, population=6000, life_expectancy=76.8,
           gnp=0, gnp_old=0, local_name='Saint Helena', government_form='Dependent Territory of the uK', head_of_state='Elisabeth II', capital=3063, code2='SH'),
    Country(code='SLE', name='Sierra Leone', continent='Africa', region='Western Africa', surface_area=71740, independence_year=1961, population=4854000,
           life_expectancy=45.3, gnp=746, gnp_old=858, local_name='Sierra Leone', government_form='Republic', head_of_state='Ahmed Tejan Kabbah', capital=3207, code2='SL'),
    Country(code='SOM', name='Somalia', continent='Africa', region='Eastern Africa', surface_area=637657, independence_year=1960, population=10097000,
           life_expectancy=46.2, gnp=935, gnp_old=0, local_name='Soomaaliya', government_form='Republic', head_of_state='Abdiqassim Salad Hassan', capital=3214, code2='SO'),
    Country(code='STP', name='Sao Tome and Principe', continent='Africa', region='Central Africa', surface_area=964, independence_year=1975, population=147000,
           life_expectancy=65.3, gnp=6, gnp_old=0, local_name='Sao Tome e PrIncipe', government_form='Republic', head_of_state='Miguel Trovoada', capital=3172, code2='ST'),
    Country(code='SWZ', name='Swaziland', continent='Africa', region='Southern Africa', surface_area=17364, independence_year=1968, population=1008000,
           life_expectancy=40.4, gnp=1206, gnp_old=1312, local_name='kaNgwane', government_form='Monarchy', head_of_state='Mswati III', capital=3244, code2='SZ'),
    Country(code='SYC', name='Seychelles', continent='Africa', region='Eastern Africa', surface_area=455, independence_year=1976, population=77000, life_expectancy=70.4,
           gnp=536, gnp_old=539, local_name='Sesel/Seychelles', government_form='Republic', head_of_state='France-Albert Rene', capital=3206, code2='SC'),
    Country(code='TCD', name='Chad', continent='Africa', region='Central Africa', surface_area=1284000, independence_year=1960, population=7651000,
           life_expectancy=50.5, gnp=1208, gnp_old=1102, local_name='Tchad/Tshad', government_form='Republic', head_of_state='Idriss Deby', capital=3337, code2='TD'),
    Country(code='TGO', name='Togo', continent='Africa', region='Western Africa', surface_area=56785, independence_year=1960, population=4629000,
           life_expectancy=54.7, gnp=1449, gnp_old=1400, local_name='Togo', government_form='Republic', head_of_state='Gnassingbe Eyadema', capital=3332, code2='TG'),
    Country(code='TuN', name='Tunisia', continent='Africa', region='Northern Africa', surface_area=163610, independence_year=1956, population=9586000, life_expectancy=73.7,
           gnp=20026, gnp_old=18898, local_name='Tunis/Tunisie', government_form='Republic', head_of_state='Zine al-Abidine Ben Ali', capital=3349, code2='TN'),
    Country(code='TZA', name='Tanzania', continent='Africa', region='Eastern Africa', surface_area=883749, independence_year=1961, population=33517000,
           life_expectancy=52.3, gnp=8005, gnp_old=7388, local_name='Tanzania', government_form='Republic', head_of_state='Benjamin William Mkapa', capital=3306, code2='TZ'),
    Country(code='uGA', name='uganda', continent='Africa', region='Eastern Africa', surface_area=241038, independence_year=1962, population=21778000,
           life_expectancy=42.9, gnp=6313, gnp_old=6887, local_name='uganda', government_form='Republic', head_of_state='Yoweri Museveni', capital=3425, code2='uG'),
    Country(code='ZAF', name='South Africa', continent='Africa', region='Southern Africa', surface_area=1221037, independence_year=1910, population=40377000,
           life_expectancy=51.1, gnp=116729, gnp_old=129092, local_name='South Africa', government_form='Republic', head_of_state='Thabo Mbeki', capital=716, code2='ZA'),
    Country(code='ZMB', name='Zambia', continent='Africa', region='Eastern Africa', surface_area=752618, independence_year=1964, population=9169000,
           life_expectancy=37.2, gnp=3377, gnp_old=3922, local_name='Zambia', government_form='Republic', head_of_state='Frederick Chiluba', capital=3162, code2='ZM'),
    Country(code='ZWE', name='Zimbabwe', continent='Africa', region='Eastern Africa', surface_area=390757, independence_year=1980, population=11669000,
           life_expectancy=37.8, gnp=5951, gnp_old=8670, local_name='Zimbabwe', government_form='Republic', head_of_state='Robert G. Mugabe', capital=4068, code2='ZW'),
]

# CREACION DE GET METHOD


@router.get("/Africa/", status_code=200)
async def country():
    return (countries_list)


@router.get("/Africa/{ID}")
async def country(ID: str):
    country = filter(lambda Country: Country.code == ID,
                     countries_list)  # Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code=404, detail="PAIS NO EXISTENTE")

# CREACION DE POST METHOD


@router.post("/Africa/", status_code=201)
async def country(country: Country):
    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == country.code or saved_user.code == country.code2:
            raise HTTPException(status_code=409, detail="PAIS YA REGISTRADO")
    else:
        countries_list.append(country)
        return country
# http://127.0.0.1:8000/country/

# CREACION DE PUT METHOD


@router.put("/Africa/", status_code=200)
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


@router.delete("/Africa/{id}", status_code=200)
async def country(id: str):

    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == id or saved_user.code2 == id:
            del countries_list[index]
            found = True
            return "PAIS ELIMINADO"

    if not found:
        raise HTTPException(status_code=401, detail="PAIS NO ENCONTRADO")
