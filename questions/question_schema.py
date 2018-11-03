import numbers
import datetime
# import utils.schema_validator as validator
import utils.errors as errors
import socket
import http.client
import utils.config as config
import utils.json_serializer as json
import questions.answer_schema as answer

QUESTION_DB_SCHEMA = {
    "question": {
        "required": True,
        "type": str,
        "minLen": 1,
        "maxLen": 500,
    },
    "answer":{
        "required":False,
        "type": answer,
    }

}

def newQuestion(authKey, params):

    conn = http.client.HTTPConnection(
        socket.gethostbyname(config.get_security_server_url()),
        config.get_security_server_port(),
    )

    headers = {"Authorization".encode("utf-8"): authKey.encode("utf-8")}

    conn.request("GET", "/v1/users/current", {}, headers)
    response = conn.getresponse()
    result = json.body_to_dic(response.read().decode('utf-8'))

    return {
        "question": params['question'],
        "userId":result['id'],
        "created": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'),
        "answered": False,
        "articleId": params['articleId'],
        "answer": None
    }