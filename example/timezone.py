import pytz
import datetime

# Define the timezone for GMT+7
tz = pytz.timezone('Asia/Bangkok')
current_date = datetime.datetime.now(tz).strftime("%Y-%m-%d")

print(current_date)