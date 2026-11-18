from fastapi import FastAPI, HTTPException, Query, Response, status

from products_api.models import Category, NewProduct, Product, ProductUpdate, SummaryResponse

app = FastAPI(title="Noor Foods Products API")

initial_products: dict[str, Product] = {
    "P101": Product(
        id="P101",
        name="Basmati rice 5kg",
        price=2400,
        category=Category.RICE,
        in_stock=40,
    ),
    "P102": Product(
        id="P102",
        name="Cooking oil 1L",
        price=650,
        category=Category.OIL,
        in_stock=0,
    ),
    "P103": Product(
        id="P103",
        name="Red chilli powder 200g",
        price=320,
        category=Category.SPICES,
        in_stock=120,
    ),
    "P104": Product(
        id="P104",
        name="Sella rice 10kg",
        price=4600,
        category=Category.RICE,
        in_stock=15,
    ),
}
products = initial_products.copy()
next_product_number = 105


def find_product(product_id: str) -> Product:
    product = products.get(product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_id} not found",
        )
    return product


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/products", response_model=list[Product])
def list_products(
    category: Category | None = None,
    max_price: int | None = Query(default=None, ge=0),
    limit: int = Query(default=10, ge=1),
) -> list[Product]:
    matching_products = [
        product
        for product in products.values()
        if (category is None or product.category == category)
        and (max_price is None or product.price <= max_price)
    ]
    return matching_products[:limit]


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str) -> Product:
    return find_product(product_id)


@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(new_product: NewProduct) -> Product:
    global next_product_number

    product_id = f"P{next_product_number}"
    next_product_number += 1
    product = Product(id=product_id, **new_product.model_dump())
    products[product_id] = product
    return product


@app.patch("/products/{product_id}", response_model=Product)
def update_product(product_id: str, changes: ProductUpdate) -> Product:
    product = find_product(product_id)
    updated_data = product.model_dump() | changes.model_dump(exclude_unset=True)
    updated_product = Product.model_validate(updated_data)
    products[product_id] = updated_product
    return updated_product


@app.delete(
    "/products/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
)
def delete_product(product_id: str) -> Response:
    product = find_product(product_id)
    if product.in_stock > 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Cannot delete product {product_id} while {product.in_stock} are in stock",
        )

    del products[product_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get("/summary", response_model=SummaryResponse)
def get_summary() -> SummaryResponse:
    category_counts: dict[str, int] = {}
    stock_value = 0

    for product in products.values():
        category_name = product.category.value
        category_counts[category_name] = category_counts.get(category_name, 0) + 1
        stock_value += product.price * product.in_stock

    return SummaryResponse(
        product_count=len(products),
        stock_value=stock_value,
        by_category=category_counts,
    )
