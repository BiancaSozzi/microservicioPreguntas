define({ "api": [
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./public/main.js",
    "group": "D__Arq__de_microservicios_Dise_o_Microservicio_microservicioPreguntas_public_main_js",
    "groupTitle": "D__Arq__de_microservicios_Dise_o_Microservicio_microservicioPreguntas_public_main_js",
    "name": ""
  },
  {
    "type": "get",
    "url": "/v1/questions/:articleId",
    "title": "Obtener preguntas de un artículo",
    "name": "Buscar_preguntas_por_art_culo",
    "group": "Preguntas",
    "success": {
      "examples": [
        {
          "title": "Respuesta",
          "content": "HTTP/1.1 200 OK\n{\n    \"_id\":\"{id de la pregunta}\",\n    \"question\": \"{contenido de la pregunta}\",\n    \"userId\": \"{User Id}\",\n    \"created\": \"{Fecha creada}\",\n    \"answered\": \"{si tiene respuesta}\",\n    \"articleId\":\"{articleId}\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./questions/crud_service.py",
    "groupTitle": "Preguntas",
    "examples": [
      {
        "title": "Header Autorización",
        "content": "Authorization=bearer {token}",
        "type": "String"
      }
    ],
    "error": {
      "examples": [
        {
          "title": "401 Unauthorized",
          "content": "HTTP/1.1 401 Unauthorized",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/v1/questions/:userId",
    "title": "Obtener preguntas de un usuario",
    "name": "Buscar_preguntas_por_usuario",
    "group": "Preguntas",
    "success": {
      "examples": [
        {
          "title": "Respuesta",
          "content": "HTTP/1.1 200 OK\n{\n    \"_id\":\"{id de la pregunta}\",\n    \"question\": \"{contenido de la pregunta}\",\n    \"userId\": \"{User Id}\",\n    \"created\": \"{Fecha creada}\",\n    \"answered\": \"{si tiene respuesta}\",\n    \"articleId\":\"{articleId}\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./questions/crud_service.py",
    "groupTitle": "Preguntas",
    "examples": [
      {
        "title": "Header Autorización",
        "content": "Authorization=bearer {token}",
        "type": "String"
      }
    ],
    "error": {
      "examples": [
        {
          "title": "401 Unauthorized",
          "content": "HTTP/1.1 401 Unauthorized",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "post",
    "url": "/v1/questions/",
    "title": "Crear Pregunta",
    "name": "Crear_Pregunta",
    "group": "Preguntas",
    "examples": [
      {
        "title": "Body",
        "content": "{\n    \"question\": \"{ contenido de la pregunta }\",\n    \"articleId\": \"{ articleId }\"\n}",
        "type": "json"
      },
      {
        "title": "Header Autorización",
        "content": "Authorization=bearer {token}",
        "type": "String"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Respuesta",
          "content": "HTTP/1.1 200 OK\n{\n    \"_id\":\"{id de la pregunta}\",\n    \"question\": \"{contenido de la pregunta}\",\n    \"userId\": \"{User Id}\",\n    \"created\": \"{Fecha creada}\",\n    \"answered\": \"{si tiene respuesta}\",\n    \"articleId\":\"{articleId}\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./questions/crud_service.py",
    "groupTitle": "Preguntas",
    "error": {
      "examples": [
        {
          "title": "401 Unauthorized",
          "content": "HTTP/1.1 401 Unauthorized",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "fanout",
    "url": "auth/logout",
    "title": "Logout",
    "group": "RabbitMQ_GET",
    "description": "<p>Escucha de mensajes logout desde auth. Invalida sesiones en cache.</p>",
    "examples": [
      {
        "title": "Mensaje",
        "content": "{\n  \"type\": \"fanout\",\n  \"message\" : \"tokenId\"\n}",
        "type": "json"
      }
    ],
    "version": "0.0.0",
    "filename": "./rabbit/rabbit_service.py",
    "groupTitle": "RabbitMQ_GET",
    "name": "FanoutAuthLogout"
  },
  {
    "type": "get",
    "url": "/v1/questions/:questioId/answers",
    "title": "Buscar Respuestas de una pregunta",
    "name": "Buscar_respuestas_de_una_pregunta",
    "group": "Respuestas",
    "success": {
      "examples": [
        {
          "title": "Respuesta",
          "content": "HTTP/1.1 200 OK\n{\n    \"_id\":\"{id de la respuesta}\",\n    \"answer\": \"{contenido de la respuesta}\",\n    \"userId\": \"{User Id}\",\n    \"created\": \"{Fecha creada}\",\n    \"articleId\":\"{articleId}\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./questions/crud_service.py",
    "groupTitle": "Respuestas",
    "examples": [
      {
        "title": "Header Autorización",
        "content": "Authorization=bearer {token}",
        "type": "String"
      }
    ],
    "error": {
      "examples": [
        {
          "title": "401 Unauthorized",
          "content": "HTTP/1.1 401 Unauthorized",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "post",
    "url": "/v1/questions/:questionId/answers",
    "title": "Crear Respuesta",
    "name": "Crear_Respuesta",
    "group": "Respuestas",
    "examples": [
      {
        "title": "Body",
        "content": "{\n    \"answer\": \"{ contenido de la respuesta }\",\n    \"articleId\": \"{ articleId }\"\n}",
        "type": "json"
      },
      {
        "title": "Header Autorización",
        "content": "Authorization=bearer {token}",
        "type": "String"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "Respuesta",
          "content": "HTTP/1.1 200 OK\n{\n    \"_id\":\"{id de la respuesta}\",\n    \"answer\": \"{contenido de la respuesta}\",\n    \"userId\": \"{User Id}\",\n    \"created\": \"{Fecha creada}\",\n    \"articleId\":\"{articleId}\",\n    \"questionId\":\"{pregunta a la que corresponde la respuesta}\"     \n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./questions/crud_service.py",
    "groupTitle": "Respuestas",
    "error": {
      "examples": [
        {
          "title": "401 Unauthorized",
          "content": "HTTP/1.1 401 Unauthorized",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"path\" : \"{Nombre de la propiedad}\",\n    \"message\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "400 Bad Request",
          "content": "HTTP/1.1 400 Bad Request\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        },
        {
          "title": "500 Server Error",
          "content": "HTTP/1.1 500 Server Error\n{\n    \"error\" : \"{Motivo del error}\"\n}",
          "type": "json"
        }
      ]
    }
  }
] });
