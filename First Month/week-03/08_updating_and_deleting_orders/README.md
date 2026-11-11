## Question 01
How do update and delete routes work in REST APIs?

### Solution
Update routes change an existing record, and delete routes remove it. They should check whether the resource exists and return 404 if not found.

### Example
`PUT /orders/3` updates order 3 and `DELETE /orders/3` removes it.

### Expected Output
`200 OK` for updates and `200 OK` or `204 No Content` for deletes.
