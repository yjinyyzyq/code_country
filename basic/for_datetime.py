# coding:utf-8
import datetime
import pytz

# 因为datetime里面的用法很多，最好只import datetime. from datetime import * 也不是太好。
# datetime 模块里面有比较重要的几个类，分别是
"""
    datetime 表示日期的类. 
    timedelta 表示时间间隔， 两个时间点的间隔, 
    time 表示时间的类, 只用于时分秒的。
    date 表示日期的类,
    tzinfo 时区的相关信息
"""
# 我工作中用的最多的是datetime 和 timedelta
# 这里分别举例说一下。先说date
# date 类有三个参数， datetime.date(year, month, day)
# date 对象只能表示日期，不能表示时间。 date实例化时需要三个参数， year, month， date
birthday = datetime.date(year=2018, month=7, day=17)
print birthday

# datetime对象可以用来表示精确的日期和时间
birthday1 = datetime.datetime(year=1993, month=8, day=23)
print birthday1
print datetime.datetime.now()

# time对象，只能用来表示时间，不能用来表示日期。可以精确到微秒，可以具有tzinfo属性
now_time = datetime.time(hour=20, minute=30, second=10)
print now_time
print now_time.hour

# timedelta, 用来表示时间差的，可以通过实例化得到, 可以手动传入的参数有：days, seconds, microseconds, miliseconds, minutes, hours, weeks
now = datetime.datetime.now()
last = datetime.datetime(year=2016, month=3, day=10, hour=8)
delta = now - last
print delta
print last + delta == now
print last + datetime.timedelta(days=859)
print last + datetime.timedelta(days=-859)

# tzinfo 这个我用的真不多，需要了解两个概念。 utc时间， 北京时间= utc time + 8 hour DST:夏时令 人为调快时间，充分利用光照资源，中国已废除。
# python中，tzinfo为空的datetime对象称为aware的，而tzinfo不为空的datetime对象称为naive(幼稚)的。这两种类型之间运算会报错。

# 这里还需安装一下pytz, 就是指定一个时区。
t = datetime.datetime.utcnow()
print t, "现在的utc时间"
# 已知本地时间，需要转成utc时间用于存储
from tzlocal import get_localzone
tz = get_localzone()        # 获取本地的timezone
print tz, "tz 本地的timezone标签"
utc = pytz.utc              # 获得UTC timezone
print utc, "utc 默认的utc标签"
dt = datetime.datetime(2016, 6, 12, 5, 0, 0)
print dt, "dt 创建一个新的时间"
loc_dt = tz.localize(dt)    # 将datetime 数据贴上timezone
print loc_dt, "loc_dt 这个是把本地的timezone标签给上面的dt贴上"
utc_dt = loc_dt.astimezone(utc)  # 转换到新的timezone
print utc_dt, "utc_dt 这是转换成utc_dt后的timezone时间"




