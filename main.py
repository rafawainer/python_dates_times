import calendar
import datetime as datetime
from datetime import date

import dateutil.utils
import pytz
from dateutil.relativedelta import relativedelta

print("Formato 2023-01-08 00:00:00")
now = dateutil.utils.today()
print(now)
print(calendar.timegm(now.timetuple())) # exibindo como epoch time

print("\nFormato 2023-01-08")
today = date.today()
print(today)
print(calendar.timegm(today.timetuple())) # exibindo como epoch time

print("\nFormato 2023-01-08 19:07:37.276208")
datetime = datetime.datetime.now()
print(datetime)
print(calendar.timegm(datetime.timetuple())) # exibindo como epoch time

print("\nExibindo data e horario até segundos")
s1 = datetime.strftime("%Y-%m-%d %H:%M:%S")
s2 = datetime.strptime(s1, "%Y-%m-%d %H:%M:%S")
print(s2)
print(calendar.timegm(s2.timetuple())) # exibindo como epoch time

sum=3
print("\nSomando {} horas".format(sum))
print(datetime)
datetime_plus_hours = datetime + relativedelta(hours=sum)
print(datetime_plus_hours)
print(calendar.timegm(datetime_plus_hours.timetuple())) # exibindo como epoch time

sub = 3
print("\nSubtraindo {} horas".format(sub))
print(datetime)
datetime_plus_hours = datetime - relativedelta(hours=sub)
print(datetime_plus_hours)
print(calendar.timegm(datetime_plus_hours.timetuple())) # exibindo como epoch time

print("\nTrabalhando com TimeZone Sao Paulo")
tz_sao_paulo = pytz.timezone("America/Sao_Paulo")
datetime_sao_paulo = datetime.now(tz_sao_paulo)
print("Sao Paulo:", datetime_sao_paulo.strftime("%Y-%m-%d %H:%M:%S"))

print("\nTrabalhando com TimeZone Nova Iorque")
tz_nova_iorque = pytz.timezone("America/New_York")
datetime_nova_iorque = datetime.now(tz_nova_iorque)
print("Nova Iorque:", datetime_nova_iorque.strftime("%Y-%m-%d %H:%M:%S"))

