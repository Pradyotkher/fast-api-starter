from typing import Union

from fastapi import FastAPI

app = FastAPI()

list = ["Apple" , "Banana"]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/returnList")
def  get_list():
    return list