'''
DriverResponse class to hold three attributes: DriverId, LengthInMeters and Status Code.

'''

class DriverResponse:
    def __init__(self, driverId, lengthInMeters, status):
        self.driverId = driverId
        self.lengthInMeters = lengthInMeters
        self.status = status
   