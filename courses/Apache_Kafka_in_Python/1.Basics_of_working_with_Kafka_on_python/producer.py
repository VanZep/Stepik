import time

from confluent_kafka import Producer


def delivery_report(err, msg):
    if err is not None:
        print('Ошибка отправки сообщения!')
        raise err
    else:
        print(
            f'Сообщение {msg.value().decode()}'
            f' в топик {msg.topic()} доставлено'
        )

config = {
    'bootstrap.servers': 'localhost:9092',
    'message.timeout.ms': 5000
}

producer = Producer(config)


def send_message(topic_: str, message_: str):
    producer.produce(topic_, value=message_, callback=delivery_report)
    producer.flush()


if __name__ == '__main__':
    topic = 'test_topic'
    message = 'Привет Kafka!'

    i = 0
    while True:
        send_message(topic, f'{message} #{i}')
        i += 1
        time.sleep(1)
