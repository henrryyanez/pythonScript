import requests
import time

while True:
    response = requests.get('https://tramitesadistancia.gob.ar/')
    result = response.status_code
    print(result)
    time.sleep(3)
