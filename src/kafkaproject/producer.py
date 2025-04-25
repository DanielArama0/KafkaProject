from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(10):
    message = f"Message {i}"
    producer.send('my_topic', value=message.encode())
    print(f"Sent: {message}")
    time.sleep(1)

producer.flush()
producer.close()
