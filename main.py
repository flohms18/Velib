import requests

from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv('URL')

response = requests.get(url)
print(response.json())



