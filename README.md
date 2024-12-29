# ☀️ Sun Calendar

A simple ICS calendar that shows daily sunrise & sunset times in San Francisco.  

## 🗓️ Usage

Subscribe to this link ("by URL") in your calendar app: `webcal://www.averychan.site/sun-calendar/sun.ics`

Sunrise and Sunset times for the current week should appear in your calendar like this:

<img src="https://github.com/user-attachments/assets/b74367bc-9a3c-44dd-b00d-57a810d2285f" style="width: 500px" alt="example calendar view">

## 💻 Dev Usage + Notes

- To generate the isc file, run `create_calendar_local.py`
    - Uses this awesome free sun API: https://sunrise-sunset.org/api
    - Uses isc python library https://icspy.readthedocs.io/en/stable/
- The isc file is exposed by hosting on GH pages
- If you want to use a different location, just change the lat and long coords in `create_calendar_local.py`

