import utils.mongo as db
import utils.errors as error
import bson.objectid as bson
from bson.json_util import dumps
import utils.json_serializer as json
import datetime
import questions.question_schema as question_schema
import questions.answer_schema as answer_schema
import http.client
import socket
import utils.errors as errors
from rabbit.rabbit_service import sendQuestionAnswered

def addQuestion(params, token):
    """
    Agrega una pregunta.\n
    params: dict<propiedad, valor> Question\n
    return dict<propiedad, valor> Question
    """
    """
    @api {post} /v1/questions/ Crear Pregunta
    @apiName Crear Pregunta
    @apiGroup Preguntas

    @apiUse AuthHeader

    @apiExample {json} Body
        {
            "question": "{ contenido de la pregunta }",
            "articleId": "{ articleId }"
        }

    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
        {
            "_id":"{id de la pregunta}",
            "question": "{contenido de la pregunta}",
            "userId": "{User Id}",
            "created": "{Fecha creada}",
            "answered": "{si tiene respuesta}",
            "articleId":"{articleId}"
        }

    @apiUse Errors

    """
    conn = http.client.HTTPConnection(
        socket.gethostbyname("localhost"),
        3002,
    )
    #5bdd902969a2bb15b80ef957
    #5bdd93e169a2bb15b80ef958
    headers = {"Authorization".encode("utf-8"): token.encode("utf-8")}
    conn.request("GET", "/v1/articles/" + params['articleId'], {}, headers)
    response = conn.getresponse()
    if response.status != 200:
        raise errors.NotFound()
    else:
        question = question_schema.newQuestion(token, params)
        question["_id"] = db.questions.insert_one(question).inserted_id
        return question
   
def addAnswer(params, questionId, token):
    """
    Responde una pregunta - Crea una respuesta.\n
    params: dict<propiedad, valor> Answer\n
    return dict<propiedad, valor> Answer
    """
    """
    @api {post} /v1/questions/:questionId/answers Crear Respuesta
    @apiName Crear Respuesta
    @apiGroup Respuestas

    @apiUse AuthHeader

    @apiExample {json} Body
        {
            "answer": "{ contenido de la respuesta }",
        }

    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
        {
            "_id":"{id de la respuesta}",
            "answer": "{contenido de la respuesta}",
            "userId": "{User Id}",
            "created": "{Fecha creada}",
            "articleId":"{articleId}",
            "questionId":"{pregunta a la que corresponde la respuesta}"
            "answer": "{respuesta - null cuando se crea}"     
        }

    @apiUse Errors

    """
    question = json.body_to_dic(dumps(db.questions.find_one({"_id": bson.ObjectId(questionId)})))
    if question['answered']:
        raise errors.InvalidRequest("question already answered")
    else:
        answer = answer_schema.newAnswer(token, params, question)
        answer["_id"] = db.answers.insert_one(answer).inserted_id
        setQuestionAnswered(answer)
        sendQuestionAnswered("questions","questions", question['userId'], answer['userId'], question['question'], answer['answer'])
    return answer

def getQuestionByArticle(articleId):
    """
    Obtiene las preguntas de un articulo. \n
    articleId: string ObjectId\n
    return dict<propiedad, valor> Pregunta\n
    """
    """
    @api {get} /v1/questions/:articleId Obtener preguntas de un artículo
    @apiName Buscar preguntas por artículo
    @apiGroup Preguntas

    @apiUse AuthHeader

    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
        {
            "_id":"{id de la pregunta}",
            "question": "{contenido de la pregunta}",
            "userId": "{User Id}",
            "created": "{Fecha creada}",
            "answered": "{si tiene respuesta}",
            "articleId":"{articleId}"
            "answer": "{respuesta - si answered es true}"
        }

    @apiUse Errors

    """
    try:
        result = dumps(db.questions.find({"articleId": str(articleId)}))
        if (not result):
            raise error.InvalidArgument("articleId", "Document does not exists")
        return result
    except Exception:
        raise error.InvalidArgument("articleId", "Invalid object id")

def getQuestionByUser(userId):
    """
    Obtiene las preguntas realizadas por un usuario. \n
    userId: string ObjectId\n
    return dict<propiedad, valor> Pregunta\n
    """
    """
    @api {get} /v1/questions/:userId Obtener preguntas de un usuario
    @apiName Buscar preguntas por usuario
    @apiGroup Preguntas

    @apiUse AuthHeader

    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
        {
            "_id":"{id de la pregunta}",
            "question": "{contenido de la pregunta}",
            "userId": "{User Id}",
            "created": "{Fecha creada}",
            "answered": "{si tiene respuesta}",
            "articleId":"{articleId}",
            "answer":"{respuesta - if answered es true}"
        }

    @apiUse Errors

    """
    try:
        result = dumps(db.questions.find({"userId": userId}))
        if (not result):
            raise error.InvalidArgument("userId", "Document does not exists")
        return result
    except Exception:
        raise error.InvalidArgument("userId","Invalid object id")

def setQuestionAnswered(answer):
    try:
        result = dumps(db.questions.find_one_and_update( {"_id": bson.ObjectId(answer['questionId'])}, { '$set': { "answered" : True, "answer":answer }} ))
        if (not result):
            raise error.InvalidArgument("_id", "Document does not exists")
        return result
    except Exception:
        raise error.InvalidArgument("_id", "Invalid object id")

def getAnswersByQuestion(questionId):
    """
    Obtiene las respuestas de una pregunta. \n
    questionId: string ObjectId\n
    return dict<propiedad, valor> Respuesta\n
    """
    """
    @api {get} /v1/questions/:questioId/answers Buscar Respuestas de una pregunta
    @apiName Buscar respuestas de una pregunta
    @apiGroup Respuestas

    @apiUse AuthHeader

    @apiSuccessExample {json} Respuesta
        HTTP/1.1 200 OK
        {
            "_id":"{id de la respuesta}",
            "answer": "{contenido de la respuesta}",
            "userId": "{User Id}",
            "created": "{Fecha creada}",
            "articleId":"{articleId}"
        }

    @apiUse Errors

    """
    try:
        result = dumps(db.answers.find({"questionId": questionId}))
        if (not result):
                raise error.InvalidArgument("questionId", "Document does not exists")
        return result
    except Exception:
        raise error.InvalidArgument("questionId","Invalid object id")