import requests
from fastapi import APIRouter, HTTPException

router = APIRouter()

RAPIDAPI_KEY = "5d33646ae6msh59189d7b543309fp1a9edcjsnedf1c52a54d7"
BASE_URL = "https://latest-mutual-fund-nav.p.rapidapi.com/latest"
querystring = {"Scheme_Type":"Open"}
@router.get("/fund-families")
async def get_fund_families():
    fund_families = await fetch_fund_families()  # Await the async function
    return {"fund_families": fund_families}

async def fetch_fund_families():
    headers = {
            "x-rapidapi-host": "latest-mutual-fund-nav.p.rapidapi.com",
            "x-rapidapi-key": RAPIDAPI_KEY,
    }
    try:
        # Make the GET request
        response = requests.get(BASE_URL, headers=headers,params=querystring)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Parse the JSON response
        # fund_families = response.json()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

