<a name="top"></a>
#Questions Service v0.0.1

Microservicio de Preguntas

-[Preguntas](#preguntas)
    -[Crear Pregunta](#crear-pregunta)
    -[Modificar Pregunta](#modificar-pregunta)
    -[Responder Pregunta](#responder-pregunta)
    -[Buscar Preguntas por Articulo](#buscar-preguntas-por-articulo)
    -[Buscar Preguntas por usuario](#buscar-preguntas-por-usuario)
    -[Buscar Pregunta por Id](#buscar-pregunta-por-id)
    -[Eliminar Pregunta](#eliminar-pregunta)

-[RabbitMQ_GET](#rabbitmq_get)
    -[Validacion de Articulo](#validación-de-artículo)
    -[Logout](#logout)
    -[Notificar Respuesta](#notificar-respuesta)

# <a name='preguntas'></a> Preguntas

## <a name='crear-pregunta'></a> Crear Pregunta
[Back to top](#top)



	POST /v1/questions/


###E xamples

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
    "question": "{contenido de la pregunta}",
    "userId": "{User Id}",
    "created": "{Fecha creada}",
    "updated": "{Fecha modificacion}",
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

## <a name='modificar-pregunta'></a> Modificar Pregunta
[Back to top](#top)



	POST /v1/questions/:questionId


### Examples

Body
```
{
    "question": "{contenido de la pregunta}",
    "userId": "{User Id}",
    "articleId":"{articleId}"
}
```

Header Autorización

```
Authorization=bearer {token}
```

### Success Response


## <a name='responder-pregunta'></a> Responder Pregunta
## <a name='crear-pregunta'></a> Crear Pregunta
## <a name='buscar-preguntas-por-articulo'></a> Buscar Pregunta por artículo
## <a name='buscar-preguntas-por-usuario'></a> Buscar Pregunta por usuario
## <a name='buscar-pregunta-por-id'></a> Buscar Pregunta por Id
## <a name='eliminar-pregunta'></a> Eliminar Pregunta


