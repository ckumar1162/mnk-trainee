import requests
from datetime import datetime
parameters={
    "lat":20.903000,
    "lng":85.174103,
    
}
response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
print(data)
sunrise=data["results"]["sunrise"]
sunset=data["results"]["sunset"]
print(sunrise)
print(sunset)

now=datetime.now()
print(now)
