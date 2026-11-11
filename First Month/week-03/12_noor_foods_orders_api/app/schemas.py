from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class OrderBase(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=100)
    item: str = Field(..., min_length=2, max_length=150)
    quantity: int = Field(default=1, ge=1)
    total: float = Field(..., ge=0)
    status: str = Field(default="pending")

    @field_validator("customer_name", "item", "status")
    @classmethod
    def normalize_text(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("value cannot be empty")
        return cleaned

    @field_validator("status")
    @classmethod
    def validate_status(cls, value: str) -> str:
        valid_statuses = {"pending", "processing", "delivered", "cancelled"}
        normalized = value.strip().lower()
        if normalized not in valid_statuses:
            raise ValueError("status must be one of: pending, processing, delivered, cancelled")
        return normalized


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass


class OrderRead(OrderBase):
    id: int
    created_at: datetime


class SummaryResponse(BaseModel):
    total_orders: int
    total_revenue: float
    average_order_value: float
    customers_served: int
