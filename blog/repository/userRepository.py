from sqlalchemy.orm import Session
from fastapi import Depends , HTTPException , status
from .. import models , database , schemas , hashing


get_db = database.get_db()

def create_user(request : schemas.User , db : Session = Depends(get_db)):
    hashedPwd = hashing.Hashing.hash_password(password=request.password)
    print(hashedPwd)
    newUser = models.User(name = request.name , email = request.email , password = hashedPwd)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

def get_user(id,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id)
    if user.first() is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="User not found")
    
    return user.first()