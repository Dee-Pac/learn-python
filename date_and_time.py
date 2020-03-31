import datetime,time


"""
----------------
Typical Usecases 
----------------
- Current time in epoch
- Print human readable time
- Print formatted time/date
- Find the time difference in seconds
- Calculate new date by adding interval
"""


"""
Usage of time module
"""

print("time now epoch --> {}".format(time.time()))
# time now epoch --> 1585678270.9856899
print('time local --> {}'.format(time.localtime()))
# time local --> time.struct_time(tm_year=2020, tm_mon=3, tm_mday=31, tm_hour=18, tm_min=11, tm_sec=10, tm_wday=1, tm_yday=91, tm_isdst=0)
print('time gmt --> {}'.format(time.gmtime()))
# time gmt --> time.struct_time(tm_year=2020, tm_mon=3, tm_mday=31, tm_hour=18, tm_min=11, tm_sec=56, tm_wday=1, tm_yday=91, tm_isdst=0)
t1 = time.time()
time.sleep(1)
t2 = time.time()
t_diff = t2-t1
print("[{}] - [{}] = [{}] seconds".format(t2,t1,t_diff))

str_time = "2020-01-01 13:00:00"
struct_time_from_str = time.strptime(str_time,"%Y-%m-%d %H:%M:%S")
print(struct_time_from_str)
time_from_str = time.mktime(struct_time_from_str)
# time.struct_time(tm_year=2020, tm_mon=1, tm_mday=1, tm_hour=13, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=1, tm_isdst=-1)
print("[{}] to [{}]".format(str_time,time_from_str))
# [2020-01-01 13:00:00] to [1577883600.0]


"""
Usage of datatime module
"""

date1 = datetime.datetime.strptime(str_time,"%Y-%m-%d %H:%M:%S")
t_diff = datetime.timedelta(days = -1)
date2 = date1 + t_diff
print("[{}] + [{}] is [{}]".format(date1,t_diff,date2))
# [2020-01-01 13:00:00] + [-1 day, 0:00:00] is [2019-12-31 13:00:00]

