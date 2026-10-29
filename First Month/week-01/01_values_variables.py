"""Practice set 1: values, variables and types."""

print("Problem 1: Delivery charge")
customer = "Karachi Crafts"
lamp_count = 3
lamp_price = 2400
delivery_charge = 350
order_total = lamp_count * lamp_price + delivery_charge
print(f"{customer}: Rs {order_total}")
print(type(order_total))
assert order_total == 7550

print("\nProblem 2: Sales tax")
subtotal = 7200
tax_rate = 0.18
tax_amount = subtotal * tax_rate
total_with_tax = subtotal + tax_amount
print(f"Tax: Rs {tax_amount}; total: Rs {total_with_tax}")
print(type(tax_amount))
print("The percentage is a float, so the tax amount is a float too.")
assert (tax_amount, total_with_tax) == (1296.0, 8496.0)

print("\nProblem 3: Splitting a bill")
dinner_total = 4750
friends = 4
print(f"Each share: Rs {dinner_total / friends}")
print(f"Whole rupees each: Rs {dinner_total // friends}")
print(f"Rupees left over: Rs {dinner_total % friends}")
assert (dinner_total // friends, dinner_total % friends) == (1187, 2)

print("\nProblem 4: Discount and tax")
phone_price = 15000
discount_rate = 0.10
tax_rate = 0.18
discount_then_tax = phone_price * (1 - discount_rate) * (1 + tax_rate)
tax_then_discount = phone_price * (1 + tax_rate) * (1 - discount_rate)
print(f"Discount then tax: Rs {discount_then_tax:,.2f}")
print(f"Tax then discount: Rs {tax_then_discount:,.2f}")
# Multiplication by the discount and tax factors commutes, so the order does not change the result.
assert discount_then_tax == tax_then_discount == 15930.0

print("\nProblem 5: Packing boxes")
items = 23
capacity = 6
full_boxes = items // capacity
left_over = items % capacity
boxes_needed = (items + capacity - 1) // capacity
shipping_cost = boxes_needed * 120
print(f"Full boxes: {full_boxes}; left over: {left_over}; total boxes: {boxes_needed}")
print(f"Shipping: Rs {shipping_cost}")
assert (full_boxes, left_over, boxes_needed, shipping_cost) == (3, 5, 4, 480)
exact_items = 24
exact_boxes = (exact_items + capacity - 1) // capacity
print(f"For 24 items, boxes needed: {exact_boxes}")
assert exact_boxes == 4
