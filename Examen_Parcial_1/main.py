#IMPORTACION DE FASTAPI
from fastapi import FastAPI
#IMPORTAMCION DESDE LA CARPETA ROUTER
from Routers import Africa, Antarctica, Asia, continent, country, Europe, North_America,South_America,Oceania,regions,Punto_D

#CREACION DEL OBJETO APP
app = FastAPI()
app.include_router(country.router)
app.include_router(continent.router)
app.include_router(regions.router)
app.include_router(Antarctica.router)
app.include_router(Africa.router)
app.include_router(Asia.router)
app.include_router(Europe.router)
app.include_router(North_America.router)
app.include_router(Oceania.router)
app.include_router(South_America.router)
app.include_router(Punto_D.router)

@app.get("/")
async def imprimir():
    return "Hola todos"