from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_index():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Locate": "Driver"}

def test_find_closest_driver_available():
    response = client.get('/find-closest-driver?lat=31.3296489&lon=30.1083')
    assert response.status_code == 200
    assert response.json() == {
                                "driverId": "0fb8f0d6-886a-4d37-bb94-9d06cb4fd8b2",
                                "lengthInMeters": 262031,
                                "status": 200
                              }

def test_find_closest_driver_unavailable():
    response = client.get('/find-closest-driver?lat=1.3296489&lon=0.1083')
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {
                                "driverId": 0,
                                "lengthInMeters": 0,
                                "status": "NO DRIVERS FOUND!"
                              }

def test_find_closest_driver_invalid_input():
    response = client.get('/find-closest-driver?lat=You&lon=Tea')
    assert response.json() ==  {
                                "detail": [
                                    {
                                        "loc": [
                                            "query",
                                            "lat"
                                        ],
                                        "msg": "value is not a valid float",
                                        "type": "type_error.float"
                                    },
                                    {
                                        "loc": [
                                            "query",
                                            "lon"
                                        ],
                                        "msg": "value is not a valid float",
                                        "type": "type_error.float"
                                    }
                                ]
                            }
                              