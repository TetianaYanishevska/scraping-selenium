import os
from dotenv import load_dotenv

load_dotenv()

SOCIAL_NETWORK_LOGIN = os.getenv('SOCIAL_NETWORK_LOGIN')
SOCIAL_NETWORK_EMAIL = os.getenv('SOCIAL_NETWORK_EMAIL')
SOCIAL_NETWORK_PASSWORD = os.getenv('SOCIAL_NETWORK_PASSWORD')
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')
SOCIAL_NETWORK_HOST = os.getenv('SOCIAL_NETWORK_HOST')
SOCIAL_NETWORK_PORT = os.getenv('SOCIAL_NETWORK_PORT')
