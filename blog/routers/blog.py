from fastapi import APIRouter , Depends , status , HTTPException
from .. import database , schemas , models , oAuth2
from sqlalchemy.orm import Session
from typing import List
from ..repository import blogRepository

router = APIRouter(
    tags=['Blogs'],
    prefix="/blog"
)

get_db = database.get_db

blog_tags = ['blogs'] 

@router.get("/getAllBlogDetails" , response_model=List[schemas.ShowBlog])
def getAllBlogs(db : Session = Depends(get_db) , get_current_user : schemas.User = Depends(oAuth2.get_current_user)):
    return blogRepository.getBlogDetails(db)


@router.post("/" , status_code=status.HTTP_201_CREATED)
def create(request : schemas.Blog , db:Session = Depends(get_db), get_current_user : schemas.User = Depends(oAuth2.get_current_user)):
    new_blog = blogRepository.create(request=request , db = db)
    return new_blog


@router.get("/getById/{id}",response_model=schemas.ShowBlog)
def getById(id , db : Session = Depends(get_db), get_current_user : schemas.User = Depends(oAuth2.get_current_user)):
   return blogRepository.getById(id = id , db = db)
    
@router.delete("/delete/{id}" , status_code=status.HTTP_204_NO_CONTENT )
def delete_blog(id , db:Session =  Depends(get_db), get_current_user : schemas.User = Depends(oAuth2.get_current_user)):
    return blogRepository.delete_blog(id=id , db=db)

@router.put("/updateBlog/{id}" , status_code=status.HTTP_202_ACCEPTED )
def updateBlog(id,request:schemas.Blog ,db:Session = Depends(get_db), get_current_user : schemas.User = Depends(oAuth2.get_current_user)):
  return blogRepository.updateBlog(id = id , db = db , request=request)
