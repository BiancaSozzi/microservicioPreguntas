#coding = utf_8

import flask
import questions.crud_service as crud
import utils.json_serializer as json
import utils.errors as errors
import utils.security as security
# import articles.rest_validations as restValidator


def init(app):
    """
    Inicializa las rutas para Articulos\n
    app: Flask
    """


    @app.route('/v1/questions', methods=['POST'])
    def addQuestion():
        # Solo puede realizar una pregunta un usuario loggeado
        
        try:
            token = flask.request.headers.get("Authorization")
            security.isValidToken(token)
            params = json.body_to_dic(flask.request.data)
            result = crud.addQuestion(params, token)
            return json.dic_to_json(result)
        except Exception as err:
            return errors.handleError(err)

    @app.route('/v1/questions/<questionId>/answers', methods=['POST'])
    def answerQuestion(questionId):
        #Solo puede responder una pregunta el admin
        try:
            token = flask.request.headers.get("Authorization")
            security.validateAdminRole(token)
            params = json.body_to_dic(flask.request.data)
            result = crud.addAnswer(params, questionId, token)
            return json.dic_to_json(result)
        except Exception as err:
            return errors.handleError(err)

 
    @app.route('/v1/questions/article/<articleId>', methods=['GET'])
    def getQuestionByArticle(articleId):
        try:
            response = crud.getQuestionByArticle(articleId)
            return response
        except Exception as err:
            return errors.handleError(err)
 

    @app.route('/v1/questions/user/<userId>', methods=['GET'])
    def getQuestionByUser(userId):
        try:
            response = crud.getQuestionByUser(userId)
            return response
        except Exception as err:
            return errors.handleError(err)


    @app.route('/v1/questions/<questionId>/answers', methods=['GET'])
    def getAnswersByQuestion(questionId):
        try:
            response = crud.getAnswersByQuestion(questionId)
            return response
        except Exception as err:
            return errors.handleError(err)
