<?php
require_once 'database.php';

function crearUsuario($nombre, $password, $permisos)
{
    if (Database::isUser($nombre)) {
        Database::insertData($nombre, $password, $permisos);
        return true;
    } else {
        return false;
    }
}

function borrarUsuario($nombre)
{
    if (Database::isUser($nombre)) {
        Database::removeData($nombre);
        return true;
    } else {
        return false;
    }
}

function increaseSearch()
{
    Database::increaseSearchDb();
}

function checkCv()
{
    $files = scandir('');
}

?>
