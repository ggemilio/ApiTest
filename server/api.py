from fastapi import FastAPI
from server.dbClient import DbClient
from dotenv import load_dotenv

app = FastAPI()
dbClinet = DbClient()
load_dotenv()

@app.get("/", tags=["Root"])
async def read_root():
  return dbClinet.getDataFromTable("Users")