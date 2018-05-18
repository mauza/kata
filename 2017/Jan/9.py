import calendar
from datetime import datetime

months = [month for month in calendar.month_name]

index = datetime.now().month

print(months[index])
