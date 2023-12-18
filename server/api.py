from fastapi import FastAPI
from server.dbClient import DbClient
from dotenv import load_dotenv
from models.post import Post

load_dotenv()
app = FastAPI()
dbClinet = DbClient()

@app.get("/", tags=["Root"])
async def read_root():
    return dbClinet.getDataFromTable("Posts")

@app.post("/posts")
async def create_post(post: Post):
    post_data = {
    "post_content": post.post_content,
    "op": post.op
    }
    dbClinet.insertToTable("Posts", post_data)
    return post
