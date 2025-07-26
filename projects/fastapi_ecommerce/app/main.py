import uvicorn
from fastapi import FastAPI

# from routers import category_router, products_router
from routers import category, products

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "My e-commerce app"}


app.include_router(category.router)
app.include_router(products.router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
