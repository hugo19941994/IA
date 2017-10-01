<?php
class Database
{
    private static $_dbName = 'everis_cv' ;
    private static $_dbHost = 'localhost' ; //Changed for localhost requests

    private static $_cont  = null;

    public function __construct()
    {
        die('La funcion Init no está permitida');
    }

    public static function connect()
    {
        // One connection through whole application
        if (null == self::$_cont) {
            try {
                self::$_cont = new PDO("mysql:host=".self::$_dbHost.";"."dbname=".self::$_dbName, $_ENV["DBUSR"], $_ENV["DBPWD"]);
            } catch(PDOException $e) {
                die($e->getMessage());
            }
        }
        return self::$_cont;
    }

    public static function disconnect()
    {
        self::$_cont = null;
    }

    public static function isUser($usuario)
    {
        $pdo = Database::connect();
        $sql = 'SELECT ' + $usuario + ' FROM usuarios';
        $result = $pdo->query($sql);
        if ($result->num_rows = 0) {
            Database::disconnect();
            return false;
        } else {
            Database::disconnect();
            return true;
        }
    }

    public static function insertData($usuario, $password, $permisos)
    {
        $pdo = Database::connect();
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $sql = "INSERT INTO usuarios (nombre,password,permisos) values(?, ?, ?)";
        $q = $pdo->prepare($sql);
        $q->execute(array($usuario,$password,$permisos));
        Database::disconnect();
    }

    public static function removeData($usuario)
    {
        $pdo = Database::connect();
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $sql = "DELETE FROM usuarios WHERE nombre = ?";
        $q = $pdo->prepare($sql);
        $q->execute(array($usuario));
        Database::disconnect();
    }

    public static function increaseSearchDb()
    {
        $pdo = Database::connect();
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $sql = "UPDATE metricas SET busquedas = busquedas + 1";
        $q = $pdo->prepare($sql);
        $q->execute();
        Database::disconnect();
    }
}
?>
