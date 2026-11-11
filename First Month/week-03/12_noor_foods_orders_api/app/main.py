from __future__ import annotations

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, func, select

from app.database import get_session, init_db
from app.models import Order
from app.schemas import OrderCreate, OrderRead, OrderUpdate, SummaryResponse

app = FastAPI(title="Noor Foods Orders API", version="1.0.0")


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "Noor Foods Orders API"}


@app.get("/orders", response_model=list[OrderRead])
def get_orders(
    *,
    customer: str | None = None,
    status: str | None = Query(default=None),
    min_total: float | None = Query(default=None, ge=0),
    session: Session = Depends(get_session),
) -> list[Order]:
    statement = select(Order)

    if customer:
        customer_name = customer.strip().lower()
        statement = statement.where(func.lower(Order.customer_name) == customer_name)

    if status:
        normalized_status = status.strip().lower()
        valid_statuses = {"pending", "processing", "delivered", "cancelled"}
        if normalized_status not in valid_statuses:
            raise HTTPException(
                status_code=400,
                detail="status must be one of: pending, processing, delivered, cancelled",
            )
        statement = statement.where(func.lower(Order.status) == normalized_status)

    if min_total is not None:
        statement = statement.where(Order.total >= min_total)

    statement = statement.order_by(Order.id)
    return session.exec(statement).all()


@app.get("/customers/{name}/orders", response_model=list[OrderRead])
def get_customer_orders(
    *,
    name: str,
    session: Session = Depends(get_session),
) -> list[Order]:
    normalized_name = name.strip().lower()
    statement = select(Order).where(func.lower(Order.customer_name) == normalized_name).order_by(Order.id)
    return session.exec(statement).all()


@app.get("/summary", response_model=SummaryResponse)
def get_summary(session: Session = Depends(get_session)) -> SummaryResponse:
    total_orders = session.exec(select(func.count(Order.id))).one()
    total_revenue = session.exec(select(func.coalesce(func.sum(Order.total), 0.0))).one()
    average_order_value = session.exec(select(func.coalesce(func.avg(Order.total), 0.0))).one()
    customers_served = session.exec(select(func.count(func.distinct(Order.customer_name)))).one()

    return SummaryResponse(
        total_orders=int(total_orders or 0),
        total_revenue=round(float(total_revenue or 0), 2),
        average_order_value=round(float(average_order_value or 0), 2),
        customers_served=int(customers_served or 0),
    )


@app.post("/orders", response_model=OrderRead, status_code=201)
def create_order(order: OrderCreate, session: Session = Depends(get_session)) -> Order:
    item = Order(**order.model_dump())
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@app.put("/orders/{order_id}", response_model=OrderRead)
def update_order(
    *,
    order_id: int,
    order_update: OrderUpdate,
    session: Session = Depends(get_session),
) -> Order:
    order = session.get(Order, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    for key, value in order_update.model_dump(exclude_unset=True).items():
        setattr(order, key, value)

    session.add(order)
    session.commit()
    session.refresh(order)
    return order


@app.delete("/orders/{order_id}")
def delete_order(*, order_id: int, session: Session = Depends(get_session)) -> dict[str, str | int]:
    order = session.get(Order, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    session.delete(order)
    session.commit()
    return {"message": "Order deleted successfully", "id": order_id}
