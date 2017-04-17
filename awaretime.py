import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("naive local time {}".format(local_time))
print("naive utc {}".format(utc_time))

aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("aware local time {}, time zone {} ".format(aware_local_time, aware_local_time.tzinfo))
print("aware utc {}, time zone {} ". format(aware_utc_time, aware_utc_time.tzinfo))


gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 1445733000
t = s + (60 * 60)

print('=' * 50)

gb = pytz.timezone('GB')
# no idea why this section won't work
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimzone('GB')
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimzone('GB')

print("{} seconds since the epoch {}".format(s, dt1))
print("{} seconds since the epoch {}".format(t, dt2))
