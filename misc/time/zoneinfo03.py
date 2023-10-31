from datetime import datetime
from pytz import timezone
import sys

tz_zones = ["Asia/Hong_Kong", "Asia/Taipei", "Asia/Tokyo", "Europe/London", "Europe/Paris"]
format = "%Y-%m-%d %H:%M:%S %Z%z"

# getting the current time in UTC timezone
now_utc = datetime.now(timezone('UTC'))

# Format the above DateTime using the strftime()
print(f"Current Time in UTC TimeZone: {now_utc.strftime(format)}")

# Converting with tz_zones
for x in tz_zones:
    transfer_time = now_utc.astimezone(timezone(x))
    print(f"Current Time in {x} TimeZone: {transfer_time.strftime(format)}")

for line in sys.stdin:
	if 'q' == line.rstrip():
		break
	print(f'Input : {line}')

print("Exit")