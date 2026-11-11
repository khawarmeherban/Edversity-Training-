## Question 01
What does it mean to go live with a database?

### Solution
Going live means moving the app and database into a real environment where the service is reachable, monitored, and backed by persistent storage. We keep the connection string and environment variables secure.

### Example
Set `DATABASE_URL=postgresql://user:password@host:5432/noor_foods` before running the app.

### Expected Output
The app connects and serves requests successfully.
