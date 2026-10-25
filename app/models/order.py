
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    id: int
    customer_name: str
    phone: str
    weight_kg: float
    service_type: str
    price_per_kg: int
    total_price: int
    status: str = "pending"
    notes: str | None = None
    created_at: datetime | None = None
