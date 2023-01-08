import calendar
from datetime import date

import datetime as datetime
import dateutil.utils
from dateutil.relativedelta import relativedelta

# Formato 2023-01-08 00:00:00
now = dateutil.utils.today()
print(now)
print(calendar.timegm(now.timetuple())) # exibindo como epoch time

# Formato 2023-01-08
today = date.today()
print(today)
print(calendar.timegm(today.timetuple())) # exibindo como epoch time

# Formato 2023-01-08 19:07:37.276208
datetime = datetime.datetime.now()
print(datetime)
print(calendar.timegm(datetime.timetuple())) # exibindo como epoch time

# Somando horas
datetime_plus_hours = datetime + relativedelta(hours=3)
print(datetime_plus_hours)
print(calendar.timegm(datetime_plus_hours.timetuple())) # exibindo como epoch time

