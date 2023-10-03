#24 Time Zones
from datetime import datetime, timezone

time_zone = timezone('Asia/Kolkata')
current_time = datetime.now(time_zone).strftime('%H:%M:%S')
print(current_time)