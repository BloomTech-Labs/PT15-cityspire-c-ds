#app/locations.py



"""Route that provides locations the model was trained on.
GET '/locations'
"""


# Imports

import os

from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values

import logging
from typing import List

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


# Router

log = logging.getLogger(__name__)
router = APIRouter()


# Connect to AWS RDS PG DB

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)

# Cursor for making SQL queries

cursor = connection.cursor()


# Instantiate LocationsResponse BaseModel

class LocationsResponse(BaseModel):
    """Use this data model to parse the request body JSON."""

    locations: List[str] = Field(..., example=['Orlando, Florida', 'Portland, Oregon', "..."])


# Query for all unique locations

cursor.execute("""SELECT DISTINCT "Location" FROM cityspire;""")
result = cursor.fetchall()
Locations = [location[0] for location in result]


# Router to make GET request for labels of data

@router.get('/locations', response_model=LocationsResponse)
async def locations():
    """Route for front end to obtain the Locations the model was trained on.
    ### Response
    - `locations`: list of locations in form of City, State
    """
    return {
        'locations': Locations
    }
