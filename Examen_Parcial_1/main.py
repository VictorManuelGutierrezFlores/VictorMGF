#IMPORTACION DE FASTAPI
from fastapi import FastAPI
#IMPORTAMCION DESDE LA CARPETA ROUTER
from Routers import country, continent, regions

#CREACION DEL OBJETO APP
app = FastAPI()
app.include_router(country.router)
app.include_router(continent.router)
app.include_router(regions.router)

@app.get("/")
async def imprimir():
    return "Hola todos"