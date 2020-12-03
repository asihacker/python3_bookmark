import pika

# 建立连接
userx = pika.PlainCredentials("admin", "admin")
conn = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1", 5672, '/', credentials=userx))

# 开辟管道
channelx = conn.channel()
# 声明队列，参数为队列名
channelx.queue_declare(queue="test1", durable=False)  # durable 持久化
# channelx.queue_bind(queue='test2', exchange='test2')

# 发送数据，发送一条，如果要发送多条则复制此段
# 其中exchange表示交换器，能精确指定消息应该发送到哪个队列，routing_key设置为队列的名称，body就是发送的内容
for key in range(10):
    channelx.basic_publish(exchange="",
                           routing_key="test1",  # 队列名
                           body=str(key)  # 发送的数据
                           )
    print("--------发送数据完成-----------")

# 关闭连接
conn.close()
