<?php
class Database
{
    private static $dbName = 'everis_cv' ;
    private static $dbHost = 'localhost' ; //Changed for localhost requests
    private static $dbUsername = 'root';
    private static $dbUserPassword = 'universal';

    private static $cont  = null;

    public function __construct() {
        die('La funcion Init no está permitida');
    }

    public static function connect()
    {
       // One connection through whole application
       if ( null == self::$cont )
       {
        try
        {
          self::$cont =  new PDO( "mysql:host=".self::$dbHost.";"."dbname=".self::$dbName, self::$dbUsername, self::$dbUserPassword);
        }
        catch(PDOException $e)
        {
          die($e->getMessage());
        }
       }
       return self::$cont;
    }

    public static function disconnect()
    {
        self::$cont = null;
    }

    public static function isUser($usuario)
    {
      $pdo = Database::connect();
      $sql = 'SELECT ' + $usuario + ' FROM usuarios';
      $result = $pdo->query($sql);
      if ($result->num_rows = 0)
      {
        Database::disconnect();
        return false;
      }
      else
      {
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
      $sql = "DELETE FROM usuarios  WHERE nombre = ?";
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
