from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['47.112.163.25:9092', '47.112.185.243:9092', '47.112.189.251:9092'])  # 连接kafka

for key in range(999999999999):
    print(key)
    msg = f"Hello, kafka,fuck{key}".encode('utf-8')
    producer.send('textMsg', msg)

producer.close()
