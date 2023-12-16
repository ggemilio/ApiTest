from fastapi import FastAPI
from server.dbClient import DbClient

app = FastAPI()
dbClinet = DbClient()

@app.get("/", tags=["Root"])
async def read_root():
  return dbClinet.getDataFromTable("Posts")