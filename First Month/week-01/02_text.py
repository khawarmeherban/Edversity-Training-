"""Practice set 2: working with text."""

# Question: Remove the extra spaces from the name, capitalize it correctly,
# and print the cleaned name and its character count.
# Solution:
print("Problem 1: Clean up a name")
raw_name = " aMNA rAZA "
name = raw_name.strip().title()
print(f"Welcome, {name}! Your name has {len(name)} characters.")
assert name == "Amna Raza" and len(name) == 9

# Question: Remove the extra spaces from the email, convert it to lowercase,
# and print the cleaned email and its character count.
# Solution:
print("\nProblem 2: Clean an email")
raw_email = " Ali.Khan@GMAIL.com "
email = raw_email.strip().lower()
print(f"Email: {email} ({len(email)} characters)")
assert email == "ali.khan@gmail.com" and len(email) == 18

# Question: Clean up the item name and print a receipt line for three items
# priced at Rs 2,499 each, including the total.
# Solution:
print("\nProblem 3: A receipt line")
item_name = " wireless MOUSE "
price = 2499
quantity = 3
receipt_total = price * quantity
print(f"{item_name.strip().title()} x{quantity} = Rs {receipt_total:,}")
assert receipt_total == 7497

# Question: Remove the extra spaces and hyphens from the order code, convert
# it to uppercase, and print the result and its character count.
# Solution:
print("\nProblem 4: Order codes")
raw_code = " ord-2024-0042 "
order_code = raw_code.strip().replace("-", "").upper()
print(f"Order {order_code} has {len(order_code)} characters")
assert order_code == "ORD20240042" and len(order_code) == 11

# Question: Build a lowercase username from the cleaned first and last names
# and the first three letters of the city; print it and a formatted greeting.
# Solution:
print("\nProblem 5: Usernames")
first = " bilal "
last = "QURESHI "
city = "lahore"
username = f"{first.strip().lower()}.{last.strip().lower()}_{city.strip().lower()[:3]}"
print(f"Welcome, {first.strip().title()} {last.strip().title()} from {city.strip().title()}!")
print(f"Your username is {username} ({len(username)} characters).")
assert username == "bilal.qureshi_lah" and len(username) == 17
