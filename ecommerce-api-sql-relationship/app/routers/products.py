from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, HTTPException

from app.database import get_db
from app.models import Product
from app.schemas import (ProductCreate, ProductResponse, InventoryUpdate)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# Create a new product


@router.post("/", response_model=ProductResponse)
def create_product(product_data: ProductCreate, db: Session = Depends(get_db)):
    product = Product(
        name=product_data.name.strip(),
        description=product_data.description.strip(),
        price=product_data.price,
        stock_quantity=product_data.stock_quantity
    )
    db.add(product)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Product not created"
        ) from exc

    db.refresh(product)
    return product

# Get products


@router.get('/', response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).order_by(Product.name.asc()).all()
    return products

# Get product by id


@router.get('/{product_id}', response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = (
        db.query(Product).filter(Product.id == product_id).first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product

# Update inventory


@router.patch('/{product_id}/inventory', response_model=ProductResponse)
def update_inventory(product_id: int, inventory_data: InventoryUpdate, db: Session = Depends(get_db)):
    product = (
        db.query(Product).filter(Product.id == product_id).first()
    )

    if not product:
        raise HTTPException(
            status_code=409,
            detail="Product not found"
        )

    product.stock_quantity += inventory_data.stock_quantity
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Inventory not updated"
        ) from exc

    db.refresh(product)
    return product
