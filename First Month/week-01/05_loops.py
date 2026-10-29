"""Practice set 5: repeating work with loops."""

orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"},
]

print("Problem 1: Delivered revenue")
delivered_revenue = 0
for order in orders:
    if order["status"] == "delivered":
        delivered_revenue += order["total"]
print(f"Delivered revenue: Rs {delivered_revenue:,}")
assert delivered_revenue == 6800

print("\nProblem 2: Numbered items")
prices = [850, 1200, 400, 3100, 650]
item_number = 0
total = 0
over_1000_count = 0
for price in prices:
    item_number += 1
    total += price
    if price > 1000:
        over_1000_count += 1
    print(f"Item {item_number}: Rs {price:,}")
print(f"Total: Rs {total:,}")
print(f"Items over Rs 1,000: {over_1000_count}")
assert total == 6200 and over_1000_count == 2

print("\nProblem 3: The biggest order")
# Start with the first order; using > keeps the first order when highest totals tie.
biggest_order = orders[0]
for order in orders[1:]:
    if order["total"] > biggest_order["total"]:
        biggest_order = order
print(f"Biggest order: {biggest_order['id']} (Rs {biggest_order['total']:,})")
tie_orders = [{"id": "A201", "total": 5000}, {"id": "A202", "total": 5000}]
biggest_tie = tie_orders[0]
for order in tie_orders[1:]:
    if order["total"] > biggest_tie["total"]:
        biggest_tie = order
print(f"If totals tie, this version keeps the first: {biggest_tie['id']}")
assert biggest_order["id"] == "A102" and biggest_tie["id"] == "A201"

print("\nProblem 4: Totals per customer")
customer_orders = [
    {"customer": "Noor Foods", "total": 4500},
    {"customer": "Karachi Crafts", "total": 12800},
    {"customer": "Noor Foods", "total": 2300},
    {"customer": "Bilal Traders", "total": 7600},
    {"customer": "Karachi Crafts", "total": 3900},
    {"customer": "Noor Foods", "total": 6100},
]
totals_by_customer = {}
for order in customer_orders:
    customer = order["customer"]
    if customer not in totals_by_customer:
        totals_by_customer[customer] = 0
    totals_by_customer[customer] += order["total"]
for customer, customer_total in totals_by_customer.items():
    print(f"{customer}: Rs {customer_total:,}")
assert totals_by_customer == {
    "Noor Foods": 12900,
    "Karachi Crafts": 16700,
    "Bilal Traders": 7600,
}

print("\nProblem 5: Reorder report")
# Plan: find low-stock items, order enough to reach twice the reorder level, and total the cost.
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
    if product["stock"] < product["reorder_level"]:
        quantity = 2 * product["reorder_level"] - product["stock"]
        line_cost = quantity * product["unit_cost"]
        reorder_total += line_cost
        reorder_count += 1
        print(f"Reorder {quantity} x {product['name']} (Rs {line_cost:,})")
if reorder_count == 0:
    print("All stock OK")
print(f"Total cost: Rs {reorder_total:,}")
assert reorder_total == 8920

# Raise every stock level and confirm that no product appears on the reorder report.
for product in inventory:
    product["stock"] = 2 * product["reorder_level"]
raised_stock_reorders = 0
for product in inventory:
    if product["stock"] < product["reorder_level"]:
        raised_stock_reorders += 1
if raised_stock_reorders == 0:
    print("Raised-stock test: All stock OK")
assert raised_stock_reorders == 0
