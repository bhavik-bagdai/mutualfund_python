from sys import audit, prefix

from fastapi import FastAPI
from app.database import database, metadata, engine
from contextlib import asynccontextmanager
from app.auth import router as auth_router
from app.portfolio import router as portfolio_router
from app.rapidapi import router as rapidapi_router

app = FastAPI()


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await database.connect()
#     yield
#     await database.disconnect()

# app = FastAPI(lifespan=lifespan)
metadata.create_all(engine)
app.include_router(auth_router, prefix="/auth")
app.include_router(portfolio_router, prefix="/portfolio")
app.include_router(rapidapi_router, prefix="/funds")

@app.get("/")
async def root():
    return {"message": "Hello World!!!!"}