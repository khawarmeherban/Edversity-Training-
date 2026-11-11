## Question 01
What are the main HTTP methods used in APIs?

### Solution
GET is used to read data, POST creates data, PUT updates data, and DELETE removes data. Each method tells the server what action to perform.

### Example
A client can call GET /orders to list orders and POST /orders to create an order.

### Expected Output
`200 OK` for a successful GET and `201 Created` for a successful POST.
