from kafka import KafkaConsumer

consumer2 = KafkaConsumer(
    'my_topic',
    bootstrap_servers='localhost:9092',
    group_id='consumer_group_1',
    auto_offset_reset='earliest'
)

for message in consumer2:
    print(f"Consumer 2 received: {message.value.decode()}")
