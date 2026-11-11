## Question 01
What is PostgreSQL and why is it used with APIs?

### Solution
PostgreSQL is a relational database used to save application data in a structured way. APIs often combine a web app with a database so data persists beyond a single process.

### Example
A table called `orders` stores each order with customer, item, quantity, and total.

### Expected Output
Rows of data can be queried with SQL such as `SELECT * FROM orders;`.
