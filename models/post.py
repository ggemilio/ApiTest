from pydantic import BaseModel

class Post(BaseModel):
    post_content: str
    op: str