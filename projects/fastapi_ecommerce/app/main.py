import uvicorn
from fastapi import FastAPI

from routers import category, products, auth, permission, reviews

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "My e-commerce app"}


app.include_router(category.router)
app.include_router(products.router)
app.include_router(auth.router)
app.include_router(permission.router)
app.include_router(reviews.router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
