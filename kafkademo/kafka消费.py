from kafka import KafkaConsumer

consumer = KafkaConsumer('textMsg', bootstrap_servers=['47.112.163.25:9092', '47.112.185.243:9092', '47.112.189.251:9092'])
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)

"""
kafka集群地址：47.112.163.25:9092,47.112.185.243:9092,47.112.189.251:9092
测试主题名：textMsg
"""
