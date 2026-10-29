"""Practice set 4: making decisions with if."""

print("Problem 1: Free delivery")

def delivery_message(total, city):
    if total >= 5000 and city == "Lahore":
        return "Free delivery"
    return "Delivery charge: Rs 350"

print(delivery_message(6200, "Lahore"))
assert delivery_message(5000, "Lahore") == "Free delivery"
assert delivery_message(4999, "Lahore") == "Delivery charge: Rs 350"
assert delivery_message(6200, "Karachi") == "Delivery charge: Rs 350"

print("\nProblem 2: Grades")
def grade_for(marks):
    if marks >= 80:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 50:
        return "C"
    return "Fail"

for marks in (80, 79, 50, 49):
    print(f"{marks}: {grade_for(marks)}")
assert [grade_for(mark) for mark in (80, 79, 50, 49)] == ["A", "B", "C", "Fail"]

print("\nProblem 3: Stock check")
def stock_message(stock, quantity):
    if quantity <= 0:
        return "Invalid quantity"
    elif quantity > stock:
        return f"Only {stock} left in stock"
    return f"Confirmed. {stock - quantity} left after this order"

stock = 12
print(stock_message(stock, 5))
assert stock_message(stock, 0) == "Invalid quantity"
assert stock_message(stock, 13) == "Only 12 left in stock"
assert stock_message(stock, 5) == "Confirmed. 7 left after this order"

print("\nProblem 4: Shipping rules")
def calculate_shipping(weight_kg, order_total, city):
    clean_city = city.strip().title()
    if order_total > 10000:
        charge = 0
    elif clean_city in ("Karachi", "Lahore", "Islamabad"):
        charge = 200 if weight_kg <= 5 else 400
    else:
        charge = 350 if weight_kg <= 5 else 700
    return clean_city, charge

shipping_cases = [
    (5, 5000, " karachi "),
    (5.01, 5000, "Lahore"),
    (5, 5000, "Multan"),
    (5.01, 5000, "Multan"),
    (6, 10001, "Peshawar"),
]
for weight, total, city in shipping_cases:
    clean_city, charge = calculate_shipping(weight, total, city)
    print(f"Shipping to {clean_city}: Rs {charge}")
assert [calculate_shipping(*case)[1] for case in shipping_cases] == [200, 400, 350, 700, 0]

print("\nProblem 5: Ticket triage")
def ticket_priority(plan, hours_open, message):
    clean_plan = plan.strip().lower()
    clean_message = message.lower()
    has_billing_issue = "refund" in clean_message or "charged twice" in clean_message
    # Urgent enterprise tickets come first, even if they also match a high-priority condition.
    if clean_plan == "enterprise" and hours_open > 4:
        return "Urgent"
    elif has_billing_issue or (clean_plan == "pro" and hours_open > 24):
        return "High"
    return "Normal"

cases = [
    ("enterprise", 6, "Login is broken", "Urgent"),
    ("free", 1, "I want a REFUND", "High"),
    ("pro", 30, "Dashboard is slow", "High"),
    ("enterprise", 2, "Question about invoices", "Normal"),
    ("enterprise", 6, "Please refund this", "Urgent"),
]
for plan, hours, message, expected in cases:
    actual = ticket_priority(plan, hours, message)
    print(f"{plan}, {hours} hours, {message!r}: {actual}")
    assert actual == expected
