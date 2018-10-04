# Microservicio de Preguntas (Questions)

Es un microservicio que permite a los usuarios realizar consultas sobre los artículos del Catálogo.

## Microservicios Relacionados - Dependencias

El microservicio Questions se comunica con:

### Auth
Sólo los usuarios loggeados pueden realizar o responder una pregunta. Solo un usuario "admin" puede responder las preguntas. Por lo tanto, el servicio de Auth se utilizará para:

-Verificar si el usuario está loggeado y la sesión es válida.
 
-Identificar al usuario que realiza o responde una pregunta.

-Asegurarse que el usuario es admin para poder responder una pregunta.

### Catalog
Una pregunta etá asociada a un artículo determinado. Por lo que el servicio de Catálogo será utilizado para identificar dicho artículo. Debe validarse que el artículo exista antes de guardar la pregunta.


### Mail
Cada vez que una respuesta sea contestada, deberá notificarse al usuario que realizó la pregunta. Es necesario comunicarse con Auth para saber a qué usuario se le debe notificar.

### RabbitMQ
Se utilizará como medio de comunicación entre el servicio de preguntas y:

    -Catalog

    -Auth

    -Mail

## Herramientas de desarrollo

#### Python3 
    -Lenguaje de Programación

#### Flask
    -Framework de desarollo

#### MongoDB
    -Base de Datos

## Casos de Uso

### Crear Pregunta
Un usuario realiza una pregunta sobre un artículo del catálogo

### Responder 
Un usuario puede responder a una pregunta en un artículo.

### Visualizar un artículo con sus preguntas
Si un usuario ve un artículo puede ver las preguntas realizadas sobre el. El microservicio catalog debería consultar a questions si ese artículo tiene preguntas, y mostrarlas en caso de que existieran.

### Ver preguntas realizadas
El usuario puede ver las preguntas que ha realizado.


### Ver respuestas de preguntas
El usuario puede ver la respuesta de una pregunta.

### Eliminar Pregunta
Un usuario puede eliminar la pregunta que realizó. 

### Eliminar Respuest
Un usuario puede eliminar su respuesta

## Entidades

### Question
-id

-answered

-question

-articleId

-userId

-created

### Answer
-id

-answer

-created

-userId

-questionId