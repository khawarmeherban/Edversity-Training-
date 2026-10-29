# Week 1: Part 1

Solutions for the first week of Edversity's Python training, including six exercise sets and the daily order-checker task.

## Exercise files

1. `01_values_variables.py` - values, variables and types
2. `02_text.py` - strings and formatting
3. `03_lists_dictionaries.py` - lists and dictionaries
4. `04_conditionals.py` - `if` decisions
5. `05_loops.py` - loops and accumulating totals
6. `06_functions.py` - functions and return values
7. `daily_task.py` - the order checker

Each practice-set script contains its five exercises in lesson order. Run one file at a time to work through it step by step. Assertions check the stated expected results and key edge cases.

## Questions matched to the solutions

### `01_values_variables.py`

1. Calculate the total for three lamps at Rs 2,400 each, plus a Rs 350 delivery charge. What is the type of the total?
2. Calculate 18% sales tax on a Rs 7,200 subtotal and find the total including tax. What is the type of the tax amount?
3. Split Rs 4,750 among four friends. Find each whole-rupee share and the amount left over.
4. Apply a 10% discount and 18% tax to a Rs 15,000 phone. Does applying the discount before the tax change the result?
5. Pack 23 items into boxes that hold six each. Find the full boxes, leftover items, boxes needed, and shipping cost at Rs 120 per box.

### `02_text.py`

1. Remove extra spaces from `" aMNA rAZA "`, format it as a name, and report its character count.
2. Clean `" Ali.Khan@GMAIL.com "` into a lowercase email address and report its character count.
3. Format a receipt line for three `" wireless MOUSE "` items priced at Rs 2,499 each.
4. Clean `" ord-2024-0042 "` into an uppercase order code without hyphens, then report its character count.
5. Create a username from the cleaned first name, last name, and first three letters of the city; also print a greeting.

### `03_lists_dictionaries.py`

1. Find the last price and sum in a price list, then update a product's stock status.
2. Use a week's sales data to find Monday and Sunday sales, the weekly total and average, and the best and worst sales days.
3. Update notebook stock, add markers to the stock dictionary, and report the number of products.
4. Look up a customer in an order list, reduce an order total, add a new order, and report the first and last order IDs.
5. Read a city and order totals from a nested customer profile, calculate spending, add a new order total, and show a default when the phone number is missing.

### `04_conditionals.py`

1. Offer free delivery only for orders of at least Rs 5,000 placed in Lahore; otherwise show a Rs 350 delivery charge.
2. Assign grades: A for 80 or more, B for 65 or more, C for 50 or more, and Fail below 50.
3. Validate an order quantity against available stock and report invalid, unavailable, or confirmed orders.
4. Calculate shipping using the order total, destination city, and weight; normalize the city name before applying the rules.
5. Prioritize support tickets: urgent for enterprise tickets open over four hours, high for billing issues or pro tickets open over 24 hours, and normal otherwise.

### `05_loops.py`

1. Loop through orders and total the revenue from delivered orders only.
2. Number and print each item, then calculate the price total and count of items over Rs 1,000.
3. Find the biggest order, keeping the first order if totals are tied.
4. Accumulate and print order totals for each customer.
5. Find products below their reorder levels, calculate how many units are needed to reach twice the reorder level, and total the reorder cost.

### `06_functions.py`

1. Write a function to format amounts as rupees with thousands separators, then use it to display an amount owed after a discount.
2. Write one function that returns a tax-inclusive total and another that only prints it; compare their results and return values.
3. Write a shipping function that accounts for city, weight, and free shipping on orders over Rs 10,000.
4. Write a function that totals orders for a requested status.
5. Refactor the reorder calculation into functions that check reorder need, calculate quantity, and calculate cost.

### `daily_task.py`

Print each item priced over Rs 1,000 and calculate the total price of all four items.

## Run

From the workspace root in PowerShell, for example:

```powershell
python "First Month/week-01/live-session/01_values_variables.py"
```

Run another set by replacing the filename. To run the daily task:

```powershell
python "First Month/week-01/live-session/daily_task.py"
```

Python 3.13 works with these files; no extra packages are needed.
