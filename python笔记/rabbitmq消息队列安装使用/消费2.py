import pika

# 建立连接
userx = pika.PlainCredentials("admin", "admin")
conn = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1", 5672, '/', credentials=userx))

# 开辟管道
channelx = conn.channel()

# 声明队列，参数为队列名
channelx.queue_declare(queue="test1")


# 消息处理函数，执行完成才说明接收完成，此时才可以接收下一条，串行
def dongcallbackfun(cn, method, properties, body):
    print("得到的数据为:", body)
    cn.basic_ack(delivery_tag=method.delivery_tag)  # 确定收到消息


# 接收准备
# channelx.basic_qos(prefetch_count=1)  # 公平调度，确保每个消费者把一条消费掉后，才接收下一条
channelx.basic_consume(
    queue="test1",  # 队列名
    on_message_callback=dongcallbackfun,  # 收到消息的回调函数
    auto_ack=False,  # 是否自动消息确认
    exclusive=False  # 是否允许其他消费者连接这个队列
)
print("-------- 开始接收数据 -----------")

# 开始接收消息
channelx.start_consuming()
