from fastapi import FastAPI
from router import router_db
import uvicorn

app = FastAPI()

app.include_router(router_db.router)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message":"Bienvenido a esta app:D"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)