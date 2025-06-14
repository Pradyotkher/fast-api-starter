from typing import Union,Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Creating a class which will behave as an Entity 
class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

list = ["Apple" , "Banana"]

@app.get("/")
def read_root(limit=5 , published : bool = True ,  sort:Optional[str]=None):
    if(published) :
        return {"Hello": f"World{limit}"}
    else:
        return "False statement executed"

@app.get("/blog/unpublished")
def get_unpublished():
    return {"data" : "unpublished blogs"}

@app.get("/blog/{id}")
def  get_list(id:int , limit=5):
    list.append(id)
    return {"list": list,"id":id , "limit":limit}

@app.post("/blog/createBlog")
def create_blog(request : Blog) :
    print(request.title)
    return {
            "data":"Blog is created",
            "Body":request
            }