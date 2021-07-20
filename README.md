# CasaAdmin
Administrador general de la casa enfocado a las finanzas
## Develop
### Sobre el desarrollo
#### Docker (Versión 3.3.3)
- Contenedor mysql: (Mysql:8.0 [DockerHub](https://hub.docker.com/layers/mysql/library/mysql/8.0/images/sha256-68b207d01891915410db3b5bc1f69963e3dc8f23813fd01e61e6d7e7e3a46680?context=explore)): Base de datos MySql
    - Volumes:
        - data (Docker/Mysql/data): contenido de la base de datos para mantener persistencia aun cuando se baja o elimina contenedor.
        - rollback (Docker/Mysql/rollback): Permite subir dumps de base de datos de forma rapida.

- Contenedor web: (Python:3 [DockerHub](https://hub.docker.com/layers/python/library/python/3/images/sha256-593703a76f19405f22c3c0b6c7bed36f9764052b701c21ee85046edf95c3edab?context=explore) Se eligió basado en [esto](https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d). 
    - Se piensa cambiar a slime o alpine
    - Volumes:
        - src (Docker/Web/src): Contiene el código fuente
#### Python (Versión 3)
- Django>=3.0,<4.0
- mysqlclient==2.0.3
- django-bootstrap4-form==4.0.1
### Bitacora de desarrollo
- Se crea contenedores docker mysql y web. Problema al levantar contenedor web, porque se levanta contenedor mysql, pero no esta preparado para resivir solicitudes. Se añade  [wait-for-it.sh](https://docs.docker.com/compose/startup-order/)

- Estructura de apps: Se crean las apps dentro de carpeta de proyecto (src/casadmin). nota: crear antes la carpeta de la app porque django no la crea automaticamente. nota2: se debe añadir en el archivo apps.py la ruta a la app[Referencia (opción 2)](https://rajasimon.io/blog/django-project-structure/)

- Estructura templates: Se crea una carpeta `templates` a nivel de la carpeta de proyecto que contiene todos los templates del proyecto (se añade la referencia en settings) [Referencia (opción 2)](https://learndjango.com/tutorials/template-structure)

- se consideran las recomentaciones de [Referencia](https://steelkiwi.medium.com/best-practices-working-with-django-models-in-python-b17d98ab92b) para crear los modelos

- Estructura statics: por orden los statics van dentro de cada app y cuando se necesitan se hace un collectstatic

- Se creo un mixin que va en el core para acelerar el crear futuros CRUD's con vistas basadas en clases.
    DefaultCRUD: retorna nombres de modelo y rutas a las acciones de ese modelo
    Delete: se añadio un eliminado logico [Referencia](https://adriennedomingus.com/blog/soft-deletion-in-django)

### Problemas comunes en el desarrollo
- Docker levanta contenedor mysql, sin embargo, no se levanta servicio antes que django lo requiera y proboca que el contenedor `web` no levante, porque django no puede conectar con la base de datos

    Solución: se implemento archivo `wait-for-it.sh` que hace ping a mysql hasta que se levantay permite continuar con levantar django. se invoca `bash -c "/wait-for-it.sh --timeout=0 mysql:3306`. [Referencia](https://docs.docker.com/compose/startup-order/)