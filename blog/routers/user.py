from fastapi import APIRouter , status  , Depends
from .. import schemas , database
from ..repository import userRepository
from sqlalchemy.orm import Session
router = APIRouter(
    prefix="/user",
    tags=['User']
)

get_db = database.get_db
 
user_tag = ['user']

@router.post("/createUser" , status_code=status.HTTP_201_CREATED , response_model=schemas.ShowUser)
def create_user(request : schemas.User , db : Session = Depends(get_db)):
    return userRepository.create_user(request=request , db = db)

@router.get("/{id}" , response_model=schemas.ShowUser)
def get_user(id,db:Session = Depends(get_db)):
    return userRepository.get_user(id = id,  db = db)
