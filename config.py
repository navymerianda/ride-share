from dotenv import load_dotenv
from pathlib import Path
import os


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    '''Set Configuration variables from env file'''

    #Load in environment variables
    DRIVER_LOCATION_TOKEN = os.getenv('DRIVER_LOCATION_TOKEN')
    AZURE_KEY = os.getenv('AZURE_KEY')
    DRIVERS_ENDPOINT = os.getenv('DRIVERS_ENDPOINT')
    ROUTE_ENDPOINT = os.getenv('ROUTE_ENDPOINT')