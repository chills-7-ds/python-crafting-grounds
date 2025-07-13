from datetime import datetime, UTC, timedelta
from zoneinfo import ZoneInfo
print("Welcome to the World countdown tracker!")
event_name = input("Do enter the Event name that you want the countdown for :\n")
event_date = input("Enter the Event date(YYYY-MM-DD) :\n")
event_time = input("Event time? (HH:MM, 24-hour) \n")
combined_event_dnt =  event_date + " " + event_time
event_date_time = datetime.strptime(combined_event_dnt,"%Y-%m-%d %H:%M")
time_zone = input("Do enter your Timezone :\n")
utc_time = datetime.now(UTC)
event_date_time = event_date_time.replace(tzinfo=ZoneInfo(time_zone))
ny_time = event_date_time.astimezone(ZoneInfo("America/New_York"))
london_time = event_date_time.astimezone(ZoneInfo("Europe/London"))
tokyo_time = event_date_time.astimezone(ZoneInfo("Asia/Tokyo"))
start_time = datetime.now(ZoneInfo(time_zone))
end_time = event_date_time
t_diff = end_time - start_time
days = t_diff.days
seconds = t_diff.seconds
hours = seconds // 3600
mins = (seconds % 3600) // 60
print(f"🎉 Event : {event_name}")
print(f"📅 Local Time ({time_zone}) : {event_date_time}")
print(f"🕰️ UTC : {utc_time}")
print(f"🌍 New York: {ny_time}")
print(f"🌍 London: {london_time}")
print(f"🌍 Tokyo: {tokyo_time}")
print(f"⏳ Time remaining: {days}days,{hours}hours,{mins}minutes")