#app/location.py



"""Route that provides data for each location based on input of location name in the form of "City, State".

POST '/location/data'
"""


# Imports

import os

from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values

import logging
from typing import List, Optional

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, Json


# Router

log = logging.getLogger(__name__)
router = APIRouter()


# Connect to AWS RDS PG DB

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)

# Cursor for making SQL queries

cursor = connection.cursor()


# Instantiate LocationDataRequest BaseModel

class LocationDataRequest(BaseModel):
    """Input Schema - the user's choice of Location (City, State)"""

    location: str = Field(..., example="El Paso, Texas")


# Instantiate LocationDataItem BaseModel

class LocationDataItem(BaseModel):
    """Output Schema - Location information."""
    
    city_name: str = Field(..., example = "Phoenix, Arizona")
    population: int = Field(..., example = 1680992)
    rent_per_month: int = Field(..., example = 1447.4375)
    walk_score: int = Field(..., example = 41)
    bike_score: int = Field(..., example = 56)
    cost_of_living_index: int = Field(..., example = 105.79999999999986)
    livability_score: int = Field(..., example = 8401.333637579924)
    crime_rate: int = Field(..., example = 8075.886143420093)
    violent_crime: int = Field(..., example = 11803)
    murder_and_nonnegligent_manslaughter: int = Field(..., example = 131)
    rape: int = Field(..., example = 1139)
    robbery: int = Field(..., example = 3197)
    aggravated_assault: int = Field(..., example = 7336)
    property_crime: int = Field(..., example = 55974)
    burglary: int = Field(..., example = 9471)
    larceny_theft: int = Field(..., example = 39427)
    motor_vehicle_theft: int = Field(..., example = 7076)
    arson: int = Field(..., example = 201)

    
# Instantiate LocationDataResponse BaseModel

class LocationDataResponse(BaseModel):
    """Output schema - List of recommended strains."""

    response: Json[LocationDataItem] = Field(...)


# Router to make POST request for data on specified location

@router.post('/location/data', response_model=LocationDataItem)
async def location_data(location: LocationDataRequest):
    """
    Route for front end to obtain the data for the Location of choice.

    ### Request:
    "location": "City, State"

    ### Response:
    A JSON Object of the data for requested Location \n
    "location": city and state of location requested \n
    "population": population of location as an int with no commas \n
    "rent_per_month": rent per month as an int with no $ sign \n
    "walk_score": walk score as a float \n
    "livability_score": livability score as a float
    """

    # Make sure location paramater is a string in the form of "City, State"

    location = str(location)
    location = location.replace('location=', "")
    location = location.replace("'", "")


    # Queries for data response

    cursor.execute("""SELECT "2019 Population" FROM cityspire WHERE "Location" = %s;""", [location])
    pop = cursor.fetchone()

    cursor.execute("""SELECT "2019 Rental Rates" FROM cityspire WHERE "Location" = %s;""", [location])
    rent = cursor.fetchone()

    cursor.execute("""SELECT "Walk Score" FROM cityspire WHERE "Location" = %s;""", [location])
    walk = cursor.fetchone()

    cursor.execute("""SELECT "Bike Score" FROM cityspire WHERE "Location" = %s;""", [location])
    bike = cursor.fetchone()

    cursor.execute("""SELECT "Cost of Living Index" FROM cityspire WHERE "Location" = %s;""", [location])
    cost_of_living_index = cursor.fetchone()

    cursor.execute("""SELECT "Livability Score" FROM cityspire WHERE "Location" = %s;""", [location])
    live = cursor.fetchone()

    cursor.execute("""SELECT "Crime Rate" FROM cityspire WHERE "Location" = %s;""", [location])
    crime_rate = cursor.fetchone()

    cursor.execute("""SELECT "Violent crime" FROM cityspire WHERE "Location" = %s;""", [location])
    violent_crime = cursor.fetchone()

    cursor.execute("""SELECT "Murder and nonnegligent manslaughter" FROM cityspire WHERE "Location" = %s;""", [location])
    murder_and_nonnegligent_manslaughter = cursor.fetchone()

    cursor.execute("""SELECT "Rape" FROM cityspire WHERE "Location" = %s;""", [location])
    rape = cursor.fetchone()

    cursor.execute("""SELECT "Robbery" FROM cityspire WHERE "Location" = %s;""", [location])
    robbery = cursor.fetchone()

    cursor.execute("""SELECT "Aggravated assault" FROM cityspire WHERE "Location" = %s;""", [location])
    aggravated_assault = cursor.fetchone()

    cursor.execute("""SELECT "Property crime" FROM cityspire WHERE "Location" = %s;""", [location])
    property_crime = cursor.fetchone()

    cursor.execute("""SELECT "Burglary" FROM cityspire WHERE "Location" = %s;""", [location])
    burglary = cursor.fetchone()

    cursor.execute("""SELECT "Larceny-theft" FROM cityspire WHERE "Location" = %s;""", [location])
    larceny_theft = cursor.fetchone()

    cursor.execute("""SELECT "Motor vehicle theft" FROM cityspire WHERE "Location" = %s;""", [location])
    motor_vehicle_theft = cursor.fetchone()

    cursor.execute("""SELECT "Arson" FROM cityspire WHERE "Location" = %s;""", [location])
    arson = cursor.fetchone()


    # Return the data that was requested and queried

    return {
        "city_name": str(location),
        "population": int(pop[0]),
        "rent_per_month": int(rent[0]),
        "walk_score": int(walk[0]),
        "bike_score": int(bike[0]),
        "cost_of_living_index": int(cost_of_living_index[0]),
        "livability_score": int(live[0]),
        "crime_rate": int(crime_rate[0]),
        "violent_crime": int(violent_crime[0]),
        "murder_and_nonnegligent_manslaughter": int(murder_and_nonnegligent_manslaughter[0]),
        "rape": int(rape[0]),
        "robbery": int(robbery[0]),
        "aggravated_assault": int(aggravated_assault[0]),
        "property_crime": int(property_crime[0]),
        "burglary": int(burglary[0]),
        "larceny_theft": int(larceny_theft[0]),
        "motor_vehicle_theft": int(motor_vehicle_theft[0]),
        "arson": int(arson[0])
    }
