from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from .database import database
from .dbmodels import portfolios

router = APIRouter()

class Investment(BaseModel):
    user_id: int
    scheme_name: str
    invested_amount: float

@router.get("/portfolio")
async def get_portfolio(user_id: int):
    query = portfolios.select().where(portfolios.c.user_id == user_id)
    return await database.fetch_all(query)

@router.post("/portfolio")
async def add_investment(investment: Investment):
    query = portfolios.insert().values(
        user_id=investment.user_id,
        scheme_name=investment.scheme_name,
        invested_amount=investment.invested_amount,
        current_value=investment.invested_amount
    )
    await database.execute(query)
    return {"message": "Investment added successfully"}
