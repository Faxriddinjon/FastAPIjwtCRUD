from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models, utils

router=APIRouter(
    prefix='/user',
    tags=["Users"]
)

get_db=database.get_db
Hash=utils.Hash

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session=Depends(get_db)):
    # hashed_password = Hash.bcrypt(request.password)
    # request.password = hashed_password
    new_user=models.User(**request.dict())
    db.add(new_user)
    db.commit()
    # db.refresh(new_user)
    return new_user


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    
    return user

