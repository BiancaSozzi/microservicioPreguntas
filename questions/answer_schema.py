import numbers
import datetime
# import utils.schema_validator as validator
import utils.errors as errors
import socket
import http.client
import utils.config as config
import utils.json_serializer as json

QUESTION_DB_SCHEMA = {
    "answer": {
        "required": True,
        "type": str,
        "minLen": 1,
        "maxLen": 500,
    }
}

def newAnswer(authKey, params, question):
    
    conn = http.client.HTTPConnection(
        socket.gethostbyname(config.get_security_server_url()),
        config.get_security_server_port(),
    )

    headers = {"Authorization".encode("utf-8"): authKey.encode("utf-8")}

    conn.request("GET", "/v1/users/current", {}, headers)
    response = conn.getresponse()
    result = json.body_to_dic(response.read().decode('utf-8'))

    return {
        "answer": params['answer'],
        "userId":result['id'],
        "created": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "articleId": question['articleId'],
        "questionId": question['_id']['$oid']
    }