<a name="top"></a>

# Microservicio de Preguntas
# Questions Service v0.0.1

-[Preguntas](#preguntas)
    -[Crear Pregunta](#crear-pregunta)
    -[Responder Pregunta](#responder-pregunta)
    -[Buscar Preguntas por Articulo](#buscar-preguntas-por-articulo)
    -[Buscar Preguntas por usuario](#buscar-preguntas-por-usuario)
    -[Buscar Pregunta por Id](#buscar-pregunta-por-id)
    -[Buscar Respuesta por pregunta](#buscar-respuesta-por-pregunta)
    -[Eliminar Pregunta](#eliminar-pregunta)
    -[Eliminar Respuesta](#eliminar-respuesta)

-[RabbitMQ_GET](#rabbitmq_get)
    -[Validacion de Articulo](#validación-de-artículos)
    -[Logout](#logout)

-[RabbitMQ_POST](#rabbitmq_post)
    -[Notificar Respuesta](#notificar-respuesta)

# <a name='preguntas'></a> Preguntas

## <a name='crear-pregunta'></a> Crear Pregunta
[Back to top](#top)



	POST /v1/questions/


### Examples

Body

```
{
    "question": "{contenido de la pregunta}",
    "userId": "{User Id}",
    "articleId":"{articleId}"
}

```

Header Autorizacion
```
Authorization=bearer {token}
```

### Success Response
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

## <a name='responder-pregunta'></a> Responder Pregunta

[Back to top](#top)



	POST /v1/questions/:questionId/answers


### Examples

Body

```
{
    "answer": "{contenido de la respuesta}",
    "userId": "{User Id}",
    "articleId":"{articleId}",
    "questionId":"{pregunta a la que corresponde la respuesta}"
}

```

Header Autorizacion
```
Authorization=bearer {token}
```

### Success Response
```
HTTP/1.1 200 OK
{
    "_id":"{id de la respuesta}",
    "answer": "{contenido de la respuesta}",
    "userId": "{User Id}",
    "created": "{Fecha creada}",
    "articleId":"{articleId}",
    "questionId":"{pregunta a la que corresponde la respuesta}"
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

## <a name='buscar-preguntas-por-articulo'></a> Buscar Pregunta por artículo
[Back to top](#top)

GET /v1/questions/:articleId

### Success Response

Respuesta

```
HTTP/1.1 200 OK
{
    "_id": "{id de la pregunta}"
    "question": "{descripción del articulo}",
    "userId": "{User Id}",
    "created": "{Fecha creada}",
    "answered": "{si tiene respuesta}",
    "articleId":"{articleId}"
}
```

### Error Response

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

## <a name='buscar-preguntas-por-usuario'></a> Buscar Pregunta por usuario
[Back to top](#top)

GET /v1/questions/:userId


### Success Response

Respuesta

```
HTTP/1.1 200 OK
{
    "_id": "{id de la pregunta}"
    "question": "{descripción del articulo}",
    "userId": "{User Id}",
    "created": "{Fecha creada}",
    "answered": "{si tiene respuesta}",
    "articleId":"{articleId}"
}
```

### Error Response

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

## <a name='buscar-pregunta-por-id'></a> Buscar Pregunta por Id
[Back to top](#top)

GET /v1/questions/:questionId


### Success Response

Respuesta

```
HTTP/1.1 200 OK
{
    "_id": "{id de la pregunta}"
    "question": "{descripción del articulo}",
    "userId": "{User Id}",
    "created": "{Fecha creada}",
    "answered": "{si tiene respuesta}",
    "articleId":"{articleId}"
}
```

### Error Response

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
## <a name='buscar-respuesta-por-pregunta'></a> Buscar Respuesta por Pregunta
[Back to top](#top)

GET /v1/questions/:questioId/answers


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
## <a name='eliminar-pregunta'></a> Eliminar Pregunta
[Back to top](#top)



	DELETE /questions/:questionId



### Examples

Header Autorización

```
Authorization=bearer {token}
```


### Success Response

200 Respuesta

```
HTTP/1.1 200 OK
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
## <a name='eliminar-respuesta'></a> Eliminar Respuesta
[Back to top](#top)



	DELETE /questions/:questioId/:answerId



### Examples

Header Autorización

```
Authorization=bearer {token}
```


### Success Response

200 Respuesta

```
HTTP/1.1 200 OK
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

# <a name='rabbitmq_get'></a> RabbitMQ_GET

## <a name='validación-de-articulos'></a> Validación de Articulos
[Back to top](#top)

<p>Escucha de mensajes article-exist desde cart. Valida articulos</p>

	DIRECT catalog/article-exist



### Examples

Mensaje

```
{
  "type": "article-exist",
  "exchange" : "{Exchange name to reply}"
  "queue" : "{Queue name to reply}"
  "message" : {
      "referenceId": "{referenceId}",
      "articleId": "{articleId}",
  }
```
## <a name='logout'></a> Logout
[Back to top](#top)

<p>Escucha de mensajes logout desde auth. Invalida sesiones en cache.</p>

	FANOUT auth/logout



### Examples
Mensaje

```
{
   "type": "logout",
   "message": "{tokenId}"
}
```


# <a name='rabbitmq_post'></a> RabbitMQ_POST

## <a name='notificar-respuesta'></a> Notificar Respuesta
[Back to top](#top)

<p>Notifica Respuesta de preguntas</p>

DIRECT mail/question-answered

### Success Response

Mensaje

```
{
    "type":"question-answered",
    "message":{
        "userQuestionEmail": {mail from who asked the question},
        "userAnswerEmail": {mail from who answered the question},
        "questio":"{question}", 
        "answer":"{answer}",
    }
}
