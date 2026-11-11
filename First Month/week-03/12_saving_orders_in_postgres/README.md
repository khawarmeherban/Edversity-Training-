## Question 01
How do we save an order in a database?

### Solution
We insert each order into a database table with a customer name, item, quantity, total, and status. This gives us persistence and query support.

### Example
```sql
INSERT INTO orders (customer_name, item, quantity, total, status)
VALUES ('Noor Foods', 'Rice', 2, 520, 'pending');
```

### Expected Output
A row is created and can be returned later with `SELECT`.
