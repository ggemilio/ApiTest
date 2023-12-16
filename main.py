from fastapi import FastAPI
from dbClient import DbClient

app = FastAPI()
dbClinet = DbClient()

@app.get("/")
async def root():
    return {"message": "Hello World"}

//main.py
import uvicorn

if __name__ == "__main__":
  uvicorn.run("server.api:app", host="0.0.0.0", port=8000, reload=True)