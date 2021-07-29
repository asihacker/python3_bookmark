from kafka import KafkaConsumer

# 一个group中的消费者数量大于分区数量的话，多余的消费者将不会收到任何消息。
consumer = KafkaConsumer('topic1', group_id='whatsapp-send-server',
                         # client_id='cjx-1',
                         bootstrap_servers=['0.0.0.0:9092'])
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)

"""
kafka集群地址：47.112.163.25:9092,47.112.185.243:9092,47.112.189.251:9092
测试主题名：textMsg
"""
