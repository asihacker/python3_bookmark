import pika

# 建立连接
userx = pika.PlainCredentials("admin", "admin")
conn = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1", 5672, '/', credentials=userx))

# 开辟管道
channelx = conn.channel()

# 声明队列，参数为队列名
channelx.queue_declare(queue="dongchannel11")


# 消息处理函数，执行完成才说明接收完成，此时才可以接收下一条，串行
def dongcallbackfun(v1, v2, v3, bodyx):
    print("得到的数据为:", bodyx)


# 接收准备
channelx.basic_consume(
    queue="dongchannel11",  # 队列名
    on_message_callback=dongcallbackfun,  # 收到消息的回调函数
    auto_ack=True,  # 是否发送消息确认
    exclusive=False  # 是否允许其他消费者连接这个队列
)
print("-------- 开始接收数据 -----------")

# 开始接收消息
channelx.start_consuming()
