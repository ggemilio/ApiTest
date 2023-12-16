from fastapi import FastAPI
from dbClient import DbClient

app = FastAPI()
dbClinet = DbClient()

@app.get("/")
async def root():
    return dbClinet.getDataFromTable("Posts", "*")