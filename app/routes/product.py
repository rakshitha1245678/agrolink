from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.product import Product
from app.schemas.product_schema import ProductCreate

router = APIRouter(prefix="/product", tags=["Product"])

@router.post("/add")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(
        name=product.name,
        price=product.price,
        quantity=product.quantity
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"message": "Product added successfully"}

@router.get("/all")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
