# coding:utf-8
import time
# 首先，我需要说明的是，time这个模块没有datetime模块好，如果可以使用，尽量使用datetime.
# 这里整理一下如何使用
# basic

now_time = time.time()
now_timestamp = now_time       # timestamp
now_struct_time = time.localtime(now_timestamp)  # timestamp ---->  struct_time
now_format_string = time.strftime("%Y-%m-%d %H-%M-%S", now_struct_time)  # struct_time ----->  format_string
new_now_format_string = time.strptime(now_format_string, "%Y-%m-%d %H-%M-%S")  # format_string ----->  struct_time
new_timestamp = time.mktime(new_now_format_string)  # struct_time ---->  timestamp

print now_timestamp,  "# timestamp"
print now_struct_time, "# timestamp ---->  struct_time"
print now_format_string, "# struct_time ----->  format_string"
print new_now_format_string, "# format_string ----->  struct_time"
print new_timestamp, "#  struct_time ---->  timestamp"

# gmtime/asctime/ctime

# gmtime 将一个时间戳转换成为UTC时区的struct_time.
# for example:
print time.gmtime(now_time), "time.gmtime(now_time)"

# asctime, 将接受一个时间元组并返回一个可读的形式为"Tue Jul 11 18:07:14 2018"
print time.asctime(now_struct_time), "time.asctime(now_struct_time)"

# ctime 将一个时间戳转换为time.asctime()的形式，如果参数未给，默认time.time()
print time.ctime(now_time), "time.ctime(now_time)"

