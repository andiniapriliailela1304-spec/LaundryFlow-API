
from fastapi import FastAPI

from app.api.orders import router as orders_router
from app.core.config import (
    APP_DESCRIPTION,
    APP_NAME,
    APP_VERSION,
)
from app.repositories.order_repository import OrderRepository
from app.services.order_service import OrderService


def create_app() -> FastAPI:
    app = FastAPI(
        title=APP_NAME,
        description=APP_DESCRIPTION,
        version=APP_VERSION,
    )

    app.state.order_service = OrderService(OrderRepository())
    app.include_router(orders_router)

    @app.get("/", tags=["Health"])
    def root():
        return {
            "message": f"{APP_NAME} aktif",
            "status": "success",
        }

    return app


app = create_app()
