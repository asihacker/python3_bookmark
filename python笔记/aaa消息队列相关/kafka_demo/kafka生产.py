import time

from kafka import KafkaProducer

producer = KafkaProducer(client_id='cjx-a',
                         bootstrap_servers=['0.0.0.0:9092'], max_request_size=3145728)  # 连接kafka
# max_request_size 配置发送包的最大值 默认 1m
for _ in range(100000):
    time.sleep(0.1)
    # producer.send(topic='3-prod-textMsg', value=f'你好{datetime.datetime.now()}'.encode())
    producer.send(topic='topic1', value=b"ni123123hao")
    print(1)

producer.close()
