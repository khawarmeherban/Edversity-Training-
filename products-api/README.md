# Noor Foods Products API

A small FastAPI service for Noor Foods' warehouse. It keeps products in memory, so changes reset to the four starting products whenever the server restarts.

## Run the API

From this directory:

```powershell
uv sync
uv run fastapi dev
```

The API is available at `http://127.0.0.1:8000`. Interactive API documentation is at `/docs`.

## Run the tests

```powershell
uv run pytest
```

The tests use an isolated copy of the starting products, so they do not depend on one another.

## Routes

| Method | Route | Description |
| --- | --- | --- |
| `GET` | `/health` | Health check |
| `GET` | `/products` | List products; optional `category`, `max_price`, and `limit` filters |
| `GET` | `/products/{product_id}` | Get one product |
| `POST` | `/products` | Create a product; new IDs are assigned in order |
| `PATCH` | `/products/{product_id}` | Update only the supplied fields |
| `DELETE` | `/products/{product_id}` | Delete a product only when its stock is zero |
| `GET` | `/summary` | Product count, stock value, and counts by category |

Product categories are `rice`, `oil`, `spices`, and `flour`. Names must be 2 to 80 characters, prices must be positive whole numbers, and stock counts must be zero or more.

## Bruno

The `bruno` directory contains the **Products API** collection, including the `Local` environment and requests for the routes and stock-conflict case.