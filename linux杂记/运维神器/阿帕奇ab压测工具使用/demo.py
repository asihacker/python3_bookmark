#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 20:26
# @Author  : AsiHacker
# @Site    : 
# @File    : 自定义异常.py
# @Software: PyCharm


# ab -n 1 -c 1 -p f:/postdata.txt -T application/x-www-form-urlencoded "http://127.0.0.1/abpost"
# -n 总共请求数
# -c 并发请求数
# -T 内容类型。
# application/x-www-form-urlencoded
# application/json
# application/text
# -p 包含POST参数的文件

# Server Software:        Apache          #服务器软件
# Server Hostname:        www.taoquan.ink #域名
# Server Port:            80              #请求端口号
# Document Path:          /               #文件路径
# Document Length:        40888 bytes     #页面字节数
# Concurrency Level:      10              #请求的并发数
# Time taken for tests:   27.300 seconds  #总访问时间
# Complete requests:      1000            #请求成功数量
# Failed requests:        0               #请求失败数量
# Write errors:           0
# Total transferred:      41054242 bytes  #请求总数据大小（包括header头信息）
# HTML transferred:       40888000 bytes  #html页面实际总字节数
# Requests per second:    36.63 [#/sec] (mean)  #每秒多少请求，这个是非常重要的参数数值，服务器的吞吐量
# Time per request:       272.998 [ms] (mean)     #用户平均请求等待时间
# Time per request:       27.300 [ms] (mean, across all concurrent requests) # 服务器平均处理时间，也就是服务器吞吐量的倒数
# Transfer rate:          1468.58 [Kbytes/sec] received  #每秒获取的数据长度
# Connection Times (ms)
#               min  mean[+/-sd] median   max
# Connect:       43   47   2.4     47      53
# Processing:   189  224  40.7    215     895
# Waiting:      102  128  38.6    118     794
# Total:        233  270  41.3    263     945
#
# Percentage of the requests served within a certain time (ms)
#   50%    263    #50%用户请求在263ms内返回
#   66%    271    #66%用户请求在271ms内返回
#   75%    279    #75%用户请求在279ms内返回
#   80%    285    #80%用户请求在285ms内返回
#   90%    303    #90%用户请求在303ms内返回
#   95%    320    #95%用户请求在320ms内返回
#   98%    341    #98%用户请求在341ms内返回
#   99%    373    #99%用户请求在373ms内返回
#  100%    945 (longest request)
