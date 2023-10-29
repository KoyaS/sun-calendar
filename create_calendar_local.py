import requests
from ics import Calendar, Event
from datetime import datetime
import pytz

# API call for sunrise and sunset times in San Francisco, CA
sun_times_url = "https://api.sunrise-sunset.org/json?lat=37.7749000&lng=122.4194000&date=today"

response = requests.get(sun_times_url)

if response.status_code == 200:
    data = response.json()  # Assuming the response is in JSON format
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


current_date = datetime.now().strftime('%Y-%m-%d')
sunrise_time_utc = response.json().get('results').get('sunrise')

# convert from Coordinated Universal Time (UTC) to Pacific Daylight Time (PDT)
utc_zone = pytz.utc
pdt_zone = pytz.timezone('America/Los_Angeles')
utc_time_format = "%I:%M:%S %p"

utc_time = datetime.strptime(sunrise_time_utc, utc_time_format).replace(tzinfo=utc_zone)

pdt_time = utc_time.astimezone(pdt_zone)

final_sunrise_time = pdt_time.strftime("%I:%M:%S")

c = Calendar()
e = Event()
e.name = "Sunrise"
e.begin = f"{current_date} {final_sunrise_time}"
c.events.add(e)

with open('sun.ics', 'w') as f:
    f.writelines(c.serialize_iter())
