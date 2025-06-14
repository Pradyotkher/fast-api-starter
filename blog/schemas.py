from pydantic import BaseModel
from typing import List
class Blog(BaseModel):
    title : str
    body : str
    class Config:
        orm_model : True

class User(BaseModel):
    name : str
    email : str
    password : str

class ShowUser(BaseModel):
    name : str
    email : str
    blogs : List['Blog']
    class Config:
        orm_model : True

class ShowBlog(Blog):
    title : str
    body : str
    creator : ShowUser
    class Config:
        orm_model : True

class Login(BaseModel):
    userName : str
    password : str

 
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None