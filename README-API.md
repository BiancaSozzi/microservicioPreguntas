<a name="top"></a>
# Questions Service v0.0.0

Microservicio de Preguntas

- [Preguntas](#preguntas)
	- [Obtener preguntas de un artículo](#obtener-preguntas-de-un-artículo)
	- [Obtener preguntas de un usuario](#obtener-preguntas-de-un-usuario)
	- [Crear Pregunta](#crear-pregunta)
	
- [RabbitMQ_GET](#rabbitmq_get)
	- [Logout](#logout)
	
- [RabbitMQ_POST](#rabbitmq_post)
	- [Notificar pregunta contestada](#notificar-pregunta-contestada)
	
- [Respuestas](#respuestas)
	- [Buscar Respuestas de una pregunta](#buscar-respuestas-de-una-pregunta)
	- [Crear Respuesta](#crear-respuesta)
	


# <a name='preguntas'></a> Preguntas

## <a name='obtener-preguntas-de-un-artículo'></a> Obtener preguntas de un artículo
[Back to top](#top)



	GET /v1/questions/:articleId



### Examples

Header Autorización

```
Authorization=bearer {token}
```


### Success Response

Respuesta

```
HTTP/1.1 200 OK
{
    "_id":"{id de la pregunta}",
    "question": "{contenido de la pregunta}",
    "userId": "{User Id}",
    "created": "{Fecha creada}",
    "answered": "{si tiene respuesta}",
    "articleId":"{articleId}"
    "answer": "{respuesta - si tiene}"
}
```


### Error Response

401 Unauthorized

```
HTTP/1.1 401 Unauthorized
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
404 Not Found

```
HTTP/1.1 404 Not Found
{
    "error": "{Motivo del error}"
}
```
## <a name='obtener-preguntas-de-un-usuario'></a> Obtener preguntas de un usuario
[Back to top](#top)



	GET /v1/questions/:userId



### Examples

Header Autorización

```
Authorization=bearer {token}
```


### Success Response

Respuesta

```
HTTP/1.1 200 OK
{
    "_id":"{id de la pregunta}",
    "question": "{contenido de la pregunta}",
    "userId": "{User Id}",
    "created": "{Fecha creada}",
    "answered": "{si tiene respuesta}",
    "articleId":"{articleId}",
    "answer":"{respuesta - si tiene respuesta}"
}
```


### Error Response

401 Unauthorized

```
HTTP/1.1 401 Unauthorized
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
404 Not Found

```
HTTP/1.1 404 Not Found
{
    "error": "{Motivo del error}"
}
```
## <a name='crear-pregunta'></a> Crear Pregunta
[Back to top](#top)



	POST /v1/questions/



### Examples

Body

```
{
    "question": "{ contenido de la pregunta }",
    "articleId": "{ articleId }"
}
```
Header Autorización

```
Authorization=bearer {token}
```


### Success Response

Respuesta

```
HTTP/1.1 200 OK
{
    "_id":"{id de la pregunta}",
    "question": "{contenido de la pregunta}",
    "userId": "{User Id}",
    "created": "{Fecha creada}",
    "answered": "{si tiene respuesta}",
    "articleId":"{articleId}"
}
```


### Error Response

401 Unauthorized

```
HTTP/1.1 401 Unauthorized
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
404 Not Found

```
HTTP/1.1 404 Not Found
{
    "error": "{Motivo del error}"
}
```
# <a name='rabbitmq_get'></a> RabbitMQ_GET

## <a name='logout'></a> Logout
[Back to top](#top)

<p>Escucha de mensajes logout desde auth. Invalida sesiones en cache.</p>

	FANOUT auth/logout



### Examples

Mensaje

```
{
  "type": "fanout",
  "message" : "tokenId"
}
```




# <a name='rabbitmq_post'></a> RabbitMQ_POST

## <a name='notificar-pregunta-contestada'></a> Notificar pregunta contestada
[Back to top](#top)

<p>Notifica al servicio de notificaciones cuando una pregunta ha sido contestada</p>

	FANOUT notifications/question-data



### Examples

Mensaje

```
{
  "type": "fanout",
  "message" : {
      "userQuestionId" : "{id del usuario que realizó la pregunta}",
      "userAnswerId": "{id del usuario que contestó la pregunta}",
      "question": "{pregunta realizada}"
      "answer": "{respuesta}"
  }
}
```




# <a name='respuestas'></a> Respuestas

## <a name='buscar-respuestas-de-una-pregunta'></a> Buscar Respuestas de una pregunta
[Back to top](#top)



	GET /v1/questions/:questioId/answers



### Examples

Header Autorización

```
Authorization=bearer {token}
```


### Success Response

Respuesta

```
HTTP/1.1 200 OK
{
    "_id":"{id de la respuesta}",
    "answer": "{contenido de la respuesta}",
    "userId": "{User Id}",
    "created": "{Fecha creada}",
    "articleId":"{articleId}"
}
```


### Error Response

401 Unauthorized

```
HTTP/1.1 401 Unauthorized
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
404 Not Found

```
HTTP/1.1 404 Not Found
{
    "error": "{Motivo del error}"
}
```
## <a name='crear-respuesta'></a> Crear Respuesta
[Back to top](#top)



	POST /v1/questions/:questionId/answers



### Examples

Body

```
{
    "answer": "{ contenido de la respuesta }",
}
```
Header Autorización

```
Authorization=bearer {token}
```


### Success Response

Respuesta

```
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
```


### Error Response

401 Unauthorized

```
HTTP/1.1 401 Unauthorized
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
404 Not Found

```
HTTP/1.1 404 Not Found
{
    "error": "{Motivo del error}"
}
```
