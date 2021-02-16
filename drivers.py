import requests
import query
import json
import constants
from datetime import datetime
from models import DriverResponse

#local cache - We could use redis or memcache for caching.
cachedData = {}

'''
Fetches the closest drivers for the location.

:param: latitude
:param: longitude
:return: DriverResponse object
'''
def getClosestDriverForLocation(latitude, longitude):
    getCachedData()
    closestDriver = DriverResponse(0, 0, 200)
    driverResponse = query.getDriversFromLocation()
    if driverResponse.ok:
        drivers = driverResponse.json()
        getClosestDriver(closestDriver, drivers, latitude, longitude)
    else:
        closestDriver.status = 401
    
    return closestDriver

'''
Calculates the best driver closest to the location from the list of drivers obtained from getClosestDriverForLocation().
Checks if the same closest driver id is cached, if yes; return another driverid.

:param: DriverResponse object
:param: list of drivers
:param: destination latitude (passenger)
:param: destination longitude (passenger)
:return: DriverResponse object
'''
def getClosestDriver(closestDriver, drivers, destLatitude, destLongitude):
    minTimeInSeconds = float("inf")

    for driver in drivers:
        distanceResponse = query.getRouteDirectionsFromLocation(driver[constants.LAT], driver[constants.LON], destLatitude, destLongitude)
        if distanceResponse.ok:
            distanceData = distanceResponse.json()
            travelTime = distanceData[constants.ROUTES][constants.IDX][constants.SUMMARY][constants.TRAVELTIME]
            distanceMeters = distanceData[constants.ROUTES][constants.IDX][constants.SUMMARY][constants.LENGTH]
            #Logic for finding the closest driver is based on travel time to reach the destination.
            if minTimeInSeconds > travelTime and not cachedDriverData(driver[constants.DRIVER_ID]):
                minTimeInSeconds = travelTime
                closestDriver.driverId = driver[constants.DRIVER_ID]
                closestDriver.lengthInMeters = distanceMeters
                closestDriver.status = distanceResponse.status_code
        elif distanceResponse.status_code == 400:
            if closestDriver.driverId == 0:
                closestDriver.status = constants.NO_ROUTES
        elif distanceResponse.status_code == 401:
            closestDriver.status = distanceResponse.status_code
            break
        else:
            closestDriver.status = distanceResponse.status_code

    if len(str(closestDriver.driverId)) > 1:
        writeCacheData(closestDriver.driverId)

'''
If driverid cached; return true else False

:param: driverId
'''
def cachedDriverData(driverId):
    if cachedData[constants.DRIVER_ID] == driverId and ((datetime.now() - cachedData[constants.TIME]).total_seconds()) < 12:
        return True
    else:
        return False

'''
Read from local cache file and update cachedData.

'''
def getCachedData():
    try:
        with open(constants.CACHE_FILE, 'r') as cacheFile:
            dataDict = json.load(cacheFile)
            oldDateTime = datetime.strptime(dataDict[constants.TIME], constants.DATE_TIME_FORMAT)
            dataDict[constants.TIME] = oldDateTime
            global cachedData
            cachedData = dataDict
    except Exception:
        print(constants.FILE_NOT_FOUND)

'''
Update the driver id in local cache file.

'''
def writeCacheData(driverId):
    try:
        dataDict = { constants.DRIVER_ID : driverId, constants.TIME: datetime.now().strftime(constants.DATE_TIME_FORMAT) }
        with open(constants.CACHE_FILE, 'w') as writeCacheFile: 
            json.dump(dataDict, writeCacheFile)
    except Exception:
        print(constants.FILE_NOT_FOUND)

