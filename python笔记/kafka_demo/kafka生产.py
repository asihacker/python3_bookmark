import json
import time

from kafka import KafkaProducer

producer = KafkaProducer(client_id='test_ng_friendsNew',
                         bootstrap_servers=['47.112.163.25:9092', '47.112.185.243:9092',
                                            '47.112.189.251:9092'], max_request_size=3145728)  # 连接kafka
# max_request_size 配置发送包的最大值 默认 1m
with open('change.json', 'r+') as f:
    b = f.read()
producer.send(topic='test_ng_friendsNew', value=b.encode('utf-8'))

producer.close()
