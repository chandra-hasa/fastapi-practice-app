from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
import schemas
import hashing
import database


def create_new_user(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(
        name=request.name, email=request.email,
        password=hashing.Hash.getBcryptPassword(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with ID: {id} is not found")
    return user
