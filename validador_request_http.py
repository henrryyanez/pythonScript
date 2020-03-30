import requests
import time

while True:
    try:
        response = requests.get('https://tramitesadistancia.gob.ar/')
        result = response.status_code
        print(result)
        time.sleep(1)
    except ConnectionError:
        print("Falla en la respuesta...!!!")
