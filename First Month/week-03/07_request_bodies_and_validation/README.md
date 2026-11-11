## Question 01
Why do we validate request bodies in APIs?

### Solution
Validation prevents invalid data such as empty customer names, negative totals, or bad statuses. FastAPI and Pydantic help enforce this before the request is processed.

### Example
A POST request with `total=-30` should raise a validation error.

### Expected Output
`422 Unprocessable Entity`
