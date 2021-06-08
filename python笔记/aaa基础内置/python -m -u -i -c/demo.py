#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 14:56
# @Author  : AsiHacker
# @File    : 自定义异常.py
# @Software: PyCharm
# python -m
#           执行py内置方法 json.tool |
#           http.server 127.0.0.1:9090 |
#           compileall 原始锁lock.py (把py文件编译成pyc 2进制文件 加密代码)目录在pycache 加-b则生成在当前目录｜
#           pydoc -p 9090 原始锁lock.py 打开一个网页也阅读py的文档
#           pdb 原始锁lock.py 调试模式来运行py代码
#           venv asi 生成虚拟环境
#           json.tool json解析工具 # echo '{"amount":3.4}' | python -m json.tool
#           idlelib example.py 可视化编辑器 简化版本idea
#           zipapp myapp -m "example:main" 打包python
#          encodings.rot_13 加密｜echo "xxx" | python -m encodings.rot_13
#          base64 -d base64加解密 echo "aGFoYQo=" | python -m base64 -d（-d 解码，没有-d就编码）echo "MTJkZHdxCg=="|python -m base64 -d
#          mimetypes 识别文件或者url的mime类型 ｜python -m mimetypes sample.py｜python -m mimetypes https://docs.python.org/3/library/mimetypes.html
#          sysconfig 查看python配置
#          site 命令查看系统路径

# python -u8bf7编码的解码 print 实时输出，不在缓存读取
# python -i 执行.py文件后进入交互模式
# python -c 单行执行.py
# python pass 占位符 ... 也是占位符

a = 10
print(a)
