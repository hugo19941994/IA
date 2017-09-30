<?php
	session_start();
  require 'functions.php';
  $lang = "es";
	$allowed = false;
  if((isset($_SESSION["usuario"]) && isset($_SESSION["password"])) && $_SESSION["permisos"] == "administrador")
  {
      $usuario = $_SESSION["usuario"];
      $password = $_SESSION["password"];
			$db = mysqli_connect('mysql', $_ENV["DBUSR"], $_ENV["DBPWD"], 'everis_cv') or die('Error conectando al servidor de base de datos.');

			$query = "SELECT * FROM usuarios";
			$result = mysqli_query($db, $query);
			while ($row = mysqli_fetch_array($result)) {
				if (($usuario == $row['nombre']) && ($password ==  $row['password'])){
					$allowed = true;
					$nombre_db = $row['nombre'];
					$password_db = $row['password'];
					$permisos_db = $row['permisos'];
				}
			}

      if (isset($_POST['delete_id'])){
        $id = $_POST['delete_id'];
          if(!borrarUsuario($id)){
            //HACER ALGO CUANDO NO PUEDE BORRAR EL USUARIO PORQUE NO EXISTA O DE ERROR
          } else {
            //HACER ALGO CUANDO LO BORRE SATISFACTORIAMENTE (MODAL)
          }
      }

      if (isset($_POST['nuevoUsuario']) && isset($_POST['nuevaPassword']) && isset($_POST['nuevoPermiso'])){
        $nuevoUsuario = $_POST['nuevoUsuario'];
        $nuevaPassword = $_POST['nuevaPassword'];
        $nuevoPermiso = $_POST['nuevoPermiso'];
          if(crearUsuario($nuevoUsuario, $nuevaPassword, $nuevoPermiso)){

          } else {

          }
      }

      if (isset($_POST['function'])){
        $id = $_POST['function'];
          increaseSearch();
      }

  }
?>
