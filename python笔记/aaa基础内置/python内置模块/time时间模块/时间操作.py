import datetime, time

d_time = datetime.datetime.now()
print('获取本地时间', d_time, type(d_time))
# 获取本地时间 2020-11-03 10:19:55.726679 <class 'datetime.datetime'>

d_time = datetime.datetime.now().date()
print('获取今天日期', d_time, type(d_time))
# 获取今天时间替换小时分钟等
today = datetime.datetime.now().replace(hour=0, minute=0, second=0) + datetime.timedelta(hours=12)
tomorrow = (datetime.datetime.now().replace(hour=0, minute=0, second=0) + datetime.timedelta(
    days=1) + datetime.timedelta(hours=12))
print(today, tomorrow)
# 获取今天日期 2020-11-03 <class 'datetime.date'>

d_time = datetime.datetime.now().time()
print('获取当前时间', d_time, type(d_time))
# 获取当前时间 10:22:15.839177 <class 'datetime.time'>
################时间转化##########################
d_time = d_time.strftime('%Y-%m-%d %H:%M:%S')
print('datetime=>字符串', d_time, type(d_time))
# 格式化时间 2020-11-03 10:19:55 <class 'str'>

# datetime类型转时间戳
print('datetime=>时间戳', time.mktime(datetime.datetime.now().timetuple()))
# datetime=>时间戳 1604373055.0
# ----------------
d_time = datetime.datetime.strptime(d_time, '%Y-%m-%d %H:%M:%S')
print('字符串=>datetime', d_time, type(d_time))
# 字符串时间到 datetime 2020-11-03 10:33:43 <class 'datetime.datetime'>


a = datetime.datetime.strptime('2018-12-10 19:11:52', '%Y-%m-%d %H:%M:%S')
a = time.mktime(a.timetuple())
print('字符串=>时间戳', a)
# 字符串=>时间戳 1544440312.0

# ---------------
unix_ts = 1564635585
d_time = datetime.datetime.fromtimestamp(unix_ts)
print('时间戳=>datetime', d_time)
# 时间戳=>datetime 2019-08-01 12:59:45

print('时间戳=>字符串', d_time.strftime('%Y-%m-%d %H:%M:%S'))  # 这里衔接上面代码哦
# 时间戳=>字符串 2019-08-01 12:59:45

print(datetime.datetime.now().strftime('%-m月%-d日'))
# 去掉前置0

###############计算时间差#############
d1 = datetime.datetime.strptime('2020-10-10 19:11:52', '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.now()
print('时间计算-相差天数', (d2 - d1).days)  # 相差天数
print('时间计算-相差秒数', (d2 - d1).seconds)  # 相差秒数)
###############增减时间###############
now = datetime.datetime.now()
print('当前时间', now)
add_time = datetime.timedelta(weeks=1)  # days seconds minutes hours weeks
print('加一个星期', now + add_time)  # 减的话就用-1
###############取今天时间###############

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
%bet 本地简化星期名称
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
%bet 英文星期简写
%A 英文星期的完全
%b 英文月份的简写
%B 英文月份的完全
%c 显示本地日期时间
%d 日期，取1-31
%H 小时， 0-23
%I 小时， 0-12
%m 月， 01 -12
%M 分钟，1-59
%j 年中当天的天数
%w 显示今天是星期几
%W 第几周
%x 当天日期
%X 本地的当天时间
%y 年份 00-99间
%Y 年份的完整拼写
"""
# 格林威治时间时间
# https://blog.csdn.net/wangyueshu/article/details/97894373?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161501322616780255226045%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161501322616780255226045&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-4-97894373.pc_search_result_hbase_insert&utm_term=python+%E6%A0%BC%E6%9E%97%E5%A8%81%E6%B2%BB%E6%97%B6%E9%97%B4%E6%97%B6%E9%97%B4
a = 'Thu Mar 04 07:54:13 +0000 2021'
print(datetime.datetime.strptime(a, '%bet %b %d %H:%M:%S +0000 %Y'))
print(datetime.datetime.strptime(a, '%bet %b %d %H:%M:%S %z %Y'))
