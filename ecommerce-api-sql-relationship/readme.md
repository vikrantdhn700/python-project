# Mini E-Commerce API

A backend REST API for a mini e-commerce application built using **FastAPI**, **PostgreSQL (Neon)**, **SQLAlchemy**, and **Pydantic**.

The project demonstrates database relationships, CRUD operations, order processing, inventory management, SQL joins, filtering, grouping, sorting, and aggregate calculations.

---

## Tech Stack

- Python 3.11+
- FastAPI
- PostgreSQL
- Neon PostgreSQL
- SQLAlchemy
- Pydantic
- Pydantic EmailStr
- psycopg2
- Uvicorn
- python-dotenv

---

## Project Features

### Users

- Create a user account
- Store user name and email
- View user information
- Maintain a relationship between users and orders

### Products

- Create products
- View products
- Update product inventory
- Store product price and stock quantity
- Prevent negative prices and inventory

### Orders

- Create an order
- Add multiple products to an order
- Automatically use the current product price as the order item's `unit_price`
- Validate product availability
- Reduce product inventory when an order is placed
- View user orders
- Cancel an order

### Order Calculations

For every order item:

```text
Item Total = Quantity × Unit Price
```

For the complete order:

```text
Order Total = SUM(Item Total)
```

`item_total` and `total_amount` are calculated values. They are **not stored as database columns**.

---

# Database Structure

The application uses four PostgreSQL tables.

```text
users
  |
  | 1
  |
  | many
orders
  |
  | 1
  |
  | many
order_items
  |
  | many
  |
  | 1
products
```

## Tables

### users

| Column     | Type        | Description           |
| ---------- | ----------- | --------------------- |
| id         | BIGINT      | Primary key           |
| email      | TEXT        | Unique user email     |
| full_name  | TEXT        | User's full name      |
| created_at | TIMESTAMPTZ | Account creation time |

### products

| Column         | Type          | Description           |
| -------------- | ------------- | --------------------- |
| id             | BIGINT        | Primary key           |
| name           | TEXT          | Product name          |
| description    | TEXT          | Product description   |
| price          | NUMERIC(12,2) | Product price         |
| stock_quantity | INTEGER       | Available inventory   |
| created_at     | TIMESTAMPTZ   | Product creation time |

### orders

| Column     | Type        | Description          |
| ---------- | ----------- | -------------------- |
| id         | BIGINT      | Primary key          |
| user_id    | BIGINT      | Foreign key to users |
| status     | TEXT        | Order status         |
| created_at | TIMESTAMPTZ | Order creation time  |

Allowed order statuses:

```text
pending
paid
shipped
completed
cancelled
```

### order_items

| Column     | Type          | Description                 |
| ---------- | ------------- | --------------------------- |
| id         | BIGINT        | Primary key                 |
| order_id   | BIGINT        | Foreign key to orders       |
| product_id | BIGINT        | Foreign key to products     |
| quantity   | INTEGER       | Ordered quantity            |
| unit_price | NUMERIC(12,2) | Product price at order time |

The combination of:

```text
order_id + product_id
```

must be unique.

---

# Project Structure

```text
ecommerce-api-sql-relationship/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   └── routers/
│       ├── __init__.py
│       ├── users.py
│       ├── products.py
│       └── orders.py
│
├── .env
├── .gitignore
├── requirements.txt
├── schema.sql
└── README.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Move into the project:

```bash
cd ecommerce-api-sql-relationship
```

---

# 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

For PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

---

# 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
fastapi
uvicorn
sqlalchemy
psycopg2-binary
python-dotenv
pydantic
email-validator
```

---

# 4. Configure Neon PostgreSQL

Create a PostgreSQL database using Neon.

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://username:password@host/database?sslmode=require
```

Use your actual Neon connection string.

### Important

Never commit `.env` to GitHub.

Add this to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

# 5. Create Database Tables

The PostgreSQL database schema is available in:

```text
schema.sql
```

Run the SQL script against your Neon PostgreSQL database.

The schema creates:

```text
users
products
orders
order_items
```

with:

- Primary keys
- Foreign keys
- Unique constraints
- Check constraints
- Timestamps
- Indexes
- Relationships

---

# 6. Run the Application

Start FastAPI with Uvicorn:

```bash
python -m uvicorn app.main:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

---

# 7. API Documentation

FastAPI automatically provides Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Alternative ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# API Operations

## Users

### Create User

```http
POST /users
```

Example request:

```json
{
  "full_name": "Vikrant Kumar",
  "email": "vikrant@example.com"
}
```

---

## Products

### Create Product

```http
POST /products
```

Example:

```json
{
  "name": "Mechanical Keyboard",
  "description": "RGB mechanical keyboard",
  "price": 2499.0,
  "stock_quantity": 20
}
```

### View Products

```http
GET /products
```

### Update Inventory

```http
PATCH /products/{product_id}/inventory
```

Example:

```json
{
  "stock_quantity": 50
}
```

---

# Orders

## Create Order

```http
POST /orders
```

Example request:

```json
{
  "user_id": 1,
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 2,
      "quantity": 1
    }
  ]
}
```

The API obtains the current product price from the database.

For example:

```text
Product price = ₹799.50
Quantity = 2

Item Total
= 799.50 × 2
= ₹1599.00
```

The complete order total is calculated by adding all item totals.

---

# Order Calculation

The database stores:

```text
quantity
unit_price
```

It does not store:

```text
item_total
total_amount
```

Therefore:

```python
item_total = quantity * unit_price
```

and:

```python
order_total = sum(
    item.quantity * item.unit_price
    for item in order.items
)
```

This avoids storing duplicate calculated data.

---

# SQL Concepts Demonstrated

This project is designed to demonstrate important SQL operations.

## JOIN

Example:

```sql
SELECT
    o.id,
    u.full_name,
    o.status
FROM orders o
JOIN users u
    ON o.user_id = u.id;
```

This joins orders with their users.

---

## WHERE

Example:

```sql
SELECT *
FROM products
WHERE stock_quantity > 0;
```

---

## GROUP BY

Calculate total quantity sold for each product:

```sql
SELECT
    product_id,
    SUM(quantity) AS total_quantity
FROM order_items
GROUP BY product_id;
```

---

## ORDER BY

Display products by price:

```sql
SELECT *
FROM products
ORDER BY price DESC;
```

---

## Aggregate Functions

The project uses functions such as:

```sql
SUM()
COUNT()
```

Example:

```sql
SELECT
    o.id AS order_id,
    SUM(oi.quantity * oi.unit_price) AS order_total
FROM orders o
JOIN order_items oi
    ON o.id = oi.order_id
WHERE o.user_id = 1
GROUP BY o.id
ORDER BY o.created_at DESC;
```

This demonstrates:

```text
JOIN
WHERE
GROUP BY
ORDER BY
SUM()
```

---

# Product Sales Query

Example query to calculate product sales:

```sql
SELECT
    p.id,
    p.name,
    SUM(oi.quantity) AS total_quantity,
    SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM products p
JOIN order_items oi
    ON p.id = oi.product_id
JOIN orders o
    ON oi.order_id = o.id
WHERE o.status != 'cancelled'
GROUP BY p.id, p.name
ORDER BY SUM(oi.quantity) DESC;
```

This can be used for product sales reporting.

---

# Order Status

Orders can have one of the following statuses:

```text
pending
paid
shipped
completed
cancelled
```

Example:

```text
pending
   ↓
paid
   ↓
shipped
   ↓
completed
```

An order can also be cancelled according to the application's business rules.

---

# Inventory Management

When an order is placed, the application should verify that sufficient stock exists.

Example:

```text
Available stock = 10
Requested quantity = 3
```

After the order:

```text
Remaining stock = 7
```

If:

```text
Available stock = 2
Requested quantity = 5
```

the order should not be created because there is insufficient inventory.

---

# Database Relationships

## User → Orders

One user can have many orders.

```text
User
  |
  └── Order
  └── Order
  └── Order
```

Relationship:

```text
users.id
    ↓
orders.user_id
```

---

## Order → Order Items

One order can contain multiple order items.

```text
Order
  |
  ├── OrderItem
  ├── OrderItem
  └── OrderItem
```

Relationship:

```text
orders.id
    ↓
order_items.order_id
```

---

## Product → Order Items

One product can appear in many orders.

```text
Product
  |
  ├── OrderItem
  ├── OrderItem
  └── OrderItem
```

Relationship:

```text
products.id
    ↓
order_items.product_id
```

---

# Data Persistence

The application uses Neon PostgreSQL instead of temporary Python lists.

Therefore, data remains available after restarting the FastAPI server.

Example:

```text
Start API
    ↓
Create user
    ↓
Create product
    ↓
Create order
    ↓
Stop API
    ↓
Start API again
    ↓
Data still exists
```

---

# Validation

Pydantic is used to validate incoming API data.

Examples:

### User email

```python
email: EmailStr
```

### Product price

```python
price: Decimal = Field(ge=0)
```

### Product inventory

```python
stock_quantity: int = Field(ge=0)
```

### Order quantity

```python
quantity: int = Field(gt=0)
```

This prevents invalid data from entering the application.

---

# Security

Database credentials must be stored in environment variables.

Example:

```env
DATABASE_URL=postgresql://...
```

Do not write credentials directly inside Python files.

Do not commit:

```text
.env
```

to GitHub.

---

# Running Tests Manually

After starting the server, use Swagger:

```text
http://127.0.0.1:8000/docs
```

Recommended testing order:

```text
1. Create User
2. Create Product
3. View Products
4. Update Inventory
5. Create Order
6. View User Orders
7. Cancel Order
```

---

# Example Order Flow

```text
Create User
     ↓
Create Products
     ↓
Check Product Stock
     ↓
Create Order
     ↓
Check Inventory
     ↓
Get Product Price
     ↓
Create Order Items
     ↓
Reduce Inventory
     ↓
Calculate Item Totals
     ↓
Calculate Order Total
     ↓
Return Order Response
```

---

# Learning Objectives

This project demonstrates practical backend development concepts:

- FastAPI REST APIs
- PostgreSQL
- Neon PostgreSQL
- SQLAlchemy ORM
- Pydantic validation
- Environment variables
- Database relationships
- Primary keys
- Foreign keys
- Unique constraints
- Check constraints
- JOIN
- WHERE
- GROUP BY
- ORDER BY
- SUM
- COUNT
- Inventory management
- Order processing
- Database transactions
- API response models
- Data persistence

---

## License

This project is created for learning and demonstration purposes.
