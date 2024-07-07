from datetime import datetime

dt = datetime.now()

print(dt)

dt_format = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print(dt_format)