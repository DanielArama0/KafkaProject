from kafka import KafkaConsumer

consumer1 = KafkaConsumer(
    'my_topic',
    bootstrap_servers='localhost:9092',
    group_id='consumer_group_1',
    auto_offset_reset='earliest'
)

for message in consumer1:
    print(f"Consumer 1 recieved: {message.value.decode()}")
