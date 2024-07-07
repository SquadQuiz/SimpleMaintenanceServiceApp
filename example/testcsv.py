import csv
from datetime import datetime

def write_csv(record_list):
    with open('data.csv', 'a', newline='') as file:
        fw = csv.writer(file)
        fw.writerow(record_list)
        
dt_format = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
record = [dt_format, 'A', 'B', 'C']
write_csv(record)
