import utils.mongo as db
import utils.errors as error
import bson.objectid as bson
from bson.json_util import dumps
import datetime
import questions.question_schema as question_schema
import questions.answer_schema as answer_schema

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
            "articleId": "{ articleId }"
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
        }

    @apiUse Errors

    """
    answer = answer_schema.newAnswer(token, params, questionId)
    answer["_id"] = db.answers.insert_one(answer).inserted_id
    result = setQuestionAnswered(questionId)
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
        }

    @apiUse Errors

    """
    try:
        result = dumps(db.questions.find({"articleId": int(articleId)}))
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
            "articleId":"{articleId}"
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

def setQuestionAnswered(questionId):
    try:
        result = dumps(db.questions.find_one_and_update( {"_id": bson.ObjectId(questionId)}, { '$set': { "answered" : True } },))
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