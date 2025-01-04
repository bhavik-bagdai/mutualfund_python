import requests
from fastapi import APIRouter, HTTPException

router = APIRouter()

RAPIDAPI_KEY = "5d33646ae6msh59189d7b543309fp1a9edcjsnedf1c52a54d7"
BASE_URL = "https://latest-mutual-fund-nav.p.rapidapi.com"

@router.get("/fund-families")
async def get_fund_families():
    headers = {
        "x-rapidapi-host": "latest-mutual-fund-nav.p.rapidapi.com",
        "x-rapidapi-key": RAPIDAPI_KEY,
    }
    response = requests.get(f"{BASE_URL}/fundFamilies", headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch fund families")
    return response.json()
