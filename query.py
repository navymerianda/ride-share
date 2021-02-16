import requests
from urllib.parse import urlencode
import config
import constants

'''
Encode and format the query based on requirements.

:param: endpoint URL
:parameters: dictionary of params
:return: formatted URL
'''
def buildQuery(endpoint, parameters):
    data = urlencode(parameters)
    url = f"{endpoint}?{data}"
    return url

'''
Setting up a query to retrieve Drivers Location

'''
def getDriversFromLocation():
    endpoint = config.Config.DRIVERS_ENDPOINT
    secret = {constants.CODE : config.Config.DRIVER_LOCATION_TOKEN }
    formattedURL = buildQuery(endpoint, secret)

    response = executeQuery(formattedURL)
    return response

'''
Setting up a query to retrieve Route directions.

:param: original latitude
:param: original longitude
:param: destination latitude
:param: destination longitude
:return json response

'''
def getRouteDirectionsFromLocation(originLat, originLon, destLatitude, destLongitude):
    endpoint = config.Config.ROUTE_ENDPOINT
    parameters = {constants.SUBS_KEY: config.Config.AZURE_KEY, constants.API_VERSION : constants.VERSION, constants.QUERY_KEY : ''}
    parameters[constants.QUERY_KEY] = f'{originLat},{originLon}:{destLatitude},{destLongitude}'
    formattedURL = buildQuery(endpoint, parameters)

    response = executeQuery(formattedURL)
    return response

'''
Main point of URL execution.

:param: formatted URL
:return: URL response

'''
def executeQuery(formattedURL):
    try:
        print(formattedURL)
        response = requests.get(formattedURL)
    except requests.exceptions.HTTPError as errh:
        print(constants.HTTP_ERROR, errh)
    except requests.exceptions.ConnectionError as errc:
        print(constants.CONNECT_ERROR, errc)
    except requests.exceptions.Timeout as errt:
        print(constants.TIMEOUT_ERROR, errt)
    except requests.exceptions.RequestException as err:
        print(constants.API_ERROR, err)

    return response
