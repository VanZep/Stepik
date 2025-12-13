from confluent_kafka import Consumer, KafkaException


config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest',
    # 'auto.offset.reset': 'latest'
}

consumer = Consumer(config)


if __name__ == '__main__':
    topic = 'test_topic'
    timeout_s = 1.0

    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(timeout=timeout_s)

            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:
                print(f'Принято: {msg.value().decode()}')
    finally:
        consumer.close()
