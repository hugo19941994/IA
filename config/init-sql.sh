#!/bin/bash

DBRPWD=$(openssl rand -base64 64)

mysql -uroot <<QUERY_INPUT
ALTER USER 'root'@'localhost' IDENTIFIED BY '$DBRPWD';
CREATE USER '$DBUSR'@'%' IDENTIFIED BY '$DBPWD';

CREATE DATABASE everis_cv;
USE everis_cv;
CREATE TABLE usuarios (nombre VARCHAR(40), password VARCHAR(40), permisos VARCHAR(40));
CREATE TABLE metricas (busquedas INT NOT NULL);
INSERT INTO usuarios VALUES ("$CVUSR", "$CVPWD", "administrador");

GRANT ALL PRIVILEGES ON everis_cv.* TO '$DBUSR'@'%';
FLUSH PRIVILEGES;
QUERY_INPUT
