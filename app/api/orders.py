
from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.schemas.order import (
    OrderCreate,
    OrderResponse,
    OrderStatusUpdate,
)
from app.services.order_service import OrderService

router = APIRouter(prefix="/api/orders", tags=["Orders"])


def get_order_service(request: Request) -> OrderService:
    return request.app.state.order_service


@router.post(
    "",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_order(
    data: OrderCreate,
    service: OrderService = Depends(get_order_service),
):
    return service.create_order(data)


@router.get("", response_model=list[OrderResponse])
def get_orders(
    service: OrderService = Depends(get_order_service),
):
    return service.get_orders()


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    service: OrderService = Depends(get_order_service),
):
    order = service.get_order(order_id)

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Pesanan tidak ditemukan",
        )

    return order


@router.patch(
    "/{order_id}/status",
    response_model=OrderResponse,
)
def update_order_status(
    order_id: int,
    data: OrderStatusUpdate,
    service: OrderService = Depends(get_order_service),
):
    order = service.update_status(order_id, data.status)

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Pesanan tidak ditemukan",
        )

    return order


@router.delete(
    "/{order_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_order(
    order_id: int,
    service: OrderService = Depends(get_order_service),
):
    if not service.delete_order(order_id):
        raise HTTPException(
            status_code=404,
            detail="Pesanan tidak ditemukan",
        )

    return None
