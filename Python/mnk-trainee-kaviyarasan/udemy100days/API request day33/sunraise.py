import requests

response = requests.get(url="https://api.sunrisesunset.io/json?lat=12.971599&lng=-77.594566&timezone=UTC&date=2025-01-07")
response.raise_for_status()

data = response.json()
# print(data)
results = data["results"]
print(f"sunrise: {results["sunrise"]}\nsunset: {results["sunset"]}\ndate: {results["date"]}")
