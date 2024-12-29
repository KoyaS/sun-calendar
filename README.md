# ☀️ Sun Calendar

A simple ICS calendar that shows daily sunrise & sunset times in San Francisco.  

## 🗓️ Usage

Subscribe to this link ("by URL") in your calendar app: `webcal://www.averychan.site/sun-calendar/sun.ics`

## 💻 Dev Usage + Notes

- To generate the isc file, run `create_calendar_local.py`
    - Uses this awesome free sun API: https://sunrise-sunset.org/api
    - Uses isc python library https://icspy.readthedocs.io/en/stable/
- The isc file is exposed by hosting on GH pages
- If you want to use a different location, just change the lat and long coords in `create_calendar_local.py`

