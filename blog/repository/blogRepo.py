from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models
import schemas


def get_all_blogs(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_blog(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with ID: {id} is not found")
    return blog


def create_new_blog(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title,
                           body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update_blog(id, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUNDdetail,
                            detail=f"Blog with ID: {id} is not found")
    blog.update(request)
    db.commit()
    return {"Updated Successfully"}


def delete_blog(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with ID: {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {f"Blog with id:{id} has been deleted"}
