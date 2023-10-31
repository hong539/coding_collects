# importing datetime
from datetime import datetime

# importing timezone from pytz module
from pytz import timezone

# giving the format of datetime
format = "%Y-%m-%d %H:%M:%S %Z%z"

# getting the current time in UTC timezone
now_utc = datetime.now(timezone('UTC'))

# Format the above DateTime using the strftime()
print('Current Time in UTC TimeZone:',now_utc.strftime(format))

# Converting to Asia/Kolkata time zone
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))

# Format the above datetime using the strftime()
print('Current Time in Asia/Kolkata TimeZone:',now_asia.strftime(format))