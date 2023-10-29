import requests

# API call for sunrise and sunset times in San Francisco, CA
sun_times_url = "https://api.sunrise-sunset.org/json?lat=37.7749&lng=122.4194"

response = requests.get(sun_times_url)

if response.status_code == 200:
    data = response.json()  # Assuming the response is in JSON format
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
