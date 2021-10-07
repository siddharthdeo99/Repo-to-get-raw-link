import time
import requests
while True:
    url = "https://sid-ki-bandi.herokuapp.com"
    data = requests.get(url)
    print(data)
    time.sleep(30)
