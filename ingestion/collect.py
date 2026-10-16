import requests 
import pandas as pd
import duckdb 
import pyarrow

from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv('URL')

response = requests.get(url).json()

data = pd.json_normalize(response)

data.to_parquet('./data/stations.parquet',index=False)

