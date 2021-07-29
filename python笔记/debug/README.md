# bookmark
python3学习笔记

-b:发出关于str（bytes\u instance）、str（bytearray\u instance）的警告

并将bytes/bytearray与str.（-bb：问题错误）进行比较

-B:导入时不要写入.pyc文件；同时PYTHONDONTWRITEBYTECODE=x

-c cmd:作为字符串传入的程序（终止选项列表）

-d：来自解析器的调试输出；也可以是PYTHONDEBUG=x

-E:忽略PYTHON*环境变量（例如PYTHONPATH）

-h:打印此帮助消息并退出（还有--help）

-i：运行脚本后交互检查；甚至强制提示

如果stdin不是一个终端，那么pythonnspect=x

-I：将Python与用户环境隔离开来（意味着-E和-s）

-m mod：将库模块作为脚本运行（终止选项列表）

-O:删除assert和调试依赖语句；在前面添加.opt-1

.pyc扩展；也为PYTHONOPTIMIZE=x

-O O:do-O更改并丢弃docstring；在

.pyc扩展

-问：互动启动时不打印版本和版权信息

-s:不将用户站点目录添加到搜索路径；也是蟒蛇

-S:初始化时不表示“导入站点”

-u：强制stdout和stderr流不缓冲；

此选项对stdin没有影响；同时PYTHONUNBUFFERED=x

-v:verbose（跟踪导入语句）；也就是PYTHONVERBOSE=x

可以多次提供以增加详细程度

-V：打印Python版本号并退出（还有--version）

如果给定两次，则打印有关生成的更多信息

-W arg：警告控制；arg是操作：消息:类别：模块：行号

还有PYTHONWARNINGS=arg

-x:跳过源代码的第一行，允许使用非Unix形式的#！命令

-X opt：设置特定于实现的选项