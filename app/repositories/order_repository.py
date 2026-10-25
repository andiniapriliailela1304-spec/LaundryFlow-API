
from app.models.order import Order


class OrderRepository:
    def __init__(self):
        self._orders: dict[int, Order] = {}
        self._next_id = 1

    def create(self, order: Order) -> Order:
        order.id = self._next_id
        self._orders[order.id] = order
        self._next_id += 1
        return order

    def get_all(self) -> list[Order]:
        return list(self._orders.values())

    def get_by_id(self, order_id: int) -> Order | None:
        return self._orders.get(order_id)

    def update_status(
        self, order_id: int, status: str
    ) -> Order | None:
        order = self.get_by_id(order_id)

        if order is None:
            return None

        order.status = status
        return order

    def delete(self, order_id: int) -> bool:
        return self._orders.pop(order_id, None) is not None
