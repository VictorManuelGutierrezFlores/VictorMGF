#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI, HTTPException
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
from fastapi import APIRouter


#Creamos un objeto a partir de la clase FastAPI
router = APIRouter()

class Country(BaseModel):
    code:str
    name:str
    continent:str
    region:str
    surface_area:int
    independence_year:int
    population:int
    life_expectancy:float
    gnp:int
    gnp_old:int
    local_name:str
    government_form:str
    head_of_state:str
    capital:int
    code2:str

## http://127.0.0.1:8000/antarctica/
## http://127.0.0.1:8000/Caribbean/
## http://127.0.0.1:8000/Australia and New Zealand/
## http://127.0.0.1:8000/Baltic Countries/ 
## http://127.0.0.1:8000/British Islands/
## http://127.0.0.1:8000/Central Africa/
## http://127.0.0.1:8000/Central America/
## http://127.0.0.1:8000/Southern Europe/
## http://127.0.0.1:8000/Eastern Africa/
## http://127.0.0.1:8000/Southern and Central Asia/
## http://127.0.0.1:8000/Middle East/
## http://127.0.0.1:8000/South America/
## http://127.0.0.1:8000/Polynesia/
## http://127.0.0.1:8000/Western Europe/
## http://127.0.0.1:8000/Western Africa/
## http://127.0.0.1:8000/North America/
## http://127.0.0.1:8000/Eastern Europe/
## http://127.0.0.1:8000/Southeast Asia/
## http://127.0.0.1:8000/Southern Africa/
## http://127.0.0.1:8000/Eastern Asia/
## http://127.0.0.1:8000/Melanesia/
## http://127.0.0.1:8000/Micronesia/
## http://127.0.0.1:8000/Nordic Countries/
## http://127.0.0.1:8000/Micronesia/Caribbean/


#LISTA DE PAISES CONTENIDOS EN LA REGION, INSTANCIADO CON BASEMODEL
#Country(code="", name="", code2=""),
contries_list = [
Country(code='HMD',name='Heard Island and McDonald Islands',continent='Antarctica',region='Antarctica',surface_area=359,independence_year=0,population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name='Heard and McDonald Islands',government_form='Territory of Australia',head_of_state='Elisabeth II',capital=0,code2='HM'), 
Country(code='SGS',name='South Georgia and the South Sandwich Islands',continent='Antarctica',region='Antarctica',surface_area=3903,independence_year=0,population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name='South Georgia and the South Sandwich Islands',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=0,code2='GS'), 
Country(code='ATA',name='Antarctica',continent='Antarctica',region='Antarctica',surface_area=13120000,independence_year=0,population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name='N/A',government_form='Co-administrated',head_of_state='',capital=0,code2='AQ'), 
Country(code='ATF',name='French Southern territories',continent='Antarctica',region='Antarctica',surface_area=7780,independence_year=0,population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name='Terres australes francaises',government_form='Nonmetropolitan Territory of France',head_of_state='Jacques Chirac',capital=0,code2='TF'),
Country(code='BVT',name='Bouvet Island',continent='Antarctica',region='Antarctica',surface_area=59,independence_year=0,population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name='Bouvetoya',government_form='Dependent Territory of Norway',head_of_state='Harald V',capital=0,code2='BV'), 
]
contries_list1 = [
Country(code='ABW',name='Aruba',continent='North America',region='Caribbean',surface_area=193,independence_year=0,population=103000,life_expectancy=78.4,gnp=828,gnp_old=793,local_name='Aruba',government_form='Nonmetropolitan Territory of The Netherlands',head_of_state='Willem-Alexander',capital=129,code2='AW'), 
Country(code='AIA',name='Anguilla',continent='North America',region='Caribbean',surface_area=96,independence_year=0,population=8000,life_expectancy=76.1,gnp=63.2,gnp_old=0,local_name='Anguilla',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=62,code2='AI'), 
Country(code='ANT',name='Netherlands Antilles',continent='North America',region='Caribbean',surface_area=800,independence_year=0,population=217000,life_expectancy=74.7,gnp=1941,gnp_old=0,local_name='Nederlandse Antillen',government_form='Nonmetropolitan Territory of The Netherlands',head_of_state='Willem-Alexander',capital=33,code2='AN'), 
Country(code='ATG',name='Antigua and Barbuda',continent='North America',region='Caribbean',surface_area=442,independence_year=1981,population=68000,life_expectancy=70.5,gnp=612,gnp_old=584,local_name='Antigua and Barbuda',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=63,code2='AG'), 
Country(code='BHS',name='Bahamas',continent='North America',region='Caribbean',surface_area=13878,independence_year=1973,population=307000,life_expectancy=71.1,gnp=3527,gnp_old=3347,local_name='The Bahamas',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=148,code2='BS'), 
Country(code='BRB',name='Barbados',continent='North America',region='Caribbean',surface_area=430,independence_year=1966,population=270000,life_expectancy=73,gnp=2223,gnp_old=2186,local_name='Barbados',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=174,code2='BB'), 
Country(code='CuB',name='Cuba',continent='North America',region='Caribbean',surface_area=110861,independence_year=1902,population=11201000,life_expectancy=76.2,gnp=17843,gnp_old=18862,local_name='Cuba',government_form='Socialistic Republic',head_of_state='Fidel Castro Ruz',capital=2413,code2='Cu'), 
Country(code='CYM',name='Cayman Islands',continent='North America',region='Caribbean',surface_area=264,independence_year=0,population=38000,life_expectancy=78.9,gnp=1263,gnp_old=1186,local_name='Cayman Islands',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=553,code2='KY'), 
Country(code='DMA',name='Dominica',continent='North America',region='Caribbean',surface_area=751,independence_year=1978,population=71000,life_expectancy=73.4,gnp=256,gnp_old=243,local_name='Dominica',government_form='Republic',head_of_state='Vernon Shaw',capital=586,code2='DM'), 
Country(code='DOM',name='Dominican Republic',continent='North America',region='Caribbean',surface_area=48511,independence_year=1844,population=8495000,life_expectancy=73.2,gnp=15846,gnp_old=15076,local_name='Republica Dominicana',government_form='Republic',head_of_state='Hipolito MejIa DomInguez',capital=587,code2='DO'), 
Country(code='GLP',name='Guadeloupe',continent='North America',region='Caribbean',surface_area=1705,independence_year=0,population=456000,life_expectancy=77,gnp=3501,gnp_old=0,local_name='Guadeloupe',government_form='Overseas Department of France',head_of_state='Jacques Chirac',capital=919,code2='GP'), 
Country(code='GRD',name='Grenada',continent='North America',region='Caribbean',surface_area=344,independence_year=1974,population=94000,life_expectancy=64.5,gnp=318,gnp_old=0,local_name='Grenada',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=916,code2='GD'), 
Country(code='HTI',name='Haiti',continent='North America',region='Caribbean',surface_area=27750,independence_year=1804,population=8222000,life_expectancy=49.2,gnp=3459,gnp_old=3107,local_name='Haiti/Dayti',government_form='Republic',head_of_state='Jean-Bertrand Aristide',capital=929,code2='HT'), 
Country(code='JAM',name='Jamaica',continent='North America',region='Caribbean',surface_area=10990,independence_year=1962,population=2583000,life_expectancy=75.2,gnp=6871,gnp_old=6722,local_name='Jamaica',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=1530,code2='JM'), 
Country(code='KNA',name='Saint Kitts and Nevis',continent='North America',region='Caribbean',surface_area=261,independence_year=1983,population=38000,life_expectancy=70.7,gnp=299,gnp_old=0,local_name='Saint Kitts and Nevis',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=3064,code2='KN'), 
Country(code='LCA',name='Saint Lucia',continent='North America',region='Caribbean',surface_area=622,independence_year=1979,population=154000,life_expectancy=72.3,gnp=571,gnp_old=0,local_name='Saint Lucia',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=3065,code2='LC'), 
Country(code='MSR',name='Montserrat',continent='North America',region='Caribbean',surface_area=102,independence_year=0,population=11000,life_expectancy=78,gnp=109,gnp_old=0,local_name='Montserrat',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=2697,code2='MS'), 
Country(code='MTQ',name='Martinique',continent='North America',region='Caribbean',surface_area=1102,independence_year=0,population=395000,life_expectancy=78.3,gnp=2731,gnp_old=2559,local_name='Martinique',government_form='Overseas Department of France',head_of_state='Jacques Chirac',capital=2508,code2='MQ'), 
Country(code='PRI',name='Puerto Rico',continent='North America',region='Caribbean',surface_area=8875,independence_year=0,population=3869000,life_expectancy=75.6,gnp=34100,gnp_old=32100,local_name='Puerto Rico',government_form='Commonwealth of the uS',head_of_state='George W. Bush',capital=2919,code2='PR'), 
Country(code='TCA',name='Turks and Caicos Islands',continent='North America',region='Caribbean',surface_area=430,independence_year=0,population=17000,life_expectancy=73.3,gnp=96,gnp_old=0,local_name='The Turks and Caicos Islands',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=3423,code2='TC'), 
Country(code='TTO',name='Trinidad and Tobago',continent='North America',region='Caribbean',surface_area=5130,independence_year=1962,population=1295000,life_expectancy=68,gnp=6232,gnp_old=5867,local_name='Trinidad and Tobago',government_form='Republic',head_of_state='Arthur N. R. Robinson',capital=3336,code2='TT'), 
Country(code='VCT',name='Saint Vincent and the Grenadines',continent='North America',region='Caribbean',surface_area=388,independence_year=1979,population=114000,life_expectancy=72.3,gnp=285,gnp_old=0,local_name='Saint Vincent and the Grenadines',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=3066,code2='VC'), 
Country(code='VGB',name='Virgin Islands, British',continent='North America',region='Caribbean',surface_area=151,independence_year=0,population=21000,life_expectancy=75.4,gnp=612,gnp_old=573,local_name='British Virgin Islands',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=537,code2='VG'), 
Country(code='VIR',name='Virgin Islands, u.S.',continent='North America',region='Caribbean',surface_area=347,independence_year=0,population=93000,life_expectancy=78.1,gnp=0,gnp_old=0,local_name='Virgin Islands of the united States',government_form='uS Territory',head_of_state='George W. Bush',capital=4067,code2='VI'),
]
contries_list2 = [
Country(code='NZL',name='New Zealand',continent='Oceania',region='Australia and New Zealand',surface_area=270534,independence_year=1907,population=3862000,life_expectancy=77.8,gnp=54669,gnp_old=64960,local_name='New Zealand/Aotearoa',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=3499,code2='NZ'), 
Country(code='NFK',name='Norfolk Island',continent='Oceania',region='Australia and New Zealand',surface_area=36,independence_year=0,population=2000,life_expectancy=0,gnp=0,gnp_old=0,local_name='Norfolk Island',government_form='Territory of Australia',head_of_state='Elisabeth II',capital=2806,code2='NF'),     
Country(code='CCK',name='Cocos (Keeling) Islands',continent='Oceania',region='Australia and New Zealand',surface_area=14,independence_year=0,population=600,life_expectancy=0,gnp=0,gnp_old=0,local_name='Cocos (Keeling) Islands',government_form='Territory of Australia',head_of_state='Elisabeth II',capital=2317,code2='CC'), 
Country(code='AuS',name='Australia',continent='Oceania',region='Australia and New Zealand',surface_area=7741220,independence_year=1901,population=18886000,life_expectancy=79.8,gnp=351182,gnp_old=392911,local_name='Australia',government_form='Constitutional Monarchy, Federation',head_of_state='Elisabeth II',capital=135,code2='Au'), 
Country(code='CXR',name='Christmas Island',continent='Oceania',region='Australia and New Zealand',surface_area=135,independence_year=0,population=2500,life_expectancy=0,gnp=0,gnp_old=0,local_name='Christmas Island',government_form='Territory of Australia',head_of_state='Elisabeth II',capital=1791,code2='CX'), 
]
contries_list3 = [
Country(code='EST',name='Estonia',continent='Europe',region='Baltic Countries',surface_area=45227,independence_year=1991,population=1439200,life_expectancy=69.5,gnp=5328,gnp_old=3371,local_name='Eesti',government_form='Republic',head_of_state='Lennart Meri',capital=3791,code2='EE'), 
Country(code='LTu',name='Lithuania',continent='Europe',region='Baltic Countries',surface_area=65301,independence_year=1991,population=3698500,life_expectancy=69.1,gnp=10692,gnp_old=9585,local_name='Lietuva',government_form='Republic',head_of_state='Valdas Adamkus',capital=2447,code2='LT'), 
Country(code='LVA',name='Latvia',continent='Europe',region='Baltic Countries',surface_area=64589,independence_year=1991,population=2424200,life_expectancy=68.4,gnp=6398,gnp_old=5639,local_name='Latvija',government_form='Republic',head_of_state='Vaira Vike-Freiberga',capital=2434,code2='LV'), 
]
contries_list4 = [
Country(code='GBR',name='united Kingdom',continent='Europe',region='British Islands',surface_area=242900,independence_year=1066,population=59623400,life_expectancy=77.7,gnp=1378330,gnp_old=1296830,local_name='united Kingdom',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=456,code2='GB'), 
Country(code='IRL',name='Ireland',continent='Europe',region='British Islands',surface_area=70273,independence_year=1921,population=3775100,life_expectancy=76.8,gnp=75921,gnp_old=73132,local_name='Ireland/eire',government_form='Republic',head_of_state='Mary McAleese',capital=1447,code2='IE'), 
]
contries_list5 = [
Country(code='STP',name='Sao Tome and Principe',continent='Africa',region='Central Africa',surface_area=964,independence_year=1975,population=147000,life_expectancy=65.3,gnp=6,gnp_old=0,local_name='Sao Tome e PrIncipe',government_form='Republic',head_of_state='Miguel Trovoada',capital=3172,code2='ST'), 
Country(code='TCD',name='Chad',continent='Africa',region='Central Africa',surface_area=1284000,independence_year=1960,population=7651000,life_expectancy=50.5,gnp=1208,gnp_old=1102,local_name='Tchad/Tshad',government_form='Republic',head_of_state='Idriss Deby',capital=3337,code2='TD'), 
Country(code='AGO',name='Angola',continent='Africa',region='Central Africa',surface_area=1246700,independence_year=1975,population=12878000,life_expectancy=38.3,gnp=6648,gnp_old=7984,local_name='Angola',government_form='Republic',head_of_state='Jose Eduardo dos Santos',capital=56,code2='AO'), 
Country(code='CAF',name='Central African Republic',continent='Africa',region='Central Africa',surface_area=622984,independence_year=1960,population=3615000,life_expectancy=44,gnp=1054,gnp_old=993,local_name='Centrafrique/Be-Afrika',government_form='Republic',head_of_state='Ange-Felix Patasse',capital=1889,code2='CF'), 
Country(code='CMR',name='Cameroon',continent='Africa',region='Central Africa',surface_area=475442,independence_year=1960,population=15085000,life_expectancy=54.8,gnp=9174,gnp_old=8596,local_name='Cameroun/Cameroon',government_form='Republic',head_of_state='Paul Biya',capital=1804,code2='CM'), 
Country(code='COD',name='Congo, The Democratic Republic of the',continent='Africa',region='Central Africa',surface_area=2344858,independence_year=1960,population=51654000,life_expectancy=48.8,gnp=6964,gnp_old=2474,local_name='Republique Democratique du Congo',government_form='Republic',head_of_state='Joseph Kabila',capital=2298,code2='CD'), 
Country(code='COG',name='Congo',continent='Africa',region='Central Africa',surface_area=342000,independence_year=1960,population=2943000,life_expectancy=47.4,gnp=2108,gnp_old=2287,local_name='Congo',government_form='Republic',head_of_state='Denis Sassou-Nguesso',capital=2296,code2='CG'), 
Country(code='GAB',name='Gabon',continent='Africa',region='Central Africa',surface_area=267668,independence_year=1960,population=1226000,life_expectancy=50.1,gnp=5493,gnp_old=5279,local_name='Le Gabon',government_form='Republic',head_of_state='Omar Bongo',capital=902,code2='GA'), 
Country(code='GNQ',name='Equatorial Guinea',continent='Africa',region='Central Africa',surface_area=28051,independence_year=1968,population=453000,life_expectancy=53.6,gnp=283,gnp_old=542,local_name='Guinea Ecuatorial',government_form='Republic',head_of_state='Teodoro Obiang Nguema Mbasogo',capital=2972,code2='GQ'), 
Country(code='TCD',name='Chad',continent='Africa',region='Central Africa',surface_area=1284000,independence_year=1960,population=7651000,life_expectancy=50.5,gnp=1208,gnp_old=1102,local_name='Tchad/Tshad',government_form='Republic',head_of_state='Idriss Deby',capital=3337,code2='TD'), 
]
contries_list6 = [
Country(code='BLZ',name='Belize',continent='North America',region='Central America',surface_area=22696,independence_year=1981,population=241000,life_expectancy=70.9,gnp=630,gnp_old=616,local_name='Belize',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=185,code2='BZ'), 
Country(code='CRI',name='Costa Rica',continent='North America',region='Central America',surface_area=51100,independence_year=1821,population=4023000,life_expectancy=75.8,gnp=10226,gnp_old=9757,local_name='Costa Rica',government_form='Republic',head_of_state='Miguel angel RodrIguez EcheverrIa',capital=584,code2='CR'), 
Country(code='GTM',name='Guatemala',continent='North America',region='Central America',surface_area=108889,independence_year=1821,population=11385000,life_expectancy=66.2,gnp=19008,gnp_old=17797,local_name='Guatemala',government_form='Republic',head_of_state='Alfonso Portillo Cabrera',capital=922,code2='GT'), 
Country(code='HND',name='Honduras',continent='North America',region='Central America',surface_area=112088,independence_year=1838,population=6485000,life_expectancy=69.9,gnp=5333,gnp_old=4697,local_name='Honduras',government_form='Republic',head_of_state='Carlos Roberto Flores Facusse',capital=933,code2='HN'), 
Country(code='MEX',name='Mexico',continent='North America',region='Central America',surface_area=1958201,independence_year=1810,population=98881000,life_expectancy=71.5,gnp=414972,gnp_old=401461,local_name='Mexico',government_form='Federal Republic',head_of_state='Vicente Fox Quesada',capital=2515,code2='MX'), 
Country(code='NIC',name='Nicaragua',continent='North America',region='Central America',surface_area=130000,independence_year=1838,population=5074000,life_expectancy=68.7,gnp=1988,gnp_old=2023,local_name='Nicaragua',government_form='Republic',head_of_state='Arnoldo Aleman Lacayo',capital=2734,code2='NI'), 
Country(code='PAN',name='Panama',continent='North America',region='Central America',surface_area=75517,independence_year=1903,population=2856000,life_expectancy=75.5,gnp=9131,gnp_old=8700,local_name='Panama',government_form='Republic',head_of_state='Mireya Elisa Moscoso RodrIguez',capital=2882,code2='PA'), 
Country(code='SLV',name='El Salvador',continent='North America',region='Central America',surface_area=21041,independence_year=1841,population=6276000,life_expectancy=69.7,gnp=11863,gnp_old=11203,local_name='El Salvador',government_form='Republic',head_of_state='Francisco Guillermo Flores Perez',capital=645,code2='SV'), 
]
contries_list7 = [
Country(code='PRT',name='Portugal',continent='Europe',region='Southern Europe',surface_area=91982,independence_year=1143,population=9997600,life_expectancy=75.8,gnp=105954,gnp_old=102133,local_name='Portugal',government_form='Republic',head_of_state='Jorge Sampaio',capital=2914,code2='PT'), 
Country(code='SMR',name='San Marino',continent='Europe',region='Southern Europe',surface_area=61,independence_year=885,population=27000,life_expectancy=81.1,gnp=510,gnp_old=0,local_name='San Marino',government_form='Republic',head_of_state='0',capital=3171,code2='SM'), 
Country(code='SVN',name='Slovenia',continent='Europe',region='Southern Europe',surface_area=20256,independence_year=1991,population=1987800,life_expectancy=74.9,gnp=19756,gnp_old=18202,local_name='Slovenija',government_form='Republic',head_of_state='Milan Kucan',capital=3212,code2='SI'), 
Country(code='VAT',name='Holy See (Vatican City State)',continent='Europe',region='Southern Europe',surface_area=0.4,independence_year=1929,population=1000,life_expectancy=0,gnp=9,gnp_old=0,local_name='Santa Sede/Citta del Vaticano',government_form='Independent Church State',head_of_state='Johannes Paavali II',capital=3538,code2='VA'), 
Country(code='YuG',name='Yugoslavia',continent='Europe',region='Southern Europe',surface_area=102173,independence_year=1918,population=10640000,life_expectancy=72.4,gnp=17000,gnp_old=0,local_name='Jugoslavija',government_form='Federal Republic',head_of_state='Vojislav KoStunica',capital=1792,code2='Yu'), 
Country(code='ALB',name='Albania',continent='Europe',region='Southern Europe',surface_area=28748,independence_year=1912,population=3401200,life_expectancy=71.6,gnp=3205,gnp_old=2500,local_name='Shqiperia',government_form='Republic',head_of_state='Rexhep Mejdani',capital=34,code2='AL'), 
Country(code='AND',name='Andorra',continent='Europe',region='Southern Europe',surface_area=468,independence_year=1278,population=78000,life_expectancy=83.5,gnp=1630,gnp_old=0,local_name='Andorra',government_form='Parliamentary Coprincipality',head_of_state='',capital=55,code2='AD'), 
Country(code='BIH',name='Bosnia and Herzegovina',continent='Europe',region='Southern Europe',surface_area=51197,independence_year=1992,population=3972000,life_expectancy=71.5,gnp=2841,gnp_old=0,local_name='Bosna i Hercegovina',government_form='Federal Republic',head_of_state='Ante Jelavic',capital=201,code2='BA'), 
Country(code='ESP',name='Spain',continent='Europe',region='Southern Europe',surface_area=505992,independence_year=1492,population=39441700,life_expectancy=78.8,gnp=553233,gnp_old=532031,local_name='Espana',government_form='Constitutional Monarchy',head_of_state='Juan Carlos I',capital=653,code2='ES'), 
Country(code='GIB',name='Gibraltar',continent='Europe',region='Southern Europe',surface_area=6,independence_year=0,population=25000,life_expectancy=79,gnp=258,gnp_old=0,local_name='Gibraltar',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=915,code2='GI'), 
Country(code='GRC',name='Greece',continent='Europe',region='Southern Europe',surface_area=131626,independence_year=1830,population=10545700,life_expectancy=78.4,gnp=120724,gnp_old=119946,local_name='Ellada',government_form='Republic',head_of_state='Kostis Stefanopoulos',capital=2401,code2='GR'), 
Country(code='HRV',name='Croatia',continent='Europe',region='Southern Europe',surface_area=56538,independence_year=1991,population=4473000,life_expectancy=73.7,gnp=20208,gnp_old=19300,local_name='Hrvatska',government_form='Republic',head_of_state='Stipe Mesic',capital=2409,code2='HR'), 
Country(code='ITA',name='Italy',continent='Europe',region='Southern Europe',surface_area=301316,independence_year=1861,population=57680000,life_expectancy=79,gnp=1161755,gnp_old=1145372,local_name='Italia',government_form='Republic',head_of_state='Carlo Azeglio Ciampi',capital=1464,code2='IT'), 
Country(code='MKD',name='Macedonia',continent='Europe',region='Southern Europe',surface_area=25713,independence_year=1991,population=2024000,life_expectancy=73.8,gnp=1694,gnp_old=1915,local_name='Makedonija',government_form='Republic',head_of_state='Boris Trajkovski',capital=2460,code2='MK'), 
Country(code='MLT',name='Malta',continent='Europe',region='Southern Europe',surface_area=316,independence_year=1964,population=380200,life_expectancy=77.9,gnp=3512,gnp_old=3338,local_name='Malta',government_form='Republic',head_of_state='Guido de Marco',capital=2484,code2='MT'), 
Country(code='YuG',name='Yugoslavia',continent='Europe',region='Southern Europe',surface_area=102173,independence_year=1918,population=10640000,life_expectancy=72.4,gnp=17000,gnp_old=0,local_name='Jugoslavija',government_form='Federal Republic',head_of_state='Vojislav KoStunica',capital=1792,code2='Yu'), 
]
contries_list8 = [
Country(code='BDI',name='Burundi',continent='Africa',region='Eastern Africa',surface_area=27834,independence_year=1962,population=6695000,life_expectancy=46.2,gnp=903,gnp_old=982,local_name='Burundi/uburundi',government_form='Republic',head_of_state='Pierre Buyoya',capital=552,code2='BI'), 
Country(code='COM',name='Comoros',continent='Africa',region='Eastern Africa',surface_area=1862,independence_year=1975,population=578000,life_expectancy=60,gnp=4401,gnp_old=4361,local_name='Komori/Comores',government_form='Republic',head_of_state='Azali Assoumani',capital=2295,code2='KM'), 
Country(code='DJI',name='Djibouti',continent='Africa',region='Eastern Africa',surface_area=23200,independence_year=1977,population=638000,life_expectancy=50.8,gnp=382,gnp_old=373,local_name='Djibouti/Jibuti',government_form='Republic',head_of_state='Ismail Omar Guelleh',capital=585,code2='DJ'), 
Country(code='ERI',name='Eritrea',continent='Africa',region='Eastern Africa',surface_area=117600,independence_year=1993,population=3850000,life_expectancy=55.8,gnp=650,gnp_old=755,local_name='Ertra',government_form='Republic',head_of_state='Isayas Afewerki [Isaias Afwerki]',capital=652,code2='ER'), 
Country(code='ETH',name='Ethiopia',continent='Africa',region='Eastern Africa',surface_area=1104300,independence_year=-1000,population=62565000,life_expectancy=45.2,gnp=6353,gnp_old=6180,local_name='YeItyop iya',government_form='Republic',head_of_state='Negasso Gidada',capital=756,code2='ET'), 
Country(code='IOT',name='British Indian Ocean Territory',continent='Africa',region='Eastern Africa',surface_area=78,independence_year=0,population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name='British Indian Ocean Territory',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=0,code2='IO'), 
Country(code='KEN',name='Kenya',continent='Africa',region='Eastern Africa',surface_area=580367,independence_year=1963,population=30080000,life_expectancy=48,gnp=9217,gnp_old=10241,local_name='Kenya',government_form='Republic',head_of_state='Daniel arap Moi',capital=1881,code2='KE'), 
Country(code='MDG',name='Madagascar',continent='Africa',region='Eastern Africa',surface_area=587041,independence_year=1960,population=15942000,life_expectancy=55,gnp=3750,gnp_old=3545,local_name='Madagasikara/Madagascar',government_form='Federal Republic',head_of_state='Didier Ratsiraka',capital=2455,code2='MG'), 
Country(code='MOZ',name='Mozambique',continent='Africa',region='Eastern Africa',surface_area=801590,independence_year=1975,population=19680000,life_expectancy=37.5,gnp=2891,gnp_old=2711,local_name='Mocambique',government_form='Republic',head_of_state='JoaquIm A. Chissano',capital=2698,code2='MZ'), 
Country(code='MuS',name='Mauritius',continent='Africa',region='Eastern Africa',surface_area=2040,independence_year=1968,population=1158000,life_expectancy=71,gnp=4251,gnp_old=4186,local_name='Mauritius',government_form='Republic',head_of_state='Cassam uteem',capital=2511,code2='Mu'), 
Country(code='MWI',name='Malawi',continent='Africa',region='Eastern Africa',surface_area=118484,independence_year=1964,population=10925000,life_expectancy=37.6,gnp=1687,gnp_old=2527,local_name='Malawi',government_form='Republic',head_of_state='Bakili Muluzi',capital=2462,code2='MW'), 
Country(code='MYT',name='Mayotte',continent='Africa',region='Eastern Africa',surface_area=373,independence_year=0,population=149000,life_expectancy=59.5,gnp=0,gnp_old=0,local_name='Mayotte',government_form='Territorial Collectivity of France',head_of_state='Jacques Chirac',capital=2514,code2='YT'), 
Country(code='REu',name='Reunion',continent='Africa',region='Eastern Africa',surface_area=2510,independence_year=0,population=699000,life_expectancy=72.7,gnp=8287,gnp_old=7988,local_name='Reunion',government_form='Overseas Department of France',head_of_state='Jacques Chirac',capital=3017,code2='RE'), 
Country(code='RWA',name='Rwanda',continent='Africa',region='Eastern Africa',surface_area=26338,independence_year=1962,population=7733000,life_expectancy=39.3,gnp=2036,gnp_old=1863,local_name='Rwanda/urwanda',government_form='Republic',head_of_state='Paul Kagame',capital=3047,code2='RW'), 
Country(code='SOM',name='Somalia',continent='Africa',region='Eastern Africa',surface_area=637657,independence_year=1960,population=10097000,life_expectancy=46.2,gnp=935,gnp_old=0,local_name='Soomaaliya',government_form='Republic',head_of_state='Abdiqassim Salad Hassan',capital=3214,code2='SO'), 
Country(code='SYC',name='Seychelles',continent='Africa',region='Eastern Africa',surface_area=455,independence_year=1976,population=77000,life_expectancy=70.4,gnp=536,gnp_old=539,local_name='Sesel/Seychelles',government_form='Republic',head_of_state='France-Albert Rene',capital=3206,code2='SC'), 
Country(code='TZA',name='Tanzania',continent='Africa',region='Eastern Africa',surface_area=883749,independence_year=1961,population=33517000,life_expectancy=52.3,gnp=8005,gnp_old=7388,local_name='Tanzania',government_form='Republic',head_of_state='Benjamin William Mkapa',capital=3306,code2='TZ'), 
Country(code='uGA',name='uganda',continent='Africa',region='Eastern Africa',surface_area=241038,independence_year=1962,population=21778000,life_expectancy=42.9,gnp=6313,gnp_old=6887,local_name='uganda',government_form='Republic',head_of_state='Yoweri Museveni',capital=3425,code2='uG'), 
Country(code='ZMB',name='Zambia',continent='Africa',region='Eastern Africa',surface_area=752618,independence_year=1964,population=9169000,life_expectancy=37.2,gnp=3377,gnp_old=3922,local_name='Zambia',government_form='Republic',head_of_state='Frederick Chiluba',capital=3162,code2='ZM'), 
Country(code='ZWE',name='Zimbabwe',continent='Africa',region='Eastern Africa',surface_area=390757,independence_year=1980,population=11669000,life_expectancy=37.8,gnp=5951,gnp_old=8670,local_name='Zimbabwe',government_form='Republic',head_of_state='Robert G. Mugabe',capital=4068,code2='ZW'),
Country(code='MYT',name='Mayotte',continent='Africa',region='Eastern Africa',surface_area=373,independence_year=0,population=149000,life_expectancy=59.5,gnp=0,gnp_old=0,local_name='Mayotte',government_form='Territorial Collectivity of France',head_of_state='Jacques Chirac',capital=2514,code2='YT'), 
]
contries_list9 = [
Country(code='AFG',name='Afghanistan',continent='Asia',region='Southern and Central Asia',surface_area=652090,independence_year=1919,population=22720000,life_expectancy=45.9,gnp=5976,gnp_old=0,local_name='Afganistan/Afqanestan',government_form='Islamic Emirate',head_of_state='Mohammad Omar',capital=1,code2='AF'), 
Country(code='BGD',name='Bangladesh',continent='Asia',region='Southern and Central Asia',surface_area=143998,independence_year=1971,population=129155000,life_expectancy=60.2,gnp=32852,gnp_old=31966,local_name='Bangladesh',government_form='Republic',head_of_state='Shahabuddin Ahmad',capital=150,code2='BD'), 
Country(code='BTN',name='Bhutan',continent='Asia',region='Southern and Central Asia',surface_area=47000,independence_year=1910,population=2124000,life_expectancy=52.4,gnp=372,gnp_old=383,local_name='Druk-Yul',government_form='Monarchy',head_of_state='Jigme Singye Wangchuk',capital=192,code2='BT'), 
Country(code='IND',name='India',continent='Asia',region='Southern and Central Asia',surface_area=3287263,independence_year=1947,population=1013662000,life_expectancy=62.5,gnp=447114,gnp_old=430572,local_name='Bharat/India',government_form='Federal Republic',head_of_state='Kocheril Raman Narayanan',capital=1109,code2='IN'), 
Country(code='IRN',name='Iran',continent='Asia',region='Southern and Central Asia',surface_area=1648195,independence_year=1906,population=67702000,life_expectancy=69.7,gnp=195746,gnp_old=160151,local_name='Iran',government_form='Islamic Republic',head_of_state='Ali Mohammad Khatami-Ardakani',capital=1380,code2='IR'), 
Country(code='KAZ',name='Kazakstan',continent='Asia',region='Southern and Central Asia',surface_area=2724900,independence_year=1991,population=16223000,life_expectancy=63.2,gnp=24375,gnp_old=23383,local_name='Qazaqstan',government_form='Republic',head_of_state='Nursultan Nazarbajev',capital=1864,code2='KZ'), 
Country(code='KGZ',name='Kyrgyzstan',continent='Asia',region='Southern and Central Asia',surface_area=199900,independence_year=1991,population=4699000,life_expectancy=63.4,gnp=1626,gnp_old=1767,local_name='Kyrgyzstan',government_form='Republic',head_of_state='Askar Akajev',capital=2253,code2='KG'), 
Country(code='LKA',name='Sri Lanka',continent='Asia',region='Southern and Central Asia',surface_area=65610,independence_year=1948,population=18827000,life_expectancy=71.8,gnp=15706,gnp_old=15091,local_name='Sri Lanka/Ilankai',government_form='Republic',head_of_state='Chandrika Kumaratunga',capital=3217,code2='LK'), 
Country(code='MDV',name='Maldives',continent='Asia',region='Southern and Central Asia',surface_area=298,independence_year=1965,population=286000,life_expectancy=62.2,gnp=199,gnp_old=0,local_name='Dhivehi Raajje/Maldives',government_form='Republic',head_of_state='Maumoon Abdul Gayoom',capital=2463,code2='MV'), 
Country(code='NPL',name='Nepal',continent='Asia',region='Southern and Central Asia',surface_area=147181,independence_year=1769,population=23930000,life_expectancy=57.8,gnp=4768,gnp_old=4837,local_name='Nepal',government_form='Constitutional Monarchy',head_of_state='Gyanendra Bir Bikram',capital=2729,code2='NP'), 
Country(code='PAK',name='Pakistan',continent='Asia',region='Southern and Central Asia',surface_area=796095,independence_year=1947,population=156483000,life_expectancy=61.1,gnp=61289,gnp_old=58549,local_name='Pakistan',government_form='Republic',head_of_state='Mohammad Rafiq Tarar',capital=2831,code2='PK'), 
Country(code='TJK',name='Tajikistan',continent='Asia',region='Southern and Central Asia',surface_area=143100,independence_year=1991,population=6188000,life_expectancy=64.1,gnp=1990,gnp_old=1056,local_name='Tocikiston',government_form='Republic',head_of_state='Emomali Rahmonov',capital=3261,code2='TJ'), 
Country(code='TKM',name='Turkmenistan',continent='Asia',region='Southern and Central Asia',surface_area=488100,independence_year=1991,population=4459000,life_expectancy=60.9,gnp=4397,gnp_old=2000,local_name='Turkmenostan',government_form='Republic',head_of_state='Saparmurad Nijazov',capital=3419,code2='TM'), 
Country(code='uZB',name='uzbekistan',continent='Asia',region='Southern and Central Asia',surface_area=447400,independence_year=1991,population=24318000,life_expectancy=63.7,gnp=14194,gnp_old=21300,local_name='uzbekiston',government_form='Republic',head_of_state='Islam Karimov',capital=3503,code2='uZ'), 
]
contries_list10 = [
Country(code='ARE',name='united Arab Emirates',continent='Asia',region='Middle East',surface_area=83600,independence_year=1971,population=2441000,life_expectancy=74.1,gnp=37966,gnp_old=36846,local_name='Al-Imarat al- Arabiya al-Muttahida',government_form='Emirate Federation',head_of_state='Zayid bin Sultan al-Nahayan',capital=65,code2='AE'), 
Country(code='ARM',name='Armenia',continent='Asia',region='Middle East',surface_area=29800,independence_year=1991,population=3520000,life_expectancy=66.4,gnp=1813,gnp_old=1627,local_name='Hajastan',government_form='Republic',head_of_state='Robert KotSarjan',capital=126,code2='AM'), 
Country(code='AZE',name='Azerbaijan',continent='Asia',region='Middle East',surface_area=86600,independence_year=1991,population=7734000,life_expectancy=62.9,gnp=4127,gnp_old=4100,local_name='Azarbaycan',government_form='Federal Republic',head_of_state='Heydar aliyev',capital=144,code2='AZ'), 
Country(code='BHR',name='Bahrain',continent='Asia',region='Middle East',surface_area=694,independence_year=1971,population=617000,life_expectancy=73,gnp=6366,gnp_old=6097,local_name='Al-Bahrayn',government_form='Monarchy (Emirate)',head_of_state='Hamad ibn Isa al-Khalifa',capital=149,code2='BH'), 
Country(code='CYP',name='Cyprus',continent='Asia',region='Middle East',surface_area=9251,independence_year=1960,population=754700,life_expectancy=76.7,gnp=9333,gnp_old=8246,local_name='Kypros/Kibris',government_form='Republic',head_of_state='Glafkos Klerides',capital=2430,code2='CY'), 
Country(code='GEO',name='Georgia',continent='Asia',region='Middle East',surface_area=69700,independence_year=1991,population=4968000,life_expectancy=64.5,gnp=6064,gnp_old=5924,local_name='Sakartvelo',government_form='Republic',head_of_state='Eduard Sevardnadze',capital=905,code2='GE'), 
Country(code='IRQ',name='Iraq',continent='Asia',region='Middle East',surface_area=438317,independence_year=1932,population=23115000,life_expectancy=66.5,gnp=11500,gnp_old=0,local_name='Al- Iraq',government_form='Republic',head_of_state='Saddam Hussein al-Takriti',capital=1365,code2='IQ'), 
Country(code='ISR',name='Israel',continent='Asia',region='Middle East',surface_area=21056,independence_year=1948,population=6217000,life_expectancy=78.6,gnp=97477,gnp_old=98577,local_name='Yisrael/Israil',government_form='Republic',head_of_state='Moshe Katzav',capital=1450,code2='IL'), 
Country(code='JOR',name='Jordan',continent='Asia',region='Middle East',surface_area=88946,independence_year=1946,population=5083000,life_expectancy=77.4,gnp=7526,gnp_old=7051,local_name='Al-urdunn',government_form='Constitutional Monarchy',head_of_state='Abdullah II',capital=1786,code2='JO'), 
Country(code='KWT',name='Kuwait',continent='Asia',region='Middle East',surface_area=17818,independence_year=1961,population=1972000,life_expectancy=76.1,gnp=27037,gnp_old=30373,local_name='Al-Kuwayt',government_form='Constitutional Monarchy (Emirate)',head_of_state='Jabir al-Ahmad al-Jabir al-Sabah',capital=2429,code2='KW'), 
Country(code='LBN',name='Lebanon',continent='Asia',region='Middle East',surface_area=10400,independence_year=1941,population=3282000,life_expectancy=71.3,gnp=17121,gnp_old=15129,local_name='Lubnan',government_form='Republic',head_of_state='emile Lahoud',capital=2438,code2='LB'), 
Country(code='OMN',name='Oman',continent='Asia',region='Middle East',surface_area=309500,independence_year=1951,population=2542000,life_expectancy=71.8,gnp=16904,gnp_old=16153,local_name='uman',government_form='Monarchy (Sultanate)',head_of_state='Qabus ibn Sa id',capital=2821,code2='OM'), 
Country(code='PSE',name='Palestine',continent='Asia',region='Middle East',surface_area=6257,independence_year=0,population=3101000,life_expectancy=71.4,gnp=4173,gnp_old=0,local_name='Filastin',government_form='Autonomous Area',head_of_state='Yasser (Yasir) Arafat',capital=4074,code2='PS'), 
Country(code='QAT',name='Qatar',continent='Asia',region='Middle East',surface_area=11000,independence_year=1971,population=599000,life_expectancy=72.4,gnp=9472,gnp_old=8920,local_name='Qatar',government_form='Monarchy',head_of_state='Hamad ibn Khalifa al-Thani',capital=2973,code2='QA'), 
Country(code='SAu',name='Saudi Arabia',continent='Asia',region='Middle East',surface_area=2149690,independence_year=1932,population=21607000,life_expectancy=67.8,gnp=137635,gnp_old=146171,local_name='Al- Arabiya as-Sa udiya',government_form='Monarchy',head_of_state='Fahd ibn Abdul-Aziz al-Sa ud',capital=3173,code2='SA'), 
Country(code='SYR',name='Syria',continent='Asia',region='Middle East',surface_area=185180,independence_year=1941,population=16125000,life_expectancy=68.5,gnp=65984,gnp_old=64926,local_name='Suriya',government_form='Republic',head_of_state='Bashar al-Assad',capital=3250,code2='SY'), 
Country(code='TuR',name='Turkey',continent='Asia',region='Middle East',surface_area=774815,independence_year=1923,population=66591000,life_expectancy=71,gnp=210721,gnp_old=189122,local_name='Turkiye',government_form='Republic',head_of_state='Ahmet Necdet Sezer',capital=3358,code2='TR'), 
Country(code='YEM',name='Yemen',continent='Asia',region='Middle East',surface_area=527968,independence_year=1918,population=18112000,life_expectancy=59.8,gnp=6041,gnp_old=5729,local_name='Al-Yaman',government_form='Republic',head_of_state='Ali Abdallah Salih',capital=1780,code2='YE'), 
]
contries_list11 = [
Country(code='ARG',name='Argentina',continent='South America',region='South America',surface_area=2780400,independence_year=1816,population=37032000,life_expectancy=75.1,gnp=340238,gnp_old=323310,local_name='Argentina',government_form='Federal Republic',head_of_state='Fernando de la Rua',capital=69,code2='AR'), 
Country(code='BOL',name='Bolivia',continent='South America',region='South America',surface_area=1098581,independence_year=1825,population=8329000,life_expectancy=63.7,gnp=8571,gnp_old=7967,local_name='Bolivia',government_form='Republic',head_of_state='Hugo Banzer Suarez',capital=194,code2='BO'), 
Country(code='BRA',name='Brazil',continent='South America',region='South America',surface_area=8547403,independence_year=1822,population=170115000,life_expectancy=62.9,gnp=776739,gnp_old=804108,local_name='Brasil',government_form='Federal Republic',head_of_state='Fernando Henrique Cardoso',capital=211,code2='BR'), 
Country(code='CHL',name='Chile',continent='South America',region='South America',surface_area=756626,independence_year=1810,population=15211000,life_expectancy=75.7,gnp=72949,gnp_old=75780,local_name='Chile',government_form='Republic',head_of_state='Ricardo Lagos Escobar',capital=554,code2='CL'), 
Country(code='COL',name='Colombia',continent='South America',region='South America',surface_area=1138914,independence_year=1810,population=42321000,life_expectancy=70.3,gnp=102896,gnp_old=105116,local_name='Colombia',government_form='Republic',head_of_state='Andres Pastrana Arango',capital=2257,code2='CO'), 
Country(code='ECu',name='Ecuador',continent='South America',region='South America',surface_area=283561,independence_year=1822,population=12646000,life_expectancy=71.1,gnp=19770,gnp_old=19769,local_name='Ecuador',government_form='Republic',head_of_state='Gustavo Noboa Bejarano',capital=594,code2='EC'), 
Country(code='FLK',name='Falkland Islands',continent='South America',region='South America',surface_area=12173,independence_year=0,population=2000,life_expectancy=0,gnp=0,gnp_old=0,local_name='Falkland Islands',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=763,code2='FK'), 
Country(code='GuF',name='French Guiana',continent='South America',region='South America',surface_area=90000,independence_year=0,population=181000,life_expectancy=76.1,gnp=681,gnp_old=0,local_name='Guyane francaise',government_form='Overseas Department of France',head_of_state='Jacques Chirac',capital=3014,code2='GF'), 
Country(code='GuY',name='Guyana',continent='South America',region='South America',surface_area=214969,independence_year=1966,population=861000,life_expectancy=64,gnp=722,gnp_old=743,local_name='Guyana',government_form='Republic',head_of_state='Bharrat Jagdeo',capital=928,code2='GY'), 
Country(code='PER',name='Peru',continent='South America',region='South America',surface_area=1285216,independence_year=1821,population=25662000,life_expectancy=70,gnp=64140,gnp_old=65186,local_name='Peru/Piruw',government_form='Republic',head_of_state='Valentin Paniagua Corazao',capital=2890,code2='PE'), 
Country(code='PRY',name='Paraguay',continent='South America',region='South America',surface_area=406752,independence_year=1811,population=5496000,life_expectancy=73.7,gnp=8444,gnp_old=9555,local_name='Paraguay',government_form='Republic',head_of_state='Luis angel Gonzalez Macchi',capital=2885,code2='PY'), 
Country(code='SuR',name='Suriname',continent='South America',region='South America',surface_area=163265,independence_year=1975,population=417000,life_expectancy=71.4,gnp=870,gnp_old=706,local_name='Suriname',government_form='Republic',head_of_state='Ronald Venetiaan',capital=3243,code2='SR'), 
Country(code='uRY',name='uruguay',continent='South America',region='South America',surface_area=175016,independence_year=1828,population=3337000,life_expectancy=75.2,gnp=20831,gnp_old=19967,local_name='uruguay',government_form='Republic',head_of_state='Jorge Batlle Ibanez',capital=3492,code2='uY'), 
Country(code='VEN',name='Venezuela',continent='South America',region='South America',surface_area=912050,independence_year=1811,population=24170000,life_expectancy=73.1,gnp=95023,gnp_old=88434,local_name='Venezuela',government_form='Federal Republic',head_of_state='Hugo Chavez FrIas',capital=3539,code2='VE'), 
]
contries_list12 = [
Country(code='ASM',name='American Samoa',continent='Oceania',region='Polynesia',surface_area=199,independence_year=0,population=68000,life_expectancy=75.1,gnp=334,gnp_old=0,local_name='Amerika Samoa',government_form='uS Territory',head_of_state='George W. Bush',capital=54,code2='AS'), 
Country(code='COK',name='Cook Islands',continent='Oceania',region='Polynesia',surface_area=236,independence_year=0,population=20000,life_expectancy=71.1,gnp=100,gnp_old=0,local_name='The Cook Islands',government_form='Nonmetropolitan Territory of New Zealand',head_of_state='Elisabeth II',capital=583,code2='CK'), 
Country(code='NIu',name='Niue',continent='Oceania',region='Polynesia',surface_area=260,independence_year=0,population=2000,life_expectancy=0,gnp=0,gnp_old=0,local_name='Niue',government_form='Nonmetropolitan Territory of New Zealand',head_of_state='Elisabeth II',capital=2805,code2='Nu'), 
Country(code='PCN',name='Pitcairn',continent='Oceania',region='Polynesia',surface_area=49,independence_year=0,population=50,life_expectancy=0,gnp=0,gnp_old=0,local_name='Pitcairn',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=2912,code2='PN'), 
Country(code='PYF',name='French Polynesia',continent='Oceania',region='Polynesia',surface_area=4000,independence_year=0,population=235000,life_expectancy=74.8,gnp=818,gnp_old=781,local_name='Polynesie francaise',government_form='Nonmetropolitan Territory of France',head_of_state='Jacques Chirac',capital=3016,code2='PF'), 
Country(code='TKL',name='Tokelau',continent='Oceania',region='Polynesia',surface_area=12,independence_year=0,population=2000,life_expectancy=0,gnp=0,gnp_old=0,local_name='Tokelau',government_form='Nonmetropolitan Territory of New Zealand',head_of_state='Elisabeth II',capital=3333,code2='TK'), 
Country(code='TON',name='Tonga',continent='Oceania',region='Polynesia',surface_area=650,independence_year=1970,population=99000,life_expectancy=67.9,gnp=146,gnp_old=170,local_name='Tonga',government_form='Monarchy',head_of_state="Taufa'ahau Tupou IV",capital=3334,code2='TO'), 
Country(code='TuV',name='Tuvalu',continent='Oceania',region='Polynesia',surface_area=26,independence_year=1978,population=12000,life_expectancy=66.3,gnp=6,gnp_old=0,local_name='Tuvalu',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=3424,code2='TV'), 
Country(code='WLF',name='Wallis and Futuna',continent='Oceania',region='Polynesia',surface_area=200,independence_year=0,population=15000,life_expectancy=0,gnp=0,gnp_old=0,local_name='Wallis-et-Futuna',government_form='Nonmetropolitan Territory of France',head_of_state='Jacques Chirac',capital=3536,code2='WF'), 
Country(code='WSM',name='Samoa',continent='Oceania',region='Polynesia',surface_area=2831,independence_year=1962,population=180000,life_expectancy=69.2,gnp=141,gnp_old=157,local_name='Samoa',government_form='Parlementary Monarchy',head_of_state='Malietoa Tanumafili II',capital=3169,code2='WS'), 
]
contries_list13 = [
Country(code='AuT',name='Austria',continent='Europe',region='Western Europe',surface_area=83859,independence_year=1918,population=8091800,life_expectancy=77.7,gnp=211860,gnp_old=206025,local_name='osterreich',government_form='Federal Republic',head_of_state='Thomas Klestil',capital=1523,code2='AT'), 
Country(code='BEL',name='Belgium',continent='Europe',region='Western Europe',surface_area=30518,independence_year=1830,population=10239000,life_expectancy=77.8,gnp=249704,gnp_old=243948,local_name='Belgie/Belgique',government_form='Constitutional Monarchy, Federation',head_of_state='Albert II',capital=179,code2='BE'), 
Country(code='CHE',name='Switzerland',continent='Europe',region='Western Europe',surface_area=41284,independence_year=1499,population=7160400,life_expectancy=79.6,gnp=264478,gnp_old=256092,local_name='Schweiz/Suisse/Svizzera/Svizra',government_form='Federation',head_of_state='Adolf Ogi',capital=3248,code2='CH'), 
Country(code='DEu',name='Germany',continent='Europe',region='Western Europe',surface_area=357022,independence_year=1955,population=82164700,life_expectancy=77.4,gnp=2133367,gnp_old=2102826,local_name='Deutschland',government_form='Federal Republic',head_of_state='Johannes Rau',capital=3068,code2='DE'), 
Country(code='FRA',name='France',continent='Europe',region='Western Europe',surface_area=551500,independence_year=843,population=59225700,life_expectancy=78.8,gnp=1424285,gnp_old=1392448,local_name='France',government_form='Republic',head_of_state='Jacques Chirac',capital=2974,code2='FR'), 
Country(code='LIE',name='Liechtenstein',continent='Europe',region='Western Europe',surface_area=160,independence_year=1806,population=32300,life_expectancy=78.8,gnp=1119,gnp_old=1084,local_name='Liechtenstein',government_form='Constitutional Monarchy',head_of_state='Hans-Adam II',capital=2446,code2='LI'), 
Country(code='LuX',name='Luxembourg',continent='Europe',region='Western Europe',surface_area=2586,independence_year=1867,population=435700,life_expectancy=77.1,gnp=16321,gnp_old=15519,local_name='Luxembourg/Letzebuerg',government_form='Constitutional Monarchy',head_of_state='Henri',capital=2452,code2='Lu'), 
Country(code='MCO',name='Monaco',continent='Europe',region='Western Europe',surface_area=1.5,independence_year=1861,population=34000,life_expectancy=78.8,gnp=776,gnp_old=0,local_name='Monaco',government_form='Constitutional Monarchy',head_of_state='Rainier III',capital=2695,code2='MC'), 
Country(code='NLD',name='Netherlands',continent='Europe',region='Western Europe',surface_area=41526,independence_year=1581,population=15864000,life_expectancy=78.3,gnp=371362,gnp_old=360478,local_name='Nederland',government_form='Constitutional Monarchy',head_of_state='Willem-Alexander',capital=5,code2='NL'), 
]
contries_list14 = [
Country(code='BEN',name='Benin',continent='Africa',region='Western Africa',surface_area=112622,independence_year=1960,population=6097000,life_expectancy=50.2,gnp=2357,gnp_old=2141,local_name='Benin',government_form='Republic',head_of_state='Mathieu Kerekou',capital=187,code2='BJ'), 
Country(code='BFA',name='Burkina Faso',continent='Africa',region='Western Africa',surface_area=274000,independence_year=1960,population=11937000,life_expectancy=46.7,gnp=2425,gnp_old=2201,local_name='Burkina Faso',government_form='Republic',head_of_state='Blaise Compaore',capital=549,code2='BF'), 
Country(code='CIV',name='Cote dIvoire',continent='Africa',region='Western Africa',surface_area=322463,independence_year=1960,population=14786000,life_expectancy=45.2,gnp=11345,gnp_old=10285,local_name='Cote dIvoire',government_form='Republic',head_of_state='Laurent Gbagbo',capital=2814,code2='CI'), 
Country(code='CPV',name='Cape Verde',continent='Africa',region='Western Africa',surface_area=4033,independence_year=1975,population=428000,life_expectancy=68.9,gnp=435,gnp_old=420,local_name='Cabo Verde',government_form='Republic',head_of_state='Antonio Mascarenhas Monteiro',capital=1859,code2='CV'), 
Country(code='GHA',name='Ghana',continent='Africa',region='Western Africa',surface_area=238533,independence_year=1957,population=20212000,life_expectancy=57.4,gnp=7137,gnp_old=6884,local_name='Ghana',government_form='Republic',head_of_state='John Kufuor',capital=910,code2='GH'), 
Country(code='GIN',name='Guinea',continent='Africa',region='Western Africa',surface_area=245857,independence_year=1958,population=7430000,life_expectancy=45.6,gnp=2352,gnp_old=2383,local_name='Guinee',government_form='Republic',head_of_state='Lansana Conte',capital=926,code2='GN'), 
Country(code='GMB',name='Gambia',continent='Africa',region='Western Africa',surface_area=11295,independence_year=1965,population=1305000,life_expectancy=53.2,gnp=320,gnp_old=325,local_name='The Gambia',government_form='Republic',head_of_state='Yahya Jammeh',capital=904,code2='GM'), 
Country(code='GNB',name='Guinea-Bissau',continent='Africa',region='Western Africa',surface_area=36125,independence_year=1974,population=1213000,life_expectancy=49,gnp=293,gnp_old=272,local_name='Guine-Bissau',government_form='Republic',head_of_state='Kumba Iala',capital=927,code2='GW'), 
Country(code='LBR',name='Liberia',continent='Africa',region='Western Africa',surface_area=111369,independence_year=1847,population=3154000,life_expectancy=51,gnp=2012,gnp_old=0,local_name='Liberia',government_form='Republic',head_of_state='Charles Taylor',capital=2440,code2='LR'), 
Country(code='MLI',name='Mali',continent='Africa',region='Western Africa',surface_area=1240192,independence_year=1960,population=11234000,life_expectancy=46.7,gnp=2642,gnp_old=2453,local_name='Mali',government_form='Republic',head_of_state='Alpha Oumar Konare',capital=2482,code2='ML'), 
Country(code='MRT',name='Mauritania',continent='Africa',region='Western Africa',surface_area=1025520,independence_year=1960,population=2670000,life_expectancy=50.8,gnp=998,gnp_old=1081,local_name='Muritaniya/Mauritanie',government_form='Republic',head_of_state='Maaouiya Ould Sid Ahmad Taya',capital=2509,code2='MR'), 
Country(code='NER',name='Niger',continent='Africa',region='Western Africa',surface_area=1267000,independence_year=1960,population=10730000,life_expectancy=41.3,gnp=1706,gnp_old=1580,local_name='Niger',government_form='Republic',head_of_state='Mamadou Tandja',capital=2738,code2='NE'), 
Country(code='NGA',name='Nigeria',continent='Africa',region='Western Africa',surface_area=923768,independence_year=1960,population=111506000,life_expectancy=51.6,gnp=65707,gnp_old=58623,local_name='Nigeria',government_form='Federal Republic',head_of_state='Olusegun Obasanjo',capital=2754,code2='NG'), 
Country(code='SEN',name='Senegal',continent='Africa',region='Western Africa',surface_area=196722,independence_year=1960,population=9481000,life_expectancy=62.2,gnp=4787,gnp_old=4542,local_name='Senegal/Sounougal',government_form='Republic',head_of_state='Abdoulaye Wade',capital=3198,code2='SN'), 
Country(code='SHN',name='Saint Helena',continent='Africa',region='Western Africa',surface_area=314,independence_year=0,population=6000,life_expectancy=76.8,gnp=0,gnp_old=0,local_name='Saint Helena',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=3063,code2='SH'), 
Country(code='SLE',name='Sierra Leone',continent='Africa',region='Western Africa',surface_area=71740,independence_year=1961,population=4854000,life_expectancy=45.3,gnp=746,gnp_old=858,local_name='Sierra Leone',government_form='Republic',head_of_state='Ahmed Tejan Kabbah',capital=3207,code2='SL'), 
Country(code='TGO',name='Togo',continent='Africa',region='Western Africa',surface_area=56785,independence_year=1960,population=4629000,life_expectancy=54.7,gnp=1449,gnp_old=1400,local_name='Togo',government_form='Republic',head_of_state='Gnassingbe Eyadema',capital=3332,code2='TG'), 
]
contries_list15 = [
Country(code='BGR',name='Bulgaria',continent='Europe',region='Eastern Europe',surface_area=110994,independence_year=1908,population=8190900,life_expectancy=70.9,gnp=12178,gnp_old=10169,local_name='Balgarija',government_form='Republic',head_of_state='Petar Stojanov',capital=539,code2='BG'), 
Country(code='BLR',name='Belarus',continent='Europe',region='Eastern Europe',surface_area=207600,independence_year=1991,population=10236000,life_expectancy=68,gnp=13714,gnp_old=0,local_name='Belarus',government_form='Republic',head_of_state='Aljaksandr LukaSenka',capital=3520,code2='BY'), 
Country(code='CZE',name='Czech Republic',continent='Europe',region='Eastern Europe',surface_area=78866,independence_year=1993,population=10278100,life_expectancy=74.5,gnp=55017,gnp_old=52037,local_name='esko',government_form='Republic',head_of_state='Vaclav Havel',capital=3339,code2='CZ'), 
Country(code='HuN',name='Hungary',continent='Europe',region='Eastern Europe',surface_area=93030,independence_year=1918,population=10043200,life_expectancy=71.4,gnp=48267,gnp_old=45914,local_name='Magyarorszag',government_form='Republic',head_of_state='Ferenc Madl',capital=3483,code2='Hu'), 
Country(code='MDA',name='Moldova',continent='Europe',region='Eastern Europe',surface_area=33851,independence_year=1991,population=4380000,life_expectancy=64.5,gnp=1579,gnp_old=1872,local_name='Moldova',government_form='Republic',head_of_state='Vladimir Voronin',capital=2690,code2='MD'), 
Country(code='POL',name='Poland',continent='Europe',region='Eastern Europe',surface_area=323250,independence_year=1918,population=38653600,life_expectancy=73.2,gnp=151697,gnp_old=135636,local_name='Polska',government_form='Republic',head_of_state='Aleksander Kwasniewski',capital=2928,code2='PL'), 
Country(code='ROM',name='Romania',continent='Europe',region='Eastern Europe',surface_area=238391,independence_year=1878,population=22455500,life_expectancy=69.9,gnp=38158,gnp_old=34843,local_name='Romania',government_form='Republic',head_of_state='Ion Iliescu',capital=3018,code2='RO'), 
Country(code='RuS',name='Russian Federation',continent='Europe',region='Eastern Europe',surface_area=17075400,independence_year=1991,population=146934000,life_expectancy=67.2,gnp=276608,gnp_old=442989,local_name='Rossija',government_form='Federal Republic',head_of_state='Vladimir Putin',capital=3580,code2='Ru'), 
Country(code='SVK',name='Slovakia',continent='Europe',region='Eastern Europe',surface_area=49012,independence_year=1993,population=5398700,life_expectancy=73.7,gnp=20594,gnp_old=19452,local_name='Slovensko',government_form='Republic',head_of_state='Rudolf Schuster',capital=3209,code2='SK'), 
Country(code='uKR',name='ukraine',continent='Europe',region='Eastern Europe',surface_area=603700,independence_year=1991,population=50456000,life_expectancy=66,gnp=42168,gnp_old=49677,local_name='ukrajina',government_form='Republic',head_of_state='Leonid KutSma',capital=3426,code2='uA'), 
]
contries_list16 = [
Country(code='BMu',name='Bermuda',continent='North America',region='North America',surface_area=53,independence_year=0,population=65000,life_expectancy=76.9,gnp=2328,gnp_old=2190,local_name='Bermuda',government_form='Dependent Territory of the uK',head_of_state='Elisabeth II',capital=191,code2='BM'), 
Country(code='CAN',name='Canada',continent='North America',region='North America',surface_area=9970610,independence_year=1867,population=31147000,life_expectancy=79.4,gnp=598862,gnp_old=625626,local_name='Canada',government_form='Constitutional Monarchy, Federation',head_of_state='Elisabeth II',capital=1822,code2='CA'), 
Country(code='GRL',name='Greenland',continent='North America',region='North America',surface_area=2166090,independence_year=0,population=56000,life_expectancy=68.1,gnp=0,gnp_old=0,local_name='Kalaallit Nunaat/Gronland',government_form='Part of Denmark',head_of_state='Margrethe II',capital=917,code2='GL'), 
Country(code='SPM',name='Saint Pierre and Miquelon',continent='North America',region='North America',surface_area=242,independence_year=0,population=7000,life_expectancy=77.6,gnp=0,gnp_old=0,local_name='Saint-Pierre-et-Miquelon',government_form='Territorial Collectivity of France',head_of_state='Jacques Chirac',capital=3067,code2='PM'), 
Country(code='uSA',name='united States',continent='North America',region='North America',surface_area=9363520,independence_year=1776,population=278357000,life_expectancy=77.1,gnp=8510700,gnp_old=8110900,local_name='united States',government_form='Federal Republic',head_of_state='George W. Bush',capital=3813,code2='uS'), 
]
contries_list17 = [
Country(code='BRN',name='Brunei',continent='Asia',region='Southeast Asia',surface_area=5765,independence_year=1984,population=328000,life_expectancy=73.6,gnp=11705,gnp_old=12460,local_name='Brunei Darussalam',government_form='Monarchy (Sultanate)',head_of_state='Haji Hassan al-Bolkiah',capital=538,code2='BN'), 
Country(code='IDN',name='Indonesia',continent='Asia',region='Southeast Asia',surface_area=1904569,independence_year=1945,population=212107000,life_expectancy=68,gnp=84982,gnp_old=215002,local_name='Indonesia',government_form='Republic',head_of_state='Abdurrahman Wahid',capital=939,code2='ID'), 
Country(code='KHM',name='Cambodia',continent='Asia',region='Southeast Asia',surface_area=181035,independence_year=1953,population=11168000,life_expectancy=56.5,gnp=5121,gnp_old=5670,local_name='Kampuchea',government_form='Constitutional Monarchy',head_of_state='Norodom Sihanouk',capital=1800,code2='KH'), 
Country(code='LAO',name='Laos',continent='Asia',region='Southeast Asia',surface_area=236800,independence_year=1953,population=5433000,life_expectancy=53.1,gnp=1292,gnp_old=1746,local_name='Lao',government_form='Republic',head_of_state='Khamtay Siphandone',capital=2432,code2='LA'), 
Country(code='MMR',name='Myanmar',continent='Asia',region='Southeast Asia',surface_area=676578,independence_year=1948,population=45611000,life_expectancy=54.9,gnp=180375,gnp_old=171028,local_name='Myanma Pye',government_form='Republic',head_of_state='kenraali Than Shwe',capital=2710,code2='MM'), 
Country(code='MYS',name='Malaysia',continent='Asia',region='Southeast Asia',surface_area=329758,independence_year=1957,population=22244000,life_expectancy=70.8,gnp=69213,gnp_old=97884,local_name='Malaysia',government_form='Constitutional Monarchy, Federation',head_of_state='Salahuddin Abdul Aziz Shah Alhaj',capital=2464,code2='MY'), 
Country(code='NAM',name='Namibia',continent='Africa',region='Southern Africa',surface_area=824292,independence_year=1990,population=1726000,life_expectancy=42.5,gnp=3101,gnp_old=3384,local_name='Namibia',government_form='Republic',head_of_state='Sam Nujoma',capital=2726,code2='NA'), 
Country(code='PHL',name='Philippines',continent='Asia',region='Southeast Asia',surface_area=300000,independence_year=1946,population=75967000,life_expectancy=67.5,gnp=65107,gnp_old=82239,local_name='Pilipinas',government_form='Republic',head_of_state='Gloria Macapagal-Arroyo',capital=766,code2='PH'), 
Country(code='SGP',name='Singapore',continent='Asia',region='Southeast Asia',surface_area=618,independence_year=1965,population=3567000,life_expectancy=80.1,gnp=86503,gnp_old=96318,local_name='Singapore/Singapura/Xinjiapo/Singapur',government_form='Republic',head_of_state='Sellapan Rama Nathan',capital=3208,code2='SG'), 
Country(code='THA',name='Thailand',continent='Asia',region='Southeast Asia',surface_area=513115,independence_year=1350,population=61399000,life_expectancy=68.6,gnp=116416,gnp_old=153907,local_name='Prathet Thai',government_form='Constitutional Monarchy',head_of_state='Bhumibol Adulyadej',capital=3320,code2='TH'), 
Country(code='TMP',name='East Timor',continent='Asia',region='Southeast Asia',surface_area=14874,independence_year=0,population=885000,life_expectancy=46,gnp=0,gnp_old=0,local_name='Timor Timur',government_form='Administrated by the uN',head_of_state='Jose Alexandre Gusmao',capital=1522,code2='TP'), 
Country(code='VNM',name='Vietnam',continent='Asia',region='Southeast Asia',surface_area=331689,independence_year=1945,population=79832000,life_expectancy=69.3,gnp=21929,gnp_old=22834,local_name='Viet Nam',government_form='Socialistic Republic',head_of_state='Tran Duc Luong',capital=3770,code2='VN'), 
]
contries_list18 = [
Country(code='BWA',name='Botswana',continent='Africa',region='Southern Africa',surface_area=581730,independence_year=1966,population=1622000,life_expectancy=39.3,gnp=4834,gnp_old=4935,local_name='Botswana',government_form='Republic',head_of_state='Festus G. Mogae',capital=204,code2='BW'), 
Country(code='LSO',name='Lesotho',continent='Africa',region='Southern Africa',surface_area=30355,independence_year=1966,population=2153000,life_expectancy=50.8,gnp=1061,gnp_old=1161,local_name='Lesotho',government_form='Constitutional Monarchy',head_of_state='Letsie III',capital=2437,code2='LS'), 
Country(code='SWZ',name='Swaziland',continent='Africa',region='Southern Africa',surface_area=17364,independence_year=1968,population=1008000,life_expectancy=40.4,gnp=1206,gnp_old=1312,local_name='kaNgwane',government_form='Monarchy',head_of_state='Mswati III',capital=3244,code2='SZ'), 
Country(code='ZAF',name='South Africa',continent='Africa',region='Southern Africa',surface_area=1221037,independence_year=1910,population=40377000,life_expectancy=51.1,gnp=116729,gnp_old=129092,local_name='South Africa',government_form='Republic',head_of_state='Thabo Mbeki',capital=716,code2='ZA'), 
]
contries_list19 = [
Country(code='CHN',name='China',continent='Asia',region='Eastern Asia',surface_area=9572900,independence_year=-1523,population=1277558000,life_expectancy=71.4,gnp=982268,gnp_old=917719,local_name='Zhongquo',government_form="People'sRepublic",head_of_state='Jiang Zemin',capital=1891,code2='CN'), 
Country(code='HKG',name='Hong Kong',continent='Asia',region='Eastern Asia',surface_area=1075,independence_year=0,population=6782000,life_expectancy=79.5,gnp=166448,gnp_old=173610,local_name='Xianggang/Hong Kong',government_form='Special Administrative Region of China',head_of_state='Jiang Zemin',capital=937,code2='HK'), 
Country(code='JPN',name='Japan',continent='Asia',region='Eastern Asia',surface_area=377829,independence_year=-660,population=126714000,life_expectancy=80.7,gnp=3787042,gnp_old=4192638,local_name='Nihon/Nippon',government_form='Constitutional Monarchy',head_of_state='Akihito',capital=1532,code2='JP'), 
Country(code='KOR',name='South Korea',continent='Asia',region='Eastern Asia',surface_area=99434,independence_year=1948,population=46844000,life_expectancy=74.4,gnp=320749,gnp_old=442544,local_name='Taehan Minguk (Namhan)',government_form='Republic',head_of_state='Kim Dae-jung',capital=2331,code2='KR'), 
Country(code='MAC',name='Macao',continent='Asia',region='Eastern Asia',surface_area=18,independence_year=0,population=473000,life_expectancy=81.6,gnp=5749,gnp_old=5940,local_name='Macau/Aomen',government_form='Special Administrative Region of China',head_of_state='Jiang Zemin',capital=2454,code2='MO'), 
Country(code='MNG',name='Mongolia',continent='Asia',region='Eastern Asia',surface_area=1566500,independence_year=1921,population=2662000,life_expectancy=67.3,gnp=1043,gnp_old=933,local_name='Mongol uls',government_form='Republic',head_of_state='Natsagiin Bagabandi',capital=2696,code2='MN'), 
Country(code='PRK',name='North Korea',continent='Asia',region='Eastern Asia',surface_area=120538,independence_year=1948,population=24039000,life_expectancy=70.7,gnp=5332,gnp_old=0,local_name='Choson Minjujuui In min Konghwaguk (Bukhan)',government_form='Socialistic Republic',head_of_state='Kim Jong-il',capital=2318,code2='KP'), 
Country(code='TWN',name='Taiwan',continent='Asia',region='Eastern Asia',surface_area=36188,independence_year=1945,population=22256000,life_expectancy=76.4,gnp=256254,gnp_old=263451,local_name='Tai-wan',government_form='Republic',head_of_state='Chen Shui-bian',capital=3263,code2='TW'), 
]
contries_list20 = [
Country(code='DNK',name='Denmark',continent='Europe',region='Nordic Countries',surface_area=43094,independence_year=800,population=5330000,life_expectancy=76.5,gnp=174099,gnp_old=169264,local_name='Danmark',government_form='Constitutional Monarchy',head_of_state='Margrethe II',capital=3315,code2='DK'), 
Country(code='FIN',name='Finland',continent='Europe',region='Nordic Countries',surface_area=338145,independence_year=1917,population=5171300,life_expectancy=77.4,gnp=121914,gnp_old=119833,local_name='Suomi',government_form='Republic',head_of_state='Tarja Halonen',capital=3236,code2='FI'), 
Country(code='FRO',name='Faroe Islands',continent='Europe',region='Nordic Countries',surface_area=1399,independence_year=0,population=43000,life_expectancy=78.4,gnp=0,gnp_old=0,local_name='Foroyar',government_form='Part of Denmark',head_of_state='Margrethe II',capital=901,code2='FO'), 
Country(code='ISL',name='Iceland',continent='Europe',region='Nordic Countries',surface_area=103000,independence_year=1944,population=279000,life_expectancy=79.4,gnp=8255,gnp_old=7474,local_name='Island',government_form='Republic',head_of_state='olafur Ragnar GrImsson',capital=1449,code2='IS'), 
Country(code='NOR',name='Norway',continent='Europe',region='Nordic Countries',surface_area=323877,independence_year=1905,population=4478500,life_expectancy=78.7,gnp=145895,gnp_old=153370,local_name='Norge',government_form='Constitutional Monarchy',head_of_state='Harald V',capital=2807,code2='NO'), 
Country(code='SJM',name='Svalbard and Jan Mayen',continent='Europe',region='Nordic Countries',surface_area=62422,independence_year=0,population=3200,life_expectancy=0,gnp=0,gnp_old=0,local_name='Svalbard og Jan Mayen',government_form='Dependent Territory of Norway',head_of_state='Harald V',capital=938,code2='SJ'), 
Country(code='SWE',name='Sweden',continent='Europe',region='Nordic Countries',surface_area=449964,independence_year=836,population=8861400,life_expectancy=79.6,gnp=226492,gnp_old=227757,local_name='Sverige',government_form='Constitutional Monarchy',head_of_state='Carl XVI Gustaf',capital=3048,code2='SE'), 
]
contries_list21 = [
Country(code='DZA',name='Algeria',continent='Africa',region='Northern Africa',surface_area=2381741,independence_year=1962,population=31471000,life_expectancy=69.7,gnp=49982,gnp_old=46966,local_name='Al-Jazair/Algerie',government_form='Republic',head_of_state='Abdelaziz Bouteflika',capital=35,code2='DZ'), 
Country(code='EGY',name='Egypt',continent='Africa',region='Northern Africa',surface_area=1001449,independence_year=1922,population=68470000,life_expectancy=63.3,gnp=82710,gnp_old=75617,local_name='Misr',government_form='Republic',head_of_state='Hosni Mubarak',capital=608,code2='EG'), 
Country(code='ESH',name='Western Sahara',continent='Africa',region='Northern Africa',surface_area=266000,independence_year=0,population=293000,life_expectancy=49.8,gnp=60,gnp_old=0,local_name='As-Sahrawiya',government_form='Occupied by Marocco',head_of_state='Mohammed Abdel Aziz',capital=2453,code2='EH'), 
Country(code='LBY',name='Libyan Arab Jamahiriya',continent='Africa',region='Northern Africa',surface_area=1759540,independence_year=1951,population=5605000,life_expectancy=75.5,gnp=44806,gnp_old=40562,local_name='Libiya',government_form='Socialistic State',head_of_state='Muammar al-Qadhafi',capital=2441,code2='LY'), 
Country(code='MAR',name='Morocco',continent='Africa',region='Northern Africa',surface_area=446550,independence_year=1956,population=28351000,life_expectancy=69.1,gnp=36124,gnp_old=33514,local_name='Al-Maghrib',government_form='Constitutional Monarchy',head_of_state='Mohammed VI',capital=2486,code2='MA'), 
Country(code='SDN',name='Sudan',continent='Africa',region='Northern Africa',surface_area=2505813,independence_year=1956,population=29490000,life_expectancy=56.6,gnp=10162,gnp_old=0,local_name='As-Sudan',government_form='Islamic Republic',head_of_state='Omar Hassan Ahmad al-Bashir',capital=3225,code2='SD'), 
Country(code='TuN',name='Tunisia',continent='Africa',region='Northern Africa',surface_area=163610,independence_year=1956,population=9586000,life_expectancy=73.7,gnp=20026,gnp_old=18898,local_name='Tunis/Tunisie',government_form='Republic',head_of_state='Zine al-Abidine Ben Ali',capital=3349,code2='TN'), 
]
contries_list22 = [
Country(code='FJI',name='Fiji Islands',continent='Oceania',region='Melanesia',surface_area=18274,independence_year=1970,population=817000,life_expectancy=67.9,gnp=1536,gnp_old=2149,local_name='Fiji Islands',government_form='Republic',head_of_state='Josefa Iloilo',capital=764,code2='FJ'), 
Country(code='NCL',name='New Caledonia',continent='Oceania',region='Melanesia',surface_area=18575,independence_year=0,population=214000,life_expectancy=72.8,gnp=3563,gnp_old=0,local_name='Nouvelle-Caledonie',government_form='Nonmetropolitan Territory of France',head_of_state='Jacques Chirac',capital=3493,code2='NC'), 
Country(code='PNG',name='Papua New Guinea',continent='Oceania',region='Melanesia',surface_area=462840,independence_year=1975,population=4807000,life_expectancy=63.1,gnp=4988,gnp_old=6328,local_name='Papua New Guinea/Papua Niugini',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=2884,code2='PG'), 
Country(code='SLB',name='Solomon Islands',continent='Oceania',region='Melanesia',surface_area=28896,independence_year=1978,population=444000,life_expectancy=71.3,gnp=182,gnp_old=220,local_name='Solomon Islands',government_form='Constitutional Monarchy',head_of_state='Elisabeth II',capital=3161,code2='SB'), 
Country(code='VuT',name='Vanuatu',continent='Oceania',region='Melanesia',surface_area=12189,independence_year=1980,population=190000,life_expectancy=60.6,gnp=261,gnp_old=246,local_name='Vanuatu',government_form='Republic',head_of_state='John Bani',capital=3537,code2='Vu'), 
]
contries_list23 = [
Country(code='FSM',name='Micronesia, Federated States of',continent='Oceania',region='Micronesia',surface_area=702,independence_year=1990,population=119000,life_expectancy=68.6,gnp=212,gnp_old=0,local_name='Micronesia',government_form='Federal Republic',head_of_state='Leo A. Falcam',capital=2689,code2='FM'), 
Country(code='GuM',name='Guam',continent='Oceania',region='Micronesia',surface_area=549,independence_year=0,population=168000,life_expectancy=77.8,gnp=1197,gnp_old=1136,local_name='Guam',government_form='uS Territory',head_of_state='George W. Bush',capital=921,code2='Gu'), 
Country(code='KIR',name='Kiribati',continent='Oceania',region='Micronesia',surface_area=726,independence_year=1979,population=83000,life_expectancy=59.8,gnp=40.7,gnp_old=0,local_name='Kiribati',government_form='Republic',head_of_state='Teburoro Tito',capital=2256,code2='KI'), 
Country(code='MHL',name='Marshall Islands',continent='Oceania',region='Micronesia',surface_area=181,independence_year=1990,population=64000,life_expectancy=65.5,gnp=97,gnp_old=0,local_name='Marshall Islands/Majol',government_form='Republic',head_of_state='Kessai Note',capital=2507,code2='MH'), 
Country(code='MNP',name='Northern Mariana Islands',continent='Oceania',region='Micronesia',surface_area=464,independence_year=0,population=78000,life_expectancy=75.5,gnp=0,gnp_old=0,local_name='Northern Mariana Islands',government_form='Commonwealth of the uS',head_of_state='George W. Bush',capital=2913,code2='MP'), 
Country(code='NRu',name='Nauru',continent='Oceania',region='Micronesia',surface_area=21,independence_year=1968,population=12000,life_expectancy=60.8,gnp=197,gnp_old=0,local_name='Naoero/Nauru',government_form='Republic',head_of_state='Bernard Dowiyogo',capital=2728,code2='NR'), 
Country(code='PLW',name='Palau',continent='Oceania',region='Micronesia',surface_area=459,independence_year=1994,population=19000,life_expectancy=68.6,gnp=105,gnp_old=0,local_name='Belau/Palau',government_form='Republic',head_of_state='Kuniwo Nakamura',capital=2881,code2='PW'), 
]
contries_list24 = [
Country(code='uMI',name='united States Minor Outlying Islands',continent='Oceania',region='Micronesia/Caribbean',surface_area=16,independence_year=0,population=0,life_expectancy=0,gnp=0,gnp_old=0,local_name='united States Minor Outlying Islands',government_form='Dependent Territory of the uS',head_of_state='George W. Bush',capital=0,code2='uM'), 

]
#CREACION DE GET METHOD
@router.get("/antarctica/", status_code = 200)
async def region():
    return  (contries_list)

#GET METHOD WITH FILTER
@router.get("/antarctica/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/antarctica/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/antarctica/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/antarctica/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Caribbean/", status_code = 200)
async def region():
    return  (contries_list1)

#GET METHOD WITH FILTER
@router.get("/Caribbean/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list1)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Caribbean/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list1):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list1.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Caribbean/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list1):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list1[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Caribbean/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list1):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list1[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Australia and New Zealand/", status_code = 200)
async def region():
    return  (contries_list2)

#GET METHOD WITH FILTER
@router.get("/Australia and New Zealand/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list2)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Australia and New Zealand/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list2):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list2.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Australia and New Zealand/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list2):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list2[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Australia and New Zealand/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list2):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list2[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Baltic Countries/", status_code = 200)
async def region():
    return  (contries_list3)

#GET METHOD WITH FILTER
@router.get("/Baltic Countries/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list3)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Baltic Countries/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list3):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list3.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Baltic Countries/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list3):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list3[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Baltic Countries/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list3):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list3[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/British Islands/", status_code = 200)
async def region():
    return  (contries_list4)

#GET METHOD WITH FILTER
@router.get("/British Islands/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list4)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/British Islands/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list4):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list4.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/British Islands/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list4):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list4[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/British Islands/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list4):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list4[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Central Africa/", status_code = 200)
async def region():
    return  (contries_list5)

#GET METHOD WITH FILTER
@router.get("/Central Africa/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list5)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Central Africa/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list5):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list5.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Central Africa/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list5):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list5[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Central Africa/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list5):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list5[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Central America/", status_code = 200)
async def region():
    return  (contries_list6)

#GET METHOD WITH FILTER
@router.get("/Central America/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list6)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Central America/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list6):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list6.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Central America/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list6):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list6[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Central America/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list6):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list6[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Southern Europe/", status_code = 200)
async def region():
    return  (contries_list7)

#GET METHOD WITH FILTER
@router.get("/Southern Europe/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list7)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Southern Europe/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list7):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list7.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Southern Europe/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list7):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list7[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Southern Europe/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list7):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list7[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Eastern Africa/", status_code = 200)
async def region():
    return  (contries_list8)

#GET METHOD WITH FILTER
@router.get("/Eastern Africa/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list8)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Eastern Africa/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list8):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list8.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Eastern Africa/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list8):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list8[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Eastern Africa/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list8):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list8[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Southern and Central Asia/", status_code = 200)
async def region():
    return  (contries_list9)

#GET METHOD WITH FILTER
@router.get("/Southern and Central Asia/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list9)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Southern and Central Asia/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list9):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list9.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Southern and Central Asia/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list9):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list9[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Southern and Central Asia/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list9):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list9[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Middle East/", status_code = 200)
async def region():
    return  (contries_list10)

#GET METHOD WITH FILTER
@router.get("/Middle East/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list10)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Middle East/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list10):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list10.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Middle East/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list10):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list10[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Middle East/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list10):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list10[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Southern and Central Asia/", status_code = 200)
async def region():
    return  (contries_list9)

#GET METHOD WITH FILTER
@router.get("/Southern and Central Asia/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list9)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Southern and Central Asia/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list9):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list9.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Southern and Central Asia/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list9):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list9[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Southern and Central Asia/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list9):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list9[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/South America/", status_code = 200)
async def region():
    return  (contries_list11)

#GET METHOD WITH FILTER
@router.get("/South America/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list11)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/South America/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list11):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list11.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/South America/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list11):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list11[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/South America/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list11):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list11[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Polynesia/", status_code = 200)
async def region():
    return  (contries_list12)

#GET METHOD WITH FILTER
@router.get("/Polynesia/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list12)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Polynesia/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list12):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list12.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Polynesia/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list12):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list12[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Polynesia/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list12):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list12[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Western Europe/", status_code = 200)
async def region():
    return  (contries_list13)

#GET METHOD WITH FILTER
@router.get("/Western Europe/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list13)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Western Europe/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list13):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list13.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Western Europe/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list13):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list13[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Western Europe/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list13):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list13[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Western Africa/", status_code = 200)
async def region():
    return  (contries_list14)

#GET METHOD WITH FILTER
@router.get("/Western Africa/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list14)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Western Africa/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list14):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list14.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Western Africa/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list14):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list14[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Western Africa/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list14):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list14[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")

########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Eastern Europe/", status_code = 200)
async def region():
    return  (contries_list15)

#GET METHOD WITH FILTER
@router.get("/Eastern Europe/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list15)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Eastern Europe/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list15):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list15.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Eastern Europe/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list15):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list15[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Eastern Europe/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list15):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list15[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/North America/", status_code = 200)
async def region():
    return  (contries_list15)

#GET METHOD WITH FILTER
@router.get("/North America/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list16)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/North America/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list16):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list16.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/North America/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list16):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list16[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/North America/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list16):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list16[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Southeast Asia/", status_code = 200)
async def region():
    return  (contries_list17)

#GET METHOD WITH FILTER
@router.get("/North America/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list17)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Southeast Asia/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list17):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list17.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Southeast Asia/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list17):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list17[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Southeast Asia/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list17):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list17[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Southern Africa/", status_code = 200)
async def region():
    return  (contries_list18)

#GET METHOD WITH FILTER
@router.get("/Southern Africa/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list18)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Southern Africa/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list18):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list18.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Southern Africa/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list18):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list18[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Southern Africa/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list18):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list18[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Eastern Asia/", status_code = 200)
async def region():
    return  (contries_list19)

#GET METHOD WITH FILTER
@router.get("/Eastern Asia/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list19)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Eastern Asia/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list19):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list19.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Eastern Asia/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list19):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list19[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Eastern Asia/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list19):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list19[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Nordic Countries/", status_code = 200)
async def region():
    return  (contries_list20)

#GET METHOD WITH FILTER
@router.get("/Nordic Countries/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list20)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Nordic Countries/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list20):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list20.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Nordic Countries/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list20):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list20[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Nordic Countries/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list20):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list20[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Northern Africa/", status_code = 200)
async def region():
    return  (contries_list21)

#GET METHOD WITH FILTER
@router.get("/Northern Africa/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list21)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Northern Africa/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list21):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list21.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Northern Africa/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list21):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list21[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Northern Africa/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list21):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list21[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")    
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Melanesia/", status_code = 200)
async def region():
    return  (contries_list22)

#GET METHOD WITH FILTER
@router.get("/Melanesia/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list22)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Melanesia/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list22):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list22.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Melanesia/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list22):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list22[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Melanesia/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list22):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list22[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")    
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Micronesia/", status_code = 200)
async def region():
    return  (contries_list23)

#GET METHOD WITH FILTER
@router.get("/Micronesia/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list23)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Micronesia/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list23):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list23.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Micronesia/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list23):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list23[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Micronesia/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list23):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list23[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")    
########################################################################################################
########################################################################################################
#CREACION DE GET METHOD
@router.get("/Micronesia/Caribbean/", status_code = 200)
async def region():
    return  (contries_list24)

#GET METHOD WITH FILTER
@router.get("/Micronesia/Caribbean/{id}")
async def region(id:str):
    country = filter (lambda country: country.code == id, contries_list24)  #Función de orden superior
    try:
        return list(country)[0]
    except:
        raise HTTPException(status_code = 404, detail="PAIS NO EXISTENTE")

#CREACION DE POST METHOD
@router.post("/Micronesia/Caribbean/", status_code = 201)
async def continent(country:Country):
    found = False
    
    for index, saved_user in enumerate(contries_list24):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            raise HTTPException(status_code = 409, detail="PAIS YA REGISTRADA")
    else:
        contries_list24.append(country)
        return country

#CREACION DE PUT METHOD
@router.put("/Micronesia/Caribbean/", status_code = 200)
async def continent(country:Country):
    
    found = False
    
    for index, saved_user in enumerate(contries_list24):
        if saved_user.code == country.code or saved_user.code2 == country.code2:
            contries_list24[index] = country
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return country

#DELETE METHOD
@router.delete("/Micronesia/Caribbean/{id}", status_code = 200)
async def continent(id:str):
    
    found = False
    
    for index, saved_user in enumerate(contries_list24):
        if saved_user.code == id or saved_user.code2 == id:
            del contries_list24[index]
            found = True
            return "PAIS ELIMINADO"
    if not found:
        raise HTTPException(status_code = 401, detail="PAIS NO ENCONTRADO")    