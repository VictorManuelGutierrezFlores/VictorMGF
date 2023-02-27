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
    Country(code='AFG', name='Afghanistan', continent='Asia', region='Southern and Central Asia', surface_area=652090, independence_year=1919, population=22720000,
         life_expectancy=45.9, gnp=5976, gnp_old=0, local_name='Afganistan/Afqanestan', government_form='Islamic Emirate', head_of_state='Mohammad Omar', capital=1, code2='AF'),

    Country(code='ARE', name='united Arab Emirates', continent='Asia', region='Middle East', surface_area=83600, independence_year=1971, population=2441000, life_expectancy=74.1,
         gnp=37966, gnp_old=36846, local_name='Al-Imarat al- Arabiya al-Muttahida', government_form='Emirate Federation', head_of_state='Zayid bin Sultan al-Nahayan', capital=65, code2='AE'),
    Country(code='ARM', name='Armenia', continent='Asia', region='Middle East', surface_area=29800, independence_year=1991, population=3520000,
         life_expectancy=66.4, gnp=1813, gnp_old=1627, local_name='Hajastan', government_form='Republic', head_of_state='Robert KotSarjan', capital=126, code2='AM'),
    Country(code='AZE', name='Azerbaijan', continent='Asia', region='Middle East', surface_area=86600, independence_year=1991, population=7734000, life_expectancy=62.9,
         gnp=4127, gnp_old=4100, local_name='Azarbaycan', government_form='Federal Republic', head_of_state='Heydar aliyev', capital=144, code2='AZ'),
    Country(code='BGD', name='Bangladesh', continent='Asia', region='Southern and Central Asia', surface_area=143998, independence_year=1971, population=129155000,
         life_expectancy=60.2, gnp=32852, gnp_old=31966, local_name='Bangladesh', government_form='Republic', head_of_state='Shahabuddin Ahmad', capital=150, code2='BD'),
    Country(code='BHR', name='Bahrain', continent='Asia', region='Middle East', surface_area=694, independence_year=1971, population=617000, life_expectancy=73,
         gnp=6366, gnp_old=6097, local_name='Al-Bahrayn', government_form='Monarchy (Emirate)', head_of_state='Hamad ibn Isa al-Khalifa', capital=149, code2='BH'),
    Country(code='BRN', name='Brunei', continent='Asia', region='Southeast Asia', surface_area=5765, independence_year=1984, population=328000, life_expectancy=73.6,
         gnp=11705, gnp_old=12460, local_name='Brunei Darussalam', government_form='Monarchy (Sultanate)', head_of_state='Haji Hassan al-Bolkiah', capital=538, code2='BN'),
    Country(code='BTN', name='Bhutan', continent='Asia', region='Southern and Central Asia', surface_area=47000, independence_year=1910, population=2124000,
         life_expectancy=52.4, gnp=372, gnp_old=383, local_name='Druk-Yul', government_form='Monarchy', head_of_state='Jigme Singye Wangchuk', capital=192, code2='BT'),
    Country(code='CHN', name='China', continent='Asia', region='Eastern Asia', surface_area=9572900, independence_year=-1523, population=1277558000, life_expectancy=71.4,
         gnp=982268, gnp_old=917719, local_name='Zhongquo', government_form="People'sRepublic", head_of_state='Jiang Zemin', capital=1891, code2='CN'),
    Country(code='CYP', name='Cyprus', continent='Asia', region='Middle East', surface_area=9251, independence_year=1960, population=754700, life_expectancy=76.7,
         gnp=9333, gnp_old=8246, local_name='Kypros/Kibris', government_form='Republic', head_of_state='Glafkos Klerides', capital=2430, code2='CY'),
    Country(code='GEO', name='Georgia', continent='Asia', region='Middle East', surface_area=69700, independence_year=1991, population=4968000, life_expectancy=64.5,
         gnp=6064, gnp_old=5924, local_name='Sakartvelo', government_form='Republic', head_of_state='Eduard Sevardnadze', capital=905, code2='GE'),
    Country(code='HKG', name='Hong Kong', continent='Asia', region='Eastern Asia', surface_area=1075, independence_year=0, population=6782000, life_expectancy=79.5, gnp=166448,
         gnp_old=173610, local_name='Xianggang/Hong Kong', government_form='Special Administrative Region of China', head_of_state='Jiang Zemin', capital=937, code2='HK'),
    Country(code='IDN', name='Indonesia', continent='Asia', region='Southeast Asia', surface_area=1904569, independence_year=1945, population=212107000,
         life_expectancy=68, gnp=84982, gnp_old=215002, local_name='Indonesia', government_form='Republic', head_of_state='Abdurrahman Wahid', capital=939, code2='ID'),
    Country(code='IND', name='India', continent='Asia', region='Southern and Central Asia', surface_area=3287263, independence_year=1947, population=1013662000, life_expectancy=62.5,
         gnp=447114, gnp_old=430572, local_name='Bharat/India', government_form='Federal Republic', head_of_state='Kocheril Raman Narayanan', capital=1109, code2='IN'),
    Country(code='IRN', name='Iran', continent='Asia', region='Southern and Central Asia', surface_area=1648195, independence_year=1906, population=67702000, life_expectancy=69.7,
         gnp=195746, gnp_old=160151, local_name='Iran', government_form='Islamic Republic', head_of_state='Ali Mohammad Khatami-Ardakani', capital=1380, code2='IR'),
    Country(code='IRQ', name='Iraq', continent='Asia', region='Middle East', surface_area=438317, independence_year=1932, population=23115000, life_expectancy=66.5,
         gnp=11500, gnp_old=0, local_name='Al- Iraq', government_form='Republic', head_of_state='Saddam Hussein al-Takriti', capital=1365, code2='IQ'),
    Country(code='ISR', name='Israel', continent='Asia', region='Middle East', surface_area=21056, independence_year=1948, population=6217000, life_expectancy=78.6,
         gnp=97477, gnp_old=98577, local_name='Yisrael/Israil', government_form='Republic', head_of_state='Moshe Katzav', capital=1450, code2='IL'),
    Country(code='JOR', name='Jordan', continent='Asia', region='Middle East', surface_area=88946, independence_year=1946, population=5083000, life_expectancy=77.4,
         gnp=7526, gnp_old=7051, local_name='Al-urdunn', government_form='Constitutional Monarchy', head_of_state='Abdullah II', capital=1786, code2='JO'),
    Country(code='JPN', name='Japan', continent='Asia', region='Eastern Asia', surface_area=377829, independence_year=-660, population=126714000, life_expectancy=80.7,
         gnp=3787042, gnp_old=4192638, local_name='Nihon/Nippon', government_form='Constitutional Monarchy', head_of_state='Akihito', capital=1532, code2='JP'),
    Country(code='KAZ', name='Kazakstan', continent='Asia', region='Southern and Central Asia', surface_area=2724900, independence_year=1991, population=16223000,
         life_expectancy=63.2, gnp=24375, gnp_old=23383, local_name='Qazaqstan', government_form='Republic', head_of_state='Nursultan Nazarbajev', capital=1864, code2='KZ'),
    Country(code='KGZ', name='Kyrgyzstan', continent='Asia', region='Southern and Central Asia', surface_area=199900, independence_year=1991, population=4699000,
         life_expectancy=63.4, gnp=1626, gnp_old=1767, local_name='Kyrgyzstan', government_form='Republic', head_of_state='Askar Akajev', capital=2253, code2='KG'),
    Country(code='KHM', name='Cambodia', continent='Asia', region='Southeast Asia', surface_area=181035, independence_year=1953, population=11168000, life_expectancy=56.5,
         gnp=5121, gnp_old=5670, local_name='Kampuchea', government_form='Constitutional Monarchy', head_of_state='Norodom Sihanouk', capital=1800, code2='KH'),
    Country(code='KOR', name='South Korea', continent='Asia', region='Eastern Asia', surface_area=99434, independence_year=1948, population=46844000, life_expectancy=74.4,
         gnp=320749, gnp_old=442544, local_name='Taehan Minguk (Namhan)', government_form='Republic', head_of_state='Kim Dae-jung', capital=2331, code2='KR'),
    Country(code='KWT', name='Kuwait', continent='Asia', region='Middle East', surface_area=17818, independence_year=1961, population=1972000, life_expectancy=76.1, gnp=27037,
         gnp_old=30373, local_name='Al-Kuwayt', government_form='Constitutional Monarchy (Emirate)', head_of_state='Jabir al-Ahmad al-Jabir al-Sabah', capital=2429, code2='KW'),
    Country(code='LAO', name='Laos', continent='Asia', region='Southeast Asia', surface_area=236800, independence_year=1953, population=5433000,
         life_expectancy=53.1, gnp=1292, gnp_old=1746, local_name='Lao', government_form='Republic', head_of_state='Khamtay Siphandone', capital=2432, code2='LA'),
    Country(code='LBN', name='Lebanon', continent='Asia', region='Middle East', surface_area=10400, independence_year=1941, population=3282000,
         life_expectancy=71.3, gnp=17121, gnp_old=15129, local_name='Lubnan', government_form='Republic', head_of_state='emile Lahoud', capital=2438, code2='LB'),
    Country(code='LKA', name='Sri Lanka', continent='Asia', region='Southern and Central Asia', surface_area=65610, independence_year=1948, population=18827000,
         life_expectancy=71.8, gnp=15706, gnp_old=15091, local_name='Sri Lanka/Ilankai', government_form='Republic', head_of_state='Chandrika Kumaratunga', capital=3217, code2='LK'),
    Country(code='MAC', name='Macao', continent='Asia', region='Eastern Asia', surface_area=18, independence_year=0, population=473000, life_expectancy=81.6, gnp=5749,
         gnp_old=5940, local_name='Macau/Aomen', government_form='Special Administrative Region of China', head_of_state='Jiang Zemin', capital=2454, code2='MO'),
    Country(code='MDV', name='Maldives', continent='Asia', region='Southern and Central Asia', surface_area=298, independence_year=1965, population=286000, life_expectancy=62.2,
         gnp=199, gnp_old=0, local_name='Dhivehi Raajje/Maldives', government_form='Republic', head_of_state='Maumoon Abdul Gayoom', capital=2463, code2='MV'),
    Country(code='MMR', name='Myanmar', continent='Asia', region='Southeast Asia', surface_area=676578, independence_year=1948, population=45611000, life_expectancy=54.9,
         gnp=180375, gnp_old=171028, local_name='Myanma Pye', government_form='Republic', head_of_state='kenraali Than Shwe', capital=2710, code2='MM'),
    Country(code='MNG', name='Mongolia', continent='Asia', region='Eastern Asia', surface_area=1566500, independence_year=1921, population=2662000, life_expectancy=67.3,
         gnp=1043, gnp_old=933, local_name='Mongol uls', government_form='Republic', head_of_state='Natsagiin Bagabandi', capital=2696, code2='MN'),
    Country(code='MYS', name='Malaysia', continent='Asia', region='Southeast Asia', surface_area=329758, independence_year=1957, population=22244000, life_expectancy=70.8, gnp=69213,
         gnp_old=97884, local_name='Malaysia', government_form='Constitutional Monarchy, Federation', head_of_state='Salahuddin Abdul Aziz Shah Alhaj', capital=2464, code2='MY'),
    Country(code='NPL', name='Nepal', continent='Asia', region='Southern and Central Asia', surface_area=147181, independence_year=1769, population=23930000, life_expectancy=57.8,
         gnp=4768, gnp_old=4837, local_name='Nepal', government_form='Constitutional Monarchy', head_of_state='Gyanendra Bir Bikram', capital=2729, code2='NP'),
    Country(code='OMN', name='Oman', continent='Asia', region='Middle East', surface_area=309500, independence_year=1951, population=2542000, life_expectancy=71.8,
         gnp=16904, gnp_old=16153, local_name='uman', government_form='Monarchy (Sultanate)', head_of_state='Qabus ibn Sa id', capital=2821, code2='OM'),
    Country(code='PAK', name='Pakistan', continent='Asia', region='Southern and Central Asia', surface_area=796095, independence_year=1947, population=156483000,
         life_expectancy=61.1, gnp=61289, gnp_old=58549, local_name='Pakistan', government_form='Republic', head_of_state='Mohammad Rafiq Tarar', capital=2831, code2='PK'),
    Country(code='PHL', name='Philippines', continent='Asia', region='Southeast Asia', surface_area=300000, independence_year=1946, population=75967000, life_expectancy=67.5,
         gnp=65107, gnp_old=82239, local_name='Pilipinas', government_form='Republic', head_of_state='Gloria Macapagal-Arroyo', capital=766, code2='PH'),
    Country(code='PRK', name='North Korea', continent='Asia', region='Eastern Asia', surface_area=120538, independence_year=1948, population=24039000, life_expectancy=70.7, gnp=5332,
         gnp_old=0, local_name='Choson Minjujuui In min Konghwaguk (Bukhan)', government_form='Socialistic Republic', head_of_state='Kim Jong-il', capital=2318, code2='KP'),
    Country(code='PSE', name='Palestine', continent='Asia', region='Middle East', surface_area=6257, independence_year=0, population=3101000, life_expectancy=71.4,
         gnp=4173, gnp_old=0, local_name='Filastin', government_form='Autonomous Area', head_of_state='Yasser (Yasir) Arafat', capital=4074, code2='PS'),
    Country(code='QAT', name='Qatar', continent='Asia', region='Middle East', surface_area=11000, independence_year=1971, population=599000, life_expectancy=72.4,
         gnp=9472, gnp_old=8920, local_name='Qatar', government_form='Monarchy', head_of_state='Hamad ibn Khalifa al-Thani', capital=2973, code2='QA'),
    Country(code='SAu', name='Saudi Arabia', continent='Asia', region='Middle East', surface_area=2149690, independence_year=1932, population=21607000, life_expectancy=67.8,
         gnp=137635, gnp_old=146171, local_name='Al- Arabiya as-Sa udiya', government_form='Monarchy', head_of_state='Fahd ibn Abdul-Aziz al-Sa ud', capital=3173, code2='SA'),
    Country(code='SGP', name='Singapore', continent='Asia', region='Southeast Asia', surface_area=618, independence_year=1965, population=3567000, life_expectancy=80.1,
         gnp=86503, gnp_old=96318, local_name='Singapore/Singapura/Xinjiapo/Singapur', government_form='Republic', head_of_state='Sellapan Rama Nathan', capital=3208, code2='SG'),
    Country(code='SYR', name='Syria', continent='Asia', region='Middle East', surface_area=185180, independence_year=1941, population=16125000,
         life_expectancy=68.5, gnp=65984, gnp_old=64926, local_name='Suriya', government_form='Republic', head_of_state='Bashar al-Assad', capital=3250, code2='SY'),
    Country(code='THA', name='Thailand', continent='Asia', region='Southeast Asia', surface_area=513115, independence_year=1350, population=61399000, life_expectancy=68.6,
         gnp=116416, gnp_old=153907, local_name='Prathet Thai', government_form='Constitutional Monarchy', head_of_state='Bhumibol Adulyadej', capital=3320, code2='TH'),
    Country(code='TJK', name='Tajikistan', continent='Asia', region='Southern and Central Asia', surface_area=143100, independence_year=1991, population=6188000,
         life_expectancy=64.1, gnp=1990, gnp_old=1056, local_name='Tocikiston', government_form='Republic', head_of_state='Emomali Rahmonov', capital=3261, code2='TJ'),
    Country(code='TKM', name='Turkmenistan', continent='Asia', region='Southern and Central Asia', surface_area=488100, independence_year=1991, population=4459000,
         life_expectancy=60.9, gnp=4397, gnp_old=2000, local_name='Turkmenostan', government_form='Republic', head_of_state='Saparmurad Nijazov', capital=3419, code2='TM'),
    Country(code='TMP', name='East Timor', continent='Asia', region='Southeast Asia', surface_area=14874, independence_year=0, population=885000, life_expectancy=46,
         gnp=0, gnp_old=0, local_name='Timor Timur', government_form='Administrated by the uN', head_of_state='Jose Alexandre Gusmao', capital=1522, code2='TP'),
    Country(code='TuR', name='Turkey', continent='Asia', region='Middle East', surface_area=774815, independence_year=1923, population=66591000, life_expectancy=71,
         gnp=210721, gnp_old=189122, local_name='Turkiye', government_form='Republic', head_of_state='Ahmet Necdet Sezer', capital=3358, code2='TR'),
    Country(code='TWN', name='Taiwan', continent='Asia', region='Eastern Asia', surface_area=36188, independence_year=1945, population=22256000, life_expectancy=76.4,
         gnp=256254, gnp_old=263451, local_name='Tai-wan', government_form='Republic', head_of_state='Chen Shui-bian', capital=3263, code2='TW'),
    Country(code='uZB', name='uzbekistan', continent='Asia', region='Southern and Central Asia', surface_area=447400, independence_year=1991, population=24318000,
         life_expectancy=63.7, gnp=14194, gnp_old=21300, local_name='uzbekiston', government_form='Republic', head_of_state='Islam Karimov', capital=3503, code2='uZ'),
    Country(code='VNM', name='Vietnam', continent='Asia', region='Southeast Asia', surface_area=331689, independence_year=1945, population=79832000, life_expectancy=69.3,
         gnp=21929, gnp_old=22834, local_name='Viet Nam', government_form='Socialistic Republic', head_of_state='Tran Duc Luong', capital=3770, code2='VN'),
    Country(code='YEM', name='Yemen', continent='Asia', region='Middle East', surface_area=527968, independence_year=1918, population=18112000, life_expectancy=59.8,
         gnp=6041, gnp_old=5729, local_name='Al-Yaman', government_form='Republic', head_of_state='Ali Abdallah Salih', capital=1780, code2='YE'),

]
# CREACION DE GET METHOD


@router.get("/Asia/", status_code=200)
async def country():
    return (countries_list)


@router.get("/Asia/{ID}")
async def country(ID: str):
    country = filter(lambda Country: Country.code == ID,
                     countries_list)  # Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code=404, detail="PAIS NO EXISTENTE")

# CREACION DE POST METHOD


@router.post("/Asia/", status_code=201)
async def country(country: Country):
    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == country.code or saved_user.code == country.code2:
            raise HTTPException(status_code=409, detail="PAIS YA REGISTRADO")
    else:
        countries_list.append(country)
        return country
# http://127.0.0.1:8000/Asia/

# CREACION DE PUT METHOD


@router.put("/Asia/", status_code=200)
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


@router.delete("/Asia/{id}", status_code=200)
async def country(id: str):

    found = False

    for index, saved_user in enumerate(countries_list):
        if saved_user.code == id or saved_user.code2 == id:
            del countries_list[index]
            found = True
            return "PAIS ELIMINADO"

    if not found:
        raise HTTPException(status_code=401, detail="PAIS NO ENCONTRADO")
