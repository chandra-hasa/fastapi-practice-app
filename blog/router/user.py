from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import database
from repository import userRepo
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["User API's"],
    prefix="/fastapi/v1/user"
)


@router.post('/create', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return userRepo.create_new_user(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(database.get_db)):
    return userRepo.get_user(id, db)
