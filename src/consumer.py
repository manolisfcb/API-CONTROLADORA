import pika
from pika.exchange_type import ExchangeType
import time

def callback(ch, method, properties, body):
    time.sleep(0.6)
    print(body.decode('utf-8'))
    
    
connectio_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connectio_params)

channel = connection.channel()

channel.exchange_declare(exchange='file_unzip', exchange_type=ExchangeType.direct)

channel.queue_declare(queue='api_controladora', exclusive=True)

channel.queue_bind(exchange='file_unzip', queue='api_controladora', routing_key='file_unzip_only')

channel.basic_consume(queue='api_controladora', on_message_callback=callback, auto_ack=True)

channel.start_consuming()