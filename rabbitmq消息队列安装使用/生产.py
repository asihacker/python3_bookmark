import pika

# 建立连接
userx = pika.PlainCredentials("admin", "admin")
conn = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1", 5672, '/', credentials=userx))

# 开辟管道
channelx = conn.channel()

# 声明队列，参数为队列名
channelx.queue_declare(queue="dongchannel11")

# 发送数据，发送一条，如果要发送多条则复制此段
for key in range(1000):
    channelx.basic_publish(exchange="",
                           routing_key="dongchannel12",  # 队列名
                           body="12"  # 发送的数据
                           )
    print("--------发送数据完成-----------")

# 关闭连接
conn.close()
