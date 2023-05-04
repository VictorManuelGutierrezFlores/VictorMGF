#########################################Primera Parte################################################
#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos la clase staticfiles para recursos estáticos****
from fastapi.staticfiles import StaticFiles

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()


#Creamos una app para acceder al directorio de recursos estaticos***
app.mount("/static", StaticFiles(directory="static"), name="static")
#app.mount("/static/image", StaticFiles(directory="image"), name="images")

#Utilizamos la (instancia) función get del framework FastAPI
@app.get("/")

#creamos la función asincrona "imprimir"
async def imprimir():
    return "Hola a todos"


#Levantamos el server Uvicorn
#-uvicorn 6_StaticResources:app --reload-
# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000

#########################################Segunda Parte################################################

#creamos la función asincrona con formato JSON
@app.get("/Git")
async def imprimir():
    return {"Git_curso":"https://github.com/freddy-7777/Modelos-de-desarrollo-WEB.git"}

# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/Git

######################################CLASE 3################################

#Detener server con: ctrl + c
#Documentación con Swagger:  http://127.0.0.1:8000/docs
#Documentación con Redocly:  http://127.0.0.1:8000/redoc