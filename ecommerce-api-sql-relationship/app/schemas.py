from decimal import Decimal
from datetime import datetime

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ConfigDict,
)


class UserCreate(BaseModel):
    full_name: str = Field(
        min_length=2,
        max_length=100,
    )

    email: EmailStr


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    full_name: str
    email: EmailStr
    created_at: datetime


class ProductCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=200,
    )

    description: str | None = None

    price: Decimal = Field(
        ge=0,
    )

    stock_quantity: int = Field(
        ge=0,
    )


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str | None
    price: Decimal
    stock_quantity: int
    created_at: datetime


class InventoryUpdate(BaseModel):
    stock_quantity: int = Field(
        ge=0,
    )


class OrderItemCreate(BaseModel):
    product_id: int

    quantity: int = Field(
        gt=0,
    )


class OrderCreate(BaseModel):
    user_id: int
    # total_amount: Decimal
    items: list[OrderItemCreate] = Field(
        min_length=1,
    )


class OrderItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    quantity: int
    unit_price: Decimal
    item_total: Decimal


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    status: str
    created_at: datetime

    # Calculated:
    # SUM(quantity * unit_price)
    total_amount: Decimal

    items: list[OrderItemResponse]
