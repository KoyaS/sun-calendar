import requests
from ics import Calendar, Event
from datetime import datetime

# API call for sunrise and sunset times in San Francisco, CA
sun_times_url = "https://api.sunrise-sunset.org/json?lat=37.7749000&lng=122.4194000&date=today"

response = requests.get(sun_times_url)

if response.status_code == 200:
    data = response.json()  # Assuming the response is in JSON format
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

# convert from Coordinated Universal Time (UTC) to Pacific Daylight Time (PDT)

current_date = datetime.now().strftime('%Y-%m-%d')
sunrise_time = response.json().get('results').get('sunrise')
sunrise_time = sunrise_time.split(' ')[0] # remove AM/PM

c = Calendar()
e = Event()
e.name = "Sunrise"
e.begin = f"{current_date} {sunrise_time}"
c.events.add(e)

with open('sun.ics', 'w') as f:
    f.writelines(c.serialize_iter())
