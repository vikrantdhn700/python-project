from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Text,
    Numeric,
    DateTime,
    ForeignKey,
    CheckConstraint,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        BigInteger,
        primary_key=True,
        index=True,
    )

    email = Column(
        String,
        nullable=False,
        unique=True,
    )

    full_name = Column(
        String,
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    # One user can have many orders
    orders = relationship(
        "Order",
        back_populates="user",
    )


# -------------------------
# Product
# -------------------------

class Product(Base):
    __tablename__ = "products"

    id = Column(
        BigInteger,
        primary_key=True,
        index=True,
    )

    name = Column(
        String,
        nullable=False,
    )

    description = Column(
        Text,
        nullable=True,
    )

    price = Column(
        Numeric(12, 2),
        nullable=False,
    )

    stock_quantity = Column(
        BigInteger,
        nullable=False,
        default=0,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    # One product can appear in many order items
    order_items = relationship(
        "OrderItem",
        back_populates="product",
    )

    __table_args__ = (
        CheckConstraint(
            "price >= 0",
            name="products_price_check",
        ),
        CheckConstraint(
            "stock_quantity >= 0",
            name="products_stock_quantity_check",
        ),
    )


# -------------------------
# Order
# -------------------------

class Order(Base):
    __tablename__ = "orders"

    id = Column(
        BigInteger,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        BigInteger,
        ForeignKey(
            "users.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )

    status = Column(
        String(20),
        nullable=False,
        default="pending",
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    total_amount = Column(
        Numeric(12, 2),
        nullable=False,
        default=0.00
    )

    # Many orders belong to one user
    user = relationship(
        "User",
        back_populates="orders",
    )

    # One order can contain many order items
    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'paid', 'shipped', 'completed', 'cancelled')",
            name="orders_status_check",
        ),
    )


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(
        BigInteger,
        primary_key=True,
        index=True,
    )

    order_id = Column(
        BigInteger,
        ForeignKey(
            "orders.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    product_id = Column(
        BigInteger,
        ForeignKey(
            "products.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )

    quantity = Column(
        BigInteger,
        nullable=False,
    )

    unit_price = Column(
        Numeric(12, 2),
        nullable=False,
    )

    item_total = Column(
        Numeric(12, 2),
        nullable=False,
        default=0.00
    )

    # Relationship with Order
    order = relationship(
        "Order",
        back_populates="items",
    )

    # Relationship with Product
    product = relationship(
        "Product",
        back_populates="order_items",
    )

    __table_args__ = (
        CheckConstraint(
            "quantity > 0",
            name="order_items_quantity_check",
        ),
        CheckConstraint(
            "unit_price >= 0",
            name="order_items_unit_price_check",
        ),
        UniqueConstraint(
            "order_id",
            "product_id",
            name="order_items_order_product_unique",
        ),
    )
