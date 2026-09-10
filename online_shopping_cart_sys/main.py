products = {
    "Laptop": 65000,
    "Phone": 25000,
    "Mouse": 800,
    "Keyboard": 1200,
    "Monitor": 9000,
    "Speaker": 2500
}

cart = {}
print("Welcome to the Shopping Cart!")
print("\nAvailable products:")
print("-------------------")
for product, price in products.items():
    print(f"{product}: ₹{price:.2f}")

print("\nPlease enter the products you want to add to your cart.")
while True:
    product_name = input(
        "Enter product name (or type done for finished): ").title()
    if product_name == "Done":
        break
    elif product_name in products:
        qty = int(input(f"Enter quantity for {product_name}: "))
        if product_name in cart:
            cart[product_name] += qty
        else:
            cart[product_name] = qty
    else:
        print("Invalid product. Please try again.")

print("\n")
print("=" * 60)
print(" " * 22 + "INVOICE")
print("=" * 60)
print(f"{'Item':15}{'Quantity':15}{'Price':15}{'Total':15}")
print("-" * 60)
subtotal = 0
for product, qty in cart.items():
    price = products[product]
    total_price = float(f"{price * qty:.2f}")
    subtotal += total_price
    print(f"{product:15}{qty:10}₹{price:10.2f}₹{total_price:.2f}")

if subtotal > 10000:
    discount_percent = 5
elif subtotal > 30000:
    discount_percent = 10
elif subtotal > 60000:
    discount_percent = 15

discount = subtotal * (discount_percent / 100)
cart_total = subtotal - discount

print("-" * 60)
print(f"{'Subtotal':35} ₹{subtotal:.2f}")
print(f"{'Discount (' + str(discount_percent) + '%)':35} -₹{discount:.2f}")
print(f"{'Final Amount':35} ₹{cart_total:.2f}")
print("=" * 60)
