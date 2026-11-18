from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints, model_validator

ProductName = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=2, max_length=80),
]
ProductPrice = Annotated[int, Field(gt=0)]
StockCount = Annotated[int, Field(ge=0)]


class Category(StrEnum):
    RICE = "rice"
    OIL = "oil"
    SPICES = "spices"
    FLOUR = "flour"


class NewProduct(BaseModel):
    name: ProductName
    price: ProductPrice
    category: Category
    in_stock: StockCount = 0


class Product(BaseModel):
    id: str
    name: ProductName
    price: ProductPrice
    category: Category
    in_stock: StockCount


class ProductUpdate(BaseModel):
    name: ProductName | None = None
    price: ProductPrice | None = None
    category: Category | None = None
    in_stock: StockCount | None = None

    @model_validator(mode="after")
    def reject_explicit_nulls(self) -> "ProductUpdate":
        for field_name in self.model_fields_set:
            if getattr(self, field_name) is None:
                raise ValueError(f"{field_name} cannot be null")
        return self


class SummaryResponse(BaseModel):
    product_count: int
    stock_value: int
    by_category: dict[str, int]
