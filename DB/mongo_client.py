from pymongo import MongoClient
import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection("students_collection")

db_client = MongoClient()

#HELPER
def student_helper(student) -> dict:
    return{
        "id":str (student["_id"]),
        "fullname":student["fullname"],
        "email":student["email"]
    }


# RECUPERA TODO LOS ESTUDIANTES EN LA BASE DE DATOS
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


# AÑADE NUEVOS ESTUDIANTES
async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# RECUPERA UN ESTUDIANTE EN ESPECIFICO CON ID
async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


# ACTUALIZA ESTUDIANTE CON ID
async def update_student(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False


# ELIMINA ESTUDIANTE CON ID
async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True