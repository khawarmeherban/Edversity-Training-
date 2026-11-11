## Question 01
What is Bruno and why do we use it for API testing?

### Solution
Bruno is an API client that lets you create requests, save environments, and reuse collections. It is helpful for testing endpoints before writing full application code.

### Example
A request can be saved as `GET /orders` and run against `localhost:8000`.

### Expected Output
A successful response with JSON data or a 404/500 error that points to the bug.
