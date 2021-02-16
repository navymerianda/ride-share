Ride Share
You work for a ride share company that allows passengers to connect with drivers to take them where they need to go. You're building out the core platform and a new webservice is needed to locate drivers near the passenger.  Create a web service using the language of your choice that exposes an endpoint which allows an external caller to provide a longitude and latitude coordinate and returns the nearest available driver.  There is an external web service that can be used to retrieve the driver locations (the OpenAPI spec for this service is provided as well).  In order to determine the distance of the driver, there is an available route service using Azure Maps.  Note that the Azure Maps service is in the S0 tier (and thus does not support the S1 APIs) and is throttled to a maximum of 50 requests/second.
The web service should adhere to the provided OpenAPI spec.  


# Resources
1.  Web Service OpenAPI spec: [webServiceApi.yaml](webServiceApi.yaml)
2.  Driver Location OpenAPI spec: [driverLocationsApi.yaml](driverLocationsApi.yaml)
3.  Code For Driver Locations Endpoint: SECRETKEY
4.  [Link to Azure Maps Route API Docs](https://docs.microsoft.com/en-us/rest/api/maps/route/getroutedirections)
5.  Azure Maps Route Endpoint: https://atlas.microsoft.com/route/directions/json?query={origin-lat},{origin-lon}:{destination-lat},{destination-lon}&&api-version=1.0

# Bonus Requirements
1.	Assume driver location data becomes stale after 30 seconds.  Stale data should not be used when determining the closest available driver.
2.	If a driver is selected as the closest driver, that same driver cannot be selected again for 12 seconds.
3.	Azure Map Route requests can become expensive at scale.  Implement optimizations that reduce the number of route requests that need to be made.