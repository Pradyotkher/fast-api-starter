from fastapi import FastAPI , Depends , status , HTTPException , Response
from . import schemas,models,hashing
from sqlalchemy.orm import Session
from .database import engine , SessionLocal , base , get_db
from typing import List
from .routers import blog , user, authentication

base.metadata.create_all(engine)

app = FastAPI() 

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

# @app.get("/")
# def read_root(db: Session = Depends(get_db)):
#     return {"message": "Connected to MySQL successfully!"}



    