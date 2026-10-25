
from datetime import datetime

from app.core.config import PRICE_PER_KG
from app.models.order import Order
from app.repositories.order_repository import OrderRepository
from app.schemas.order import OrderCreate, OrderStatus


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create_order(self, data: OrderCreate) -> Order:
        price = PRICE_PER_KG[data.service_type]

        order = Order(
            id=0,
            customer_name=data.customer_name,
            phone=data.phone,
            weight_kg=data.weight_kg,
            service_type=data.service_type,
            price_per_kg=price,
            total_price=round(data.weight_kg * price),
            status="pending",
            notes=data.notes,
            created_at=datetime.now(),
        )

        return self.repository.create(order)

    def get_orders(self) -> list[Order]:
        return self.repository.get_all()

    def get_order(self, order_id: int) -> Order | None:
        return self.repository.get_by_id(order_id)

    def update_status(
        self, order_id: int, status: OrderStatus
    ) -> Order | None:
        return self.repository.update_status(order_id, status)

    def delete_order(self, order_id: int) -> bool:
        return self.repository.delete(order_id)
