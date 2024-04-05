

import requests
import os 
import sqlite3

api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
query = '3lb carrots and a chicken sandwich'
response = requests.get(api_url + query, headers={'X-Api-Key':os.getenv("CNINJA_API_KEY")})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)