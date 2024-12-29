# ☀️ Sun Calendar

A simple ICS calendar that shows daily sunrise & sunset times in San Francisco.  

## Usage

Subscribe to this link ("by URL") in your calendar app: `webcal://www.averychan.site/sun-calendar/sun.ics`

## Dev Usage + Notes

1. To generate the isc file, run `create_calendar_local.py`
    1. Uses this awesome free sun API: https://sunrise-sunset.org/api
    2. Uses isc python library https://icspy.readthedocs.io/en/stable/
2. The isc file is exposed by hosting on GH pages
3. If you want to use a different location, just change the lat and long coords in `create_calendar_local.py`

