# Controlador REST Proyecto para gestión de curriculums

Proyecto de la asignatura de programación concurrente y de tiempo real impartida en la [Universidad Europea de Madrid(UEM)](http://madrid.universidadeuropea.es) (3er curso) que forma parte del proyecto integrador desarrollado para [Everis](http://www.everis.com/spain/).
En esta asignatura se ha desarrollado el controlador REST para la gestión y clasificación de curriculums.

## Documentación online de la API

La documentación de la API se ha generado con [Swagger](http://swagger.io/): [Documentación API](http://51.255.202.84:8080/swagger-ui.html)

## Uso

### Búsqueda de curriculums por parámetros

```java
http://51.255.202.84:8080/buscador/<id>?nombre=&dni=&empresa=&direccion=&tecnologia=&idiomas=
```

### Descarga de curriculum

```java
http://51.255.202.84:8080/descargas/<id>
```

### Mostrar json parseado indexado en Elastic Search

```java
http://51.255.202.84:8080/curriculums/<id>
```
