from __future__ import annotations

from datetime import UTC, datetime

from sqlmodel import Field, SQLModel


class Order(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_name: str = Field(index=True, nullable=False)
    item: str = Field(index=True, nullable=False)
    quantity: int = Field(default=1, nullable=False, ge=1)
    total: float = Field(default=0.0, nullable=False, ge=0)
    status: str = Field(default="pending", nullable=False, index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC), nullable=False)
