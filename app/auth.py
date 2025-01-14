from operator import and_

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db.database import database
from app.models.dbmodels import users

router = APIRouter()

class User(BaseModel):
    email:str
    password:str

@router.post("/register")
async def register(user: User):
    qry = users.insert().values(email=user.email, password=user.password)
    try:
        await database.execute(qry)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400,detail="User Found")
    return {"message": "User Created"}

@router.post("/login")
async def login(user: User):
    query = users.select().where(and_(users.c.email == user.email, users.c.password == user.password))
    db_user = await database.fetch_one(query)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"id": db_user["id"]}

