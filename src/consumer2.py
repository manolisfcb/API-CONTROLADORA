import pika
from pika.exchange_type import ExchangeType
import time
from pika import URLParameters

def callback_from_file_handler(ch, method, properties, body):
    time.sleep(0.6)
    print(body.decode('utf-8'))
    
#parm = URLParameters('amqp://guest:guest@192.168.15.117:5672/%2f')
conection_parameters =  pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(conection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='file_unzip2', exchange_type=ExchangeType.topic)

channel.queue_declare(queue='api')

channel.queue_bind(exchange='file_unzip2', queue='api', routing_key='file_unzip_only')




channel.basic_consume(queue='api', on_message_callback=callback_from_file_handler, auto_ack=True)

channel.start_consuming()