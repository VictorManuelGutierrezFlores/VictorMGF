#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app = FastAPI()

#Levantamos el server Uvicorn
#-uvicorn GETyPOST:app --reload-
# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000

class Passenger(BaseModel):
    passengerID:int
    Survived:int
    Pclass:int
    Name: str
    Sex:str
    Age:int

#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
passengers_list = [Passenger(passengerID=1, Survived=0,Pclass=3, Name="Braund, Mr. Owen Harris", Sex="Male", Age=22),
                Passenger(passengerID=2, Survived=1,Pclass=1, Name="Cumings, Mrs. John Bradley (Florence Briggs Thayer)", Sex="Female", Age=38),
                Passenger(passengerID=3, Survived=1,Pclass=3, Name="Heikkinen, Miss. Laina", Sex="Female", Age=26),
                Passenger(passengerID=4, Survived=1,Pclass=1, Name="Futrelle, Mrs. Jacques Heath (Lily May Peel)", Sex="Female", Age=35),
                Passenger(passengerID=5, Survived=0,Pclass=3, Name="Allen, Mr. William Henry", Sex="Male", Age=35),
                Passenger(passengerID=6, Survived=0,Pclass=3, Name="Moran, Mr. James", Sex="Male", Age=0),
                Passenger(passengerID=7, Survived=0,Pclass=1, Name="McCarthy, Mr. Timothy J", Sex="Male", Age=54),
                Passenger(passengerID=8, Survived=0,Pclass=3, Name="Palsson, Master. Gosta Leonard", Sex="Male", Age=2),
                Passenger(passengerID=9, Survived=1,Pclass=3, Name="Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)", Sex="Female", Age=27),
                Passenger(passengerID=10, Survived=1,Pclass=3, Name="Nasser, Mrs. Nicholas (Adele Achem)", Sex="Female", Age=14),
                Passenger(passengerID=11, Survived=1,Pclass=3, Name="Sandstrom, Miss. Marguerite Rut", Sex="Female", Age=4),
                Passenger(passengerID=12, Survived=1,Pclass=1, Name="Bonnell, Miss. Elizabeth", Sex="Female", Age=58),
                Passenger(passengerID=13, Survived=0,Pclass=3, Name="Saundercock, Mr. William Henry", Sex="Male", Age=20),
                Passenger(passengerID=14, Survived=0,Pclass=3, Name="Andersson, Mr. Anders Johan", Sex="Male", Age=39),
                Passenger(passengerID=15, Survived=0,Pclass=3, Name="Vestrom, Miss. Hulda Amanda Adolfina", Sex="Female", Age=14),
                Passenger(passengerID=16, Survived=1,Pclass=2, Name="Hewlett, Mrs. (Mary D Kingcome)", Sex="Female", Age=55),
                Passenger(passengerID=17, Survived=0,Pclass=3, Name="Rice, Master. Eugene", Sex="Male", Age=2),
                Passenger(passengerID=18, Survived=1,Pclass=2, Name="Williams, Mr. Charles Eugene", Sex="Male", Age=0),
                Passenger(passengerID=19, Survived=0,Pclass=3, Name="Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)", Sex="Female", Age=31),
                Passenger(passengerID=20, Survived=1,Pclass=2, Name="Masselmani, Mrs. Fatima", Sex="Female", Age=0),
                Passenger(passengerID=21, Survived=0,Pclass=2, Name="Fynney, Mr. Joseph J", Sex="Male", Age=35),
                Passenger(passengerID=22, Survived=1,Pclass=2, Name="Beesley, Mr. Lawrence", Sex="Male", Age=34),
                Passenger(passengerID=23, Survived=1,Pclass=3, Name="McGowan, Miss. Anna ""Annie""", Sex="Female", Age=15),
                Passenger(passengerID=24, Survived=1,Pclass=1, Name="Sloper, Mr. William Thompson", Sex="Male", Age=28),
                Passenger(passengerID=25, Survived=1,Pclass=3, Name="Palsson, Miss. Torborg Danira", Sex="Female", Age=8)
                ]


#CREACION DE GET METHOD
@app.get("/listapasajeros/")
async def listapasajeros():
    return  (passengers_list)

#CREACION DE POST METHOD
@app.post("/listapasajeros/")
async def listapasajeros(person:Passenger):
    found = False
    
    for index, saved_user in enumerate(passengers_list):
        if saved_user.passengerID == person.passengerID:
            return {"ERROR":"EL USUARIO YA EXISTE"}
    else:
        passengers_list.append(person)
        return person
#http://127.0.0.1:8000/listapasajeros/