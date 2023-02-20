#IMPORTACION DE FUNCION APIROUTER
from fastapi import APIRouter

#CREACION DE OBJETO ROUTER
router = APIRouter()

#INSTANCIA DE PRODUCTOS
@router.get("/products/")
async def products():
    return ["Producto1","Producto2","Producto3","Producto4", "Producto5"]