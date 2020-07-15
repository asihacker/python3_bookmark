import time
import datetime

# python中使用time和datetime来进行时间操作
# 获取时间戳
import requests

time.time()  # 1544601181.549864

# 获取本地时间
datetime.datetime.now()  # 2018-12-12 16:04:35.667419
datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 获取今天日期
datetime.datetime.now().date()  # 2018-11-15

# 获取当前时间
datetime.datetime.now().time()  # 15:56:39.598010

# asctime格式化日期, 形式：Thu Nov 15 15:14:25 2018, str类型 与 time.ctime()相同
time.asctime(time.localtime())
time.ctime()

# strftime格式化日期
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 2018-12-12 15:53:01  str类型

# 计算时间差
now_time = datetime.datetime.now()
now_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
d1 = datetime.datetime.strptime('2016-12-10 19:11:52', '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')
print((d2 - d1).days)  # 相差天数
print((d2 - d1).seconds)  # 相差秒数)

# # 将时间转为时间戳
# a = datetime.datetime.strptime('2018-12-10 19:11:52', '%Y-%m-%d %H:%M:%S')
# time.mktime(a.timetuple())
#
# # 将时间戳转为datetime
# unix_ts = 1564635585.0
# times = datetime.datetime.fromtimestamp(unix_ts)
# # 将时间戳格式化为%Y-%m-%d %H:%M:%S格式
# # 通过淘宝api获取时间戳
# r = requests.get('http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp', timeout=10)
# b = r.json()['data']['t']
# # 淘宝的时间戳为12位，需要截取前10位
# a = time.localtime(int(b[:10]))
# c = time.strftime("%Y-%m-%d %H:%M:%S", a)
# print(c)
"""
1555048106052

2019-04-12 13:48:26
苏宁：
http://quan.suning.com/getSysTime.do

淘宝：
http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp
"""
"""
%y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称  # 乱码
    %% %号本身
"""
a = datetime.datetime.strptime('2018-12-10 19:11:52', '%Y-%m-%d %H:%M:%S')
print(time.mktime(a.timetuple()))
print(time.time())