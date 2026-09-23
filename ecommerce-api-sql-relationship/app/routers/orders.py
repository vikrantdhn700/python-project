from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app.models import (
    User,
    Product,
    Order,
    OrderItem
)
from app.schemas import OrderCreate, OrderResponse


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

# Create New Order


@router.post("/", response_model=OrderResponse)
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    user = (
        db.query(User)
        .filter(User.id == order_data.user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not order_data.items:
        raise HTTPException(
            status_code=400,
            detail="Order must contain at least one item"
        )

    order = Order(
        user_id=order_data.user_id,
        total_amount=0,
        status="pending"
    )

    db.add(order)
    db.flush()

    order_total = 0

    for item in order_data.items:

        product = (
            db.query(Product)
            .filter(Product.id == item.product_id)
            .first()
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"Product {item.product_id} not found"
            )

        if product.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient inventory for {product.name}"
            )

        unit_price = product.price

        item_total = unit_price * item.quantity

        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=item.quantity,
            unit_price=unit_price,
            item_total=item_total
        )

        db.add(order_item)
        product.stock_quantity -= item.quantity
        order_total += item_total

    order.total_amount = order_total
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Ordr not created"
        ) from exc

    db.refresh(order)

    return order

# View user's orders


@router.get(
    "/user/{user_id}",
    response_model=list[OrderResponse]
)
def get_user_orders(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    orders = (
        db.query(Order)
        .join(User, Order.user_id == User.id)
        .filter(User.id == user_id)
        .order_by(Order.created_at.desc())
        .all()
    )

    return orders

# Cancel order


@router.patch("/{order_id}/cancel")
def cancel_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    if order.status == "cancelled":
        raise HTTPException(
            status_code=400,
            detail="Order is already cancelled"
        )

    if order.status == "completed":
        raise HTTPException(
            status_code=400,
            detail="Completed order cannot be cancelled"
        )

    for item in order.items:

        product = (
            db.query(Product)
            .filter(Product.id == item.product_id)
            .first()
        )

        if product:
            product.stock_quantity += item.quantity

    order.status = "cancelled"

    db.commit()

    return {
        "message": "Order cancelled successfully",
        "order_id": order.id,
        "status": order.status
    }
