import requests
from ics import Calendar, Event
from datetime import datetime, timezone
import pytz

# API call for sunrise and sunset times in San Francisco, CA
sun_times_url = "https://api.sunrise-sunset.org/json?lat=37.7749000&lng=-122.4194000&date=today"
current_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
sun_times_url += f"&date={current_date}"
print(f"sun_times_url: {sun_times_url}")

response = requests.get(sun_times_url)

response_json = None

if response.status_code == 200:
    data = response.json()  # Assuming the response is in JSON format
    print(f"response json: {data}")
    response_json = data
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

time_format = "%I:%M:%S %p"  # format that matches the time strings in the response
year, month, day = map(int, current_date.split('-'))
# Convert the strings to datetime objects
datetime_objects = {
    key: datetime.strptime(value, time_format).replace(tzinfo=pytz.utc)
    for key, value in response_json['results'].items()
    if key != 'day_length'  # 'day_length' doesn't match the time format
}

for key, dt_obj in datetime_objects.items():
    datetime_objects[key] = dt_obj.replace(year=year, month=month, day=day)

calendar_time_format = "%Y-%m-%d %H:%M:%S"

c = Calendar()

# Create an event for today's sunrise
e = Event()
e.name = "🌅 Sunrise"
e.begin = datetime_objects['sunrise'].strftime(calendar_time_format)
e.duration = {'seconds': 15*60}
c.events.add(e)

# Create an event for today's sunset
e = Event()
e.name = "🌇 Sunset"
e.begin = datetime_objects['sunset'].strftime(calendar_time_format)
e.duration = {'seconds': 15*60}
c.events.add(e)

with open('sun.ics', 'w') as f:
    f.writelines(c.serialize_iter())
