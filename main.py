from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

@app.get("/blog")# path operation decorator
# query paramter
def index(limit: int = 10, published: bool = True,sort:Optional[str] = None):
    #return published
    if published:
        #fetch published blogs
        return {"message": f"blog list - limit: {limit}, published: {published}"}
    else:
        return {"message": f"blog list{limit} from db"}
@app.get("/blog/unpublished")
#path parameter
def unpublished():
    #fetch unpublished blogs
    return {"message": "unpublished blogs"}

@app.get("/about")# path operation decorator
def about():
    return {"message": "About page"}
#path parameter
# #dynamic routing
@app.get("/blog/{id}")# path operation decorator
def show(id:int):# type of id and other query parameters is int
    #fetch blog with id = id
    return {"message": f"blog id: {id}"}
@app.get("/blog/{id}/comments")
def show_comments(id:int):
    #fetch comments of blog with id = id
    return {"message": f"blog id: {id} - comments"}
# create model and use it in request body
class Blog(BaseModel):
    title:str
    body:str
    published_at: Optional[bool]
@app.post("/blog")
def create_blog(blog: Blog):
    return {"message": f"blog created with title {blog.title}"}
# debugging