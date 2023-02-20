#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI, HTTPException
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
from fastapi import APIRouter


#Creamos un objeto a partir de la clase FastAPI
router = APIRouter()

#Levantamos el server Uvicorn
#-uvicorn router_2:app --reload-
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
                Passenger(passengerID=4, Survived=1,Pclass=1, Name="Futrelle, Mrs. Jacques Heath (Lily May Peel)", Sex="Female", Age=35)]

#CREACION DE GET METHOD
@router.get("/listapasajeros/", status_code = 200)
async def listapasajeros():
    return  (passengers_list)

@router.get("/listapasajero/{ID}")
async def listapasajeros(ID:int):
    person=filter (lambda Passenger: Passenger.passengerID == ID, passengers_list)  #Función de orden superior
    try:
        return list(person)[0]
    except:
        raise HTTPException(status_code = 404, detail="NO HAY USUARIOS REGISTRADOS")

#CREACION DE POST METHOD
@router.post("/listapasajeros/", status_code = 201)
async def listapasajeros(person:Passenger):
    found = False
    
    for index, saved_user in enumerate(passengers_list):
        if saved_user.passengerID == person.passengerID:
            raise HTTPException(status_code = 409, detail="USUARIO EXISTENTE")
    else:
        passengers_list.append(person)
        return person
#http://127.0.0.1:8000/listapasajeros/

#CREACION DE PUT METHOD
@router.put("/listaspasajeros/", status_code = 200)
async def listapasajeros(person:Passenger):
    
    found = False
    
    for index, saved_user in enumerate(passengers_list):
        if saved_user.passengerID == person.passengerID:
            passengers_list[index] = person
            found = True
    if not found:
        raise HTTPException(status_code = 406, detail="ERROR AL ACTUALIZAR")
    else:
        return person

#DELETE METHOD
@router.delete("/listapasajeros/{id}", status_code = 200)
async def listapasajeros(id:int):
    
    found = False
    
    for index, saved_user in enumerate(passengers_list):
        if saved_user.passengerID == id:
            del passengers_list[index]
            found = True
            return "USUARIO ELIMINADO"
        
    if not found:
        raise HTTPException(status_code = 401, detail="USUARIO NO ENCONTRADO")