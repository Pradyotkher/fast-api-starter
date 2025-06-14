from sqlalchemy.orm import Session
from fastapi import Depends , HTTPException , status
from .. import models , database , schemas

get_db = database.get_db

def getBlogDetails(db:Session = Depends(get_db)):
    list =db.query(models.Blog).all()
    return list 

# Create Blog 
def create(request : schemas.Blog , db:Session = Depends(get_db)):
    print(request)
    new_blog = models.Blog(
        title = request.title,
        body = request.body,
        userId = 1
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"created Blog":new_blog}

def getById(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Blog Not found 123")
    else:
        return  blog 
    
def delete_blog(id:int , db:Session =  Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)

    if blog.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Blog Id not found")

    blog.delete(synchronize_session=False)

    db.commit()
    return {"deleted":id}

def updateBlog(id:int,request:schemas.Blog ,db:Session = Depends(get_db)):
    
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    
    if blog.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Blog Id not found")

    blog.update(request.model_dump())
    db.commit()
    updated_blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    return updated_blog