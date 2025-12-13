import uvicorn
from uuid import uuid4
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger

from app.routers import categories, products, users, reviews, cart, orders
from app.config import MEDIA_ROOT

logger.add(
    "info.log",
    format="Log: [{extra[log_id]}:{time} - {level} - {message}]",
    level="INFO",
    enqueue = True
)

app = FastAPI(
    title="FastAPI Интернет-магазин",
    version="0.1.0",
)
app.mount(
    "/media",
    StaticFiles(directory=MEDIA_ROOT),
    name="media"
)

@app.middleware("http")
async def log_middleware(request: Request, call_next):
    log_id = str(uuid4())
    with logger.contextualize(log_id=log_id):
        try:
            response = await call_next(request)
            if response.status_code in [
                status.HTTP_400_BAD_REQUEST,
                status.HTTP_402_PAYMENT_REQUIRED,
                status.HTTP_403_FORBIDDEN,
                status.HTTP_404_NOT_FOUND
            ]:
                logger.warning(f"Request to {request.url.path} failed")
            else:
                logger.info('Successfully accessed ' + request.url.path)
        except Exception as ex:
            logger.error(f"Request to {request.url.path} failed: {ex}")
            response = JSONResponse(
                content={"success": False},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return response

app.include_router(categories.router)
app.include_router(products.router)
app.include_router(users.router)
app.include_router(reviews.router)
app.include_router(cart.router)
app.include_router(orders.router)


@app.get("/")
async def root():
    """
    Корневой маршрут, подтверждающий, что API работает.
    """
    return {"message": "Добро пожаловать в API интернет-магазина!"}


# if __name__ == '__main__':
#     uvicorn.run('app.main:app')
