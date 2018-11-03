import pika
import utils.config as config
connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.get_rabbit_server_url()))
channel = connection.channel()

channel.exchange_declare(exchange='questions', exchange_type='fanout')
channel.queue_declare(queue='questions')

channel.queue_bind(exchange='questions',
                   queue='questions')

                   
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                    queue='questions',
                    no_ack=True)

channel.start_consuming()
    
