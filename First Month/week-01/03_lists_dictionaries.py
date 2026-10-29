"""Practice set 3: lists and dictionaries."""

print("Problem 1: A product record")
prices = [850, 1200, 400]
print(f"Last price: Rs {prices[-1]}")
print(f"Sum: Rs {sum(prices)}")
product = {"name": "Notebook", "price": 850, "in_stock": True}
product["in_stock"] = False
print(product["name"])
assert prices[-1] == 400 and sum(prices) == 2450 and product["in_stock"] is False

print("\nProblem 2: A week of sales")
daily_sales = [18500, 22300, 19800, 25400, 31200, 42800, 38600]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekly_total = sum(daily_sales)
print(f"Monday: Rs {daily_sales[0]:,}")
print(f"Sunday: Rs {daily_sales[-1]:,}")
print(f"Weekly total: Rs {weekly_total:,}")
print(f"Daily average: Rs {weekly_total / len(daily_sales):,.0f}")
best_sales = max(daily_sales)
worst_sales = min(daily_sales)
print(f"Best day: {days[daily_sales.index(best_sales)]} (Rs {best_sales:,})")
print(f"Worst day: {days[daily_sales.index(worst_sales)]} (Rs {worst_sales:,})")
assert weekly_total == 198600 and best_sales == 42800 and worst_sales == 18500

print("\nProblem 3: Stock levels")
stock = {"pens": 120, "notebooks": 45, "staplers": 8}
stock["notebooks"] -= 30
stock["markers"] = 60
print(f"Products: {len(stock)}")
print(stock)
assert stock["notebooks"] == 15 and len(stock) == 4

print("\nProblem 4: A list of orders")
orders = [
    {"id": "A101", "customer": "Noor Foods", "total": 4500},
    {"id": "A102", "customer": "Karachi Crafts", "total": 12800},
    {"id": "A103", "customer": "Bilal Traders", "total": 2300},
]
print(f"Second customer: {orders[1]['customer']}")
orders[2]["total"] -= 500
orders.append({"id": "A104", "customer": "Amna Store", "total": 6100})
print(f"{len(orders)} orders. The first is {orders[0]['id']} and the last is {orders[-1]['id']}.")
assert orders[2]["total"] == 1800 and len(orders) == 4

print("\nProblem 5: A customer profile")
customer = {
    "name": "Noor Foods",
    "address": {"city": "Karachi", "area": "Clifton"},
    "order_totals": [4500, 12800, 2300],
}
print(f"City: {customer['address']['city']}")
print(f"Orders: {len(customer['order_totals'])}")
print(f"Total spent: Rs {sum(customer['order_totals']):,}")
customer["order_totals"].append(6100)
print(f"New total: Rs {sum(customer['order_totals']):,}")
print(customer.get("phone", "No phone number"))
assert sum(customer["order_totals"]) == 25700
