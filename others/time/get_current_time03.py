from datetime import datetime, timedelta, timezone

time_zone_offset = timedelta(hours=5, minutes=30)
time_zone = timezone(time_zone_offset)
current_time = datetime.now(time_zone).strftime('%H:%M:%S')
print(current_time)