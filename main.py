from typing import Optional
from fastapi import FastAPI
import drivers
import json
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/")
def index():
    return {"Locate": "Driver"}

'''
Find closest driver endpoint.

:param lat: float (Latitude Coordinate)
:param lon: float (Longitude Coordinate)
:return: (driverid, length, http status code)
'''
@app.get("/find-closest-driver")
def find_closest_driver(lat:float, lon:float):
    closestDriver = drivers.getClosestDriverForLocation(lat, lon)

    return jsonable_encoder(closestDriver)