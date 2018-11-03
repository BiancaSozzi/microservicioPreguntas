# coding=utf_8

import pika
import utils.security as security
import threading
import utils.json_serializer as json
import utils.config as config
import utils.schema_validator as validator
import traceback

EVENT = {
    "type": {
        "required": True,
        "type": str
    },
    "message": {
        "required": True
    }
}

MSG_QUESTION_ANSWERED = {
    "userQuestionId": {
        "required": True,
        "type": str
    },
    "userAnswerId": {
        "required": True,
        "type": str
    },
    "question": {
        "required": True,
        "type": str
    },
    "answer": {
        "required": True,
        "type": str
    }

}

def init():
    """ 
    Inicializar los servicios de rabbit
    """
    initAuth()

def initAuth():
    """
    Inicializar Rabbit para escuchar los eventos de logout.
    """
    print("Init Auth")
    authConsumer = threading.Thread(target=listenAuth)
    authConsumer.start()

def listenAuth():
    """
    Escucha Eventos de logout enviados por auth
    
     @api {fanout} auth/logout Logout

    @apiGroup RabbitMQ GET

    @apiDescription Escucha de mensajes logout desde auth. Invalida sesiones en cache.

    @apiExample {json} Mensaje
      {
        "type": "fanout",
        "message" : "tokenId"
      }
    """

    EXCHANGE = "auth"

    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host = config.get_rabbit_server_url())
        )
        channel = connection.channel()

        channel.exchange_declare(
            exchange=EXCHANGE,
            exchange_type='fanout'
        )

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(
            exchange=EXCHANGE,
            queue = queue_name
        )

        def callback(ch, method, properties, body):
            event = json.body_to_dic(body.decode('utf-8'))
            if (len(validator.validateSchema(EVENT, event)) > 0):
                return

            if (event["type"] == "logout"):
                security.invalidateSession(event["message"])
            
        print("RabbitMQ Auth conectado")

        channel.basic_consume(
            callback, 
            queue=queue_name,
            no_ack = True
        )

        channel.start_consuming()
    
    except Exception:
        print("RabbitMQ Auth desconectado... Reintentando en 10 segundos")
        threading.Timer(10.0, initAuth).start()

def sendQuestionAnswered(exchange, queue, userQuestionId, userAnswerId, question, answer):
    """
    Envía eventos a notificaciones. Notifica que se ha respondido una
    pregunta para que se envie la información al usuario que realizó la pregunta.
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.get_rabbit_server_url()))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange, exchange_type='fanout')
    channel.queue_declare(queue = queue)

    message = {
        "type": "question-data",
        "message": {
            "userQuestionId": userQuestionId,
            "userAnswerId": userAnswerId,
            "question": question,
            "answer": answer,
        }
    }

    channel.basic_publish(exchange=exchange, routing_key=queue, body=json.dic_to_json(message))

    print(" [x] Sent %r" % message)

    connection.close()



