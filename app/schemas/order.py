
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


ServiceType = Literal["regular", "express"]

OrderStatus = Literal[
    "pending",
    "washing",
    "drying",
    "ironing",
    "ready",
    "completed",
]


class OrderCreate(BaseModel):
    customer_name: str = Field(min_length=2, max_length=100)
    phone: str = Field(min_length=10, max_length=15)
    weight_kg: float = Field(gt=0, le=100)
    service_type: ServiceType = "regular"
    notes: str | None = Field(default=None, max_length=500)


class OrderStatusUpdate(BaseModel):
    status: OrderStatus


class OrderResponse(BaseModel):
    id: int
    customer_name: str
    phone: str
    weight_kg: float
    service_type: ServiceType
    price_per_kg: int
    total_price: int
    status: OrderStatus
    notes: str | None
    created_at: datetime
