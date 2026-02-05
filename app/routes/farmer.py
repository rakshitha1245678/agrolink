from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.utils.auth import hash_password

router = APIRouter(prefix="/farmer", tags=["Farmer"])

@router.post("/register")
def register_farmer(user: UserCreate, db: Session = Depends(get_db)):
    hashed_pwd = hash_password(user.password)
    farmer = User(
        name=user.name,
        role="farmer",
        password=hashed_pwd
    )
    db.add(farmer)
    db.commit()
    return {"message": "Farmer registered successfully"}
