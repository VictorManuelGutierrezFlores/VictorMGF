# En vez de Importar el framework fastapi, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, Body
from fastapi.encoders import jsonable_encoder

# Importamos nuestro cliente para poder agregar usuarios a la db****nEw
from mongo_client import db_client

from models.student_model import (
    StudentSchema, 
    UpdateStudentModel,
    ErrorResponse,
    ResponseModel
)

from mongo_client import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student
)

# Creamos un objeto a partir de la clase FastAPI
router = APIRouter()

# Levantamos el server Uvicorn
# -uvicorn 4_codigos_HTTP:app --reload-
# {"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}

# ** POST **
@router.post("/userdb/", response_description="Datos del estudiante añadidos exitosamente", status_code=200)
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Estudiante añadido exitosamente")

# ***Get
@router.get("/userdb/", status_code = 200)
async def get_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, "Extraccion exitosa")
    else:
        raise HTTPException(status_code= 404, detail="SIN REGISTROS EXISTENTES")

#GET CON ID
@router.get("/userdb/{id}", status_code=200)
async def get_student_data(id):
    student = await retrieve_student(id)
    if student:
        return ResponseModel(student, "Datos de estudiante devueltos")
    else:
        raise HTTPException(status_code= 404, detail="ESTUDIANTE NO ENCONTRADO")

# PUT CON ID
@router.put("/{id}")
async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(id, req)
    if updated_student:
        return ResponseModel(
            "Estudiante con ID: {} actualizado correctamente".format(id),
            "Estudiante actualizado!",
        )
    else:
        raise HTTPException(status_code=404, detail="Ocurrio un error al actualizar, no encontrado")
    
# DELETE WITH ID
@router.delete("/{id}", response_description="Estudiante elimando de la base de datos", status_code=200)
async def delete_student_data(id: str):
    # ESPERA VALOR BOOLEANO PARA CONTINUAR
    deleted_student = await delete_student(id)
    if deleted_student:
        return ResponseModel(
            "Estudiante con  ID: {} removido".format(id), "Estudiante eliminado correctamente"
        )
    else:
        return ErrorResponseModel(
            "Ocurrio un error", 404, "Estudiante con ID {0} no existe".format(id)
        )
        raise HTTPException(status_code=404)
