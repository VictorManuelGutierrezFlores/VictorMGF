from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "fullname": "Fulanito 22",
                "email": "fulanito@fulanito.com",
            }
        }
    

class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Fulanito 22 cambiadito",
                "email": "fulanit22o@fulanito.com",
            }
        }
        
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponse(error, code, message):
    return {"error":error, "code":code, "message":message}