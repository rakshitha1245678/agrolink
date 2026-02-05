from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.utils.auth import hash_password

router = APIRouter(prefix="/buyer", tags=["Buyer"])

@router.post("/register")
def register_buyer(user: UserCreate, db: Session = Depends(get_db)):
    hashed_pwd = hash_password(user.password)
    buyer = User(
        name=user.name,
        role="buyer",
        password=hashed_pwd
    )
    db.add(buyer)
    db.commit()
    return {"message": "Buyer registered successfully"}
