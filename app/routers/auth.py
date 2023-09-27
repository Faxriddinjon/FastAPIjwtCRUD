from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..utils import Hash
from ..oauth2 import create_access_token

router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)


@router.post("/", response_model=schemas.Token)
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if user is None:
        raise HTTPExpection(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}