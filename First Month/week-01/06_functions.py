"""Practice set 6: writing your own functions."""

print("Problem 1: Formatting rupees")
def format_rupees(amount):
    return f"Rs {amount:,.0f}"

for amount in (12800, 999, 1250000):
    print(format_rupees(amount))
noor_total = 12800 - 12800 * 0.10
print(f"Noor Foods owes {format_rupees(noor_total)}")
assert [format_rupees(amount) for amount in (12800, 999, 1250000)] == [
    "Rs 12,800", "Rs 999", "Rs 1,250,000"
]

print("\nProblem 2: Return or print?")
def add_tax(subtotal, rate=0.18):
    return subtotal * (1 + rate)

def add_tax_and_print(subtotal, rate=0.18):
    print(f"Printed from function: {subtotal * (1 + rate)}")

print(f"Default tax: {add_tax(7200)}")
print(f"Custom tax: {add_tax(7200, 0.05)}")
print_only_result = add_tax_and_print(7200)
print(f"The print-only function returned: {print_only_result}")
assert add_tax(7200) == 8496.0
assert add_tax(7200, 0.05) == 7560.0
assert print_only_result is None

print("\nProblem 3: Shipping as a function")
def shipping_charge(weight_kg, city, order_total=None):
    clean_city = city.strip().title()
    if order_total is not None and order_total > 10000:
        return 0
    if clean_city in ("Karachi", "Lahore", "Islamabad"):
        charge = 200
    else:
        charge = 350
    if weight_kg > 5:
        charge *= 2
    return charge

shipping_cases = [
    (5, " karachi ", 5000),
    (5.01, "Lahore", 5000),
    (5, "Multan", 5000),
    (6, "Multan", 5000),
    (6, "Karachi", 12000),
]
for weight, city, order_total in shipping_cases:
    print(f"Shipping to {city.strip().title()}: {format_rupees(shipping_charge(weight, city, order_total))}")
assert [shipping_charge(*case) for case in shipping_cases] == [200, 400, 350, 700, 0]

print("\nProblem 4: Totals by status")
def total_by_status(orders, status):
    result = 0
    for order in orders:
        if order["status"] == status:
            result += order["total"]
    return result

orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"},
]
for status in ("delivered", "pending", "cancelled"):
    print(f"{status}: Rs {total_by_status(orders, status):,}")
assert total_by_status(orders, "delivered") == 6800
assert total_by_status(orders, "pending") == 12800
assert total_by_status(orders, "cancelled") == 0

print("\nProblem 5: Refactor the reorder report")
# Small functions separate the rules, so each can be tested or changed independently.
def needs_reorder(product):
    return product["stock"] < product["reorder_level"]

def reorder_quantity(product):
    if needs_reorder(product):
        return 2 * product["reorder_level"] - product["stock"]
    return 0

def reorder_cost(product):
    return reorder_quantity(product) * product["unit_cost"]

inventory = [
    {"name": "Notebook", "stock": 8, "reorder_level": 15, "unit_cost": 90},
    {"name": "Pen", "stock": 140, "reorder_level": 50, "unit_cost": 25},
    {"name": "Stapler", "stock": 2, "reorder_level": 5, "unit_cost": 650},
    {"name": "Marker", "stock": 30, "reorder_level": 30, "unit_cost": 120},
    {"name": "Folder", "stock": 11, "reorder_level": 20, "unit_cost": 60},
]
reorder_total = 0
reorder_count = 0
for product in inventory:
    if needs_reorder(product):
        quantity = reorder_quantity(product)
        cost = reorder_cost(product)
        reorder_total += cost
        reorder_count += 1
        print(f"Reorder {quantity} x {product['name']} ({format_rupees(cost)})")
if reorder_count == 0:
    print("All stock OK")
print(f"Total cost: {format_rupees(reorder_total)}")
assert reorder_total == 8920
assert needs_reorder(inventory[0]) is True
assert needs_reorder(inventory[1]) is False
