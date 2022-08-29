from fastapi import APIRouter, Depends, status
from typing import List
import schemas
import database
from repository import blogRepo
from sqlalchemy.orm import Session
import oauth2

router = APIRouter(
    tags=["Blog API's"],
    prefix="/fastapi/v1/blog"
)


@router.get('/show', response_model=List[schemas.ShowBlog])
def show_all_blogs(db: Session = Depends(database.get_db), current_user=Depends(oauth2.get_current_user)):
    return blogRepo.get_all_blogs(db)


@ router.post('/create', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db), current_user=Depends(oauth2.get_current_user)):
    return blogRepo.create_new_blog(request, db)


@ router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(id, db: Session = Depends(database.get_db), current_user=Depends(oauth2.get_current_user)):
    return blogRepo.get_blog(id, db)


@ router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog_by_id(id, db: Session = Depends(database.get_db), current_user=Depends(oauth2.get_current_user)):
    return blogRepo.delete_blog(id, db)


@ router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog_by_id(id, request: schemas.Blog, db: Session = Depends(database.get_db), current_user=Depends(oauth2.get_current_user)):
    return blogRepo.update_by_id(id, request, db)
