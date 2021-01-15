import re
from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2021, 1, 15, 15, 59)
print(dt)

dt = datetime(2021, 1, 15, 15, 59)
print(dt.timestamp())

t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now.strftime('%a, %b %H:%M'))


now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))


tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)


utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)


def to_timestamp(dt_str, tz_str):
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    print(cday)
    m = re.match(r'^(UTC)(.+?):(00)$', tz_str)
    return cday.astimezone(timezone(timedelta(hours=int(m[2])))).timestamp()


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
