from fastapi import APIRouter , Depends , HTTPException , status
from .. import schemas , database , models , JWtoken
from ..hashing import Hashing
from sqlalchemy.orm import Session
from datetime import timedelta , timezone
from ..JWtoken import  create_access_token
from fastapi.security import OAuth2PasswordRequestForm
get_db = database.get_db

router = APIRouter(
    tags=['Authentication']
)

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db :Session = Depends(get_db) ):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="User not founddddd")
    
    if not Hashing.verify(user.password , request.password) :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Incorrect Password")
    
    access_token_expires = timedelta(minutes=JWtoken.ACCESS_TOKEN_EXPIRE_LIMIT)
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return schemas.Token(access_token=access_token, token_type="bearer")
    