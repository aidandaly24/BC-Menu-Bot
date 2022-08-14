import json
import requests

url = "https://web.bc.edu/dining/menu/todayMenu_PROD.json"

response = requests.get(url)

data = json.loads(response.text)