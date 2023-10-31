# src: https://docs.python.org/3.9/library/zoneinfo.html?highlight=zoneinfo#module-zoneinfo
import zoneinfo

for tz in zoneinfo.available_timezones():
    print(tz)