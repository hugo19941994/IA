<?php session_start(); ?>
<!DOCTYPE html>
<html dir="ltr" lang="es">
<head>
    <title>Everis - Gestor de curriculums</title>

    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta name="author" content="jdecastroc" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato:300,400,400italic,600,700|Raleway:300,400,500,600,700|Crete+Round:400italic" type="text/css">
    <link rel="stylesheet" href="css/bootstrap.min.css" type="text/css">
    <link rel="stylesheet" href="style.min.css" type="text/css">
    <link rel="stylesheet" href="css/swiper.css" type="text/css">
    <link rel="stylesheet" href="css/dark.min.css" type="text/css">
    <link rel="stylesheet" href="css/font-icons.css" type="text/css">
    <link rel="stylesheet" href="css/animate.min.css" type="text/css">
    <link rel="stylesheet" href="css/magnific-popup.css" type="text/css">
    <link rel="stylesheet" href="css/responsive.css" type="text/css">

    <link rel="icon" href="favicon.ico">
</head>

<?php
require 'functions.php';
$lang = "es";
$allowed = false;
if (isset($_SESSION["usuario"]) && isset($_SESSION["password"])) {
    $usuario = $_SESSION["usuario"];
    $password = $_SESSION["password"];
    $db = mysqli_connect('mysql', $_ENV["DBUSR"], $_ENV["DBPWD"], 'everis_cv')
        or die('Error conectando al servidor de base de datos.');

    $query = "SELECT * FROM usuarios";
    $result = mysqli_query($db, $query);
    while ($row = mysqli_fetch_array($result)) {
        if (($usuario == $row['nombre']) && ($password ==  $row['password'])) {
            $allowed = true;
            $nombre_db = $row['nombre'];
            $password_db = $row['password'];
            $permisos_db = $row['permisos'];
        }
    }
}
?>

<body class="stretched side-header">
    <div id="wrapper" class="clearfix">

      <header id="header" class="no-sticky">
            <div id="header-wrap">
                <div class="container clearfix">
                    <div id="primary-menu-trigger"><i class="icon-reorder"></i></div>
                    <div id="logo" class="nobottomborder">
                        <a href="index.php" class="standard-logo" data-dark-logo="img/logo-everis.png"><img src="img/logo-everis.png" alt="Everis logo"></a>
                    </div>

                    <nav id="primary-menu">
                        <ul>
                            <li><a href="index.php"><div>Índice</div></a></li>
                            <li><a href="gestor.php"><div>Gestión de repositorio</div></a></li>
                            <li class="current"><a href="buscador.php"><div>Búsqueda de CV</div></a></li>
                            <?php
                            if ($allowed && $permisos_db == "administrador") {
                            ?>
                            <li><a href="usuarios.php"><div>Gestión de usuarios</div></a></li>
                            <br><br>
                            <?php } ?>
                            <li><a href="ayuda.php"><div>Ayuda</div></a></li>
                            <li><a href="contacto.php"><div>Contacto</div></a></li>
                        </ul>
                    </nav>

                    <div class="clearfix visible-md visible-lg">
                        <a href="https://github.com/hugo19941994/CV-Parser" class="social-icon si-small si-borderless si-github">
                            <i class="icon-github"></i>
                            <i class="icon-github"></i>
                        </a>
                    </div>
                </div>
            </div>
        </header>

        <section id="content">
            <div class="content-wrap">

                <div class="promo promo-full promo-border header-stick bottommargin-lg">
                    <div class="container clearfix">
                        <h3>Buscador de curriculums</h3>
                        <span>Añada las opciones necesarias para realizar la búsqueda de manera general o más precisa.</span>
                    </div>
                </div>

                <div class="container clearfix">
                    <?php
                        if ($allowed) {
                    ?>
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-title text-center">Busqueda de Curriculums</div>
                        </div>

                        <div id="collapse2" class="panel-collapse collapse in">
                            <div id="contenedorOpcional" class="panel-body">
                                <div class="text-center">
                                    <a id="volverBuscar" name="buscar" class="button button-xlarge tright">Volver a buscar<i class="icon-refresh"></i></a>
                                </div>
                            </div>

                            <div id="formularioBusqueda" class="panel-body text-center form-horizontal">
                                <div class="col_half">
                                    <h4>Parámetros de búsqueda</h4>

                                    <label class="col-md-6 control-label" for="nombre">Nombre</label>
                                    <div class="col-md-6">
                                        <input id="nombre" name="nombre" type="text" placeholder="" class="input-md">
                                        <button class="btn btn-success btn-number" id="addNombre" type="button" style="display: inline-block;">
                                            <i class="icon-line-circle-plus"></i>
                                        </button>
                                    </div>
                                    <br><br>

                                    <label class="col-md-6 control-label" for="dni">DNI</label>
                                    <div class="col-md-6">
                                        <input id="dni" name="dni" type="text" placeholder="" class="input-md">
                                        <button class="btn btn-success btn-number" id="addDNI" type="button" style="display: inline-block;">
                                            <i class="icon-line-circle-plus"></i>
                                        </button>
                                    </div>
                                    <br><br>

                                    <label class="col-md-6 control-label" for="empresa">Empresa</label>
                                    <div class="col-md-6">
                                        <input id="empresa" name="empresa" type="text" placeholder="" class="input-md">
                                        <button class="btn btn-success btn-number" id="addEmpresa" type="button" style="display: inline-block;">
                                            <i class="icon-line-circle-plus"></i>
                                        </button>
                                    </div>
                                    <br><br>

                                    <label class="col-md-6 control-label" for="direccion">Dirección</label>
                                    <div class="col-md-6">
                                        <input id="direccion" name="direccion" type="text" placeholder="" class="input-md">
                                        <button class="btn btn-success btn-number" id="addDireccion" type="button" style="display: inline-block;">
                                            <i class="icon-line-circle-plus"></i>
                                        </button>
                                    </div>
                                    <br><br>

                                    <label class="col-md-6 control-label" for="tecnologia">Estudios</label>
                                    <div class="col-md-6">
                                        <input id="habilidad" name="habilidad" type="text" placeholder="" class="input-md">
                                        <button class="btn btn-success btn-number" id="addHabilidad" type="button" style="display: inline-block;">
                                            <i class="icon-line-circle-plus"></i>
                                        </button>
                                    </div>
                                    <br><br>

                                    <label class="col-md-6 control-label" for="tecnologia">Tecnologias</label>
                                    <div class="col-md-6">
                                        <input id="tecnologia" name="tecnologia" type="text" placeholder="" class="input-md">
                                        <button class="btn btn-success btn-number" id="addTecnologia" type="button" style="display: inline-block;">
                                            <i class="icon-line-circle-plus"></i>
                                        </button>
                                    </div>
                                    <br><br>

                                    <label class="col-md-6 control-label" for="idiomas">Idiomas</label>
                                    <div class="col-md-6">
                                          <input id="idiomas" name="idiomas" type="text" placeholder="" class="typeahead tt-input">
                                          <button class="btn btn-success btn-number" id="addIdioma" type="button" style="display: inline-block;">
                                              <i class="icon-line-circle-plus"></i>
                                          </button>
                                    </div>
                                    <br><br>

                                    <label class="col-md-4 control-label" for="buscar"></label>
                                </div>

                                <div class="col_half col_last">
                                  <h4>Consulta</h4>
                                  <div id="nombresConsulta"></div>
                                  <div id="dniConsulta" style="margin-top: 1%;"></div>
                                  <div id="empresasConsulta" style="margin-top: 1%;"></div>
                                  <div id="direccionesConsulta" style="margin-top: 1%;"></div>
                                  <div id="habilidadesConsulta" style="margin-top: 1%;"></div>
                                  <div id="tecnologiasConsulta" style="margin-top: 1%;"></div>
                                  <div id="idiomasConsulta" style="margin-top: 1%;"></div>
                                </div>

                                <div class="col_full">
                                    <a id="buscarAhora" name="buscarp" class="button button-xlarge tright">Iniciar búsqueda<i class="icon-circle-arrow-right"></i></a>
                                </div>

                            </div>
                        </div>
                    </div>

                    <div id="panelBusquedas" class="panel panel-default">
                        <div class="panel-body">
                            <div id="contenidoBusqueda"></div>
                            </tbody>
                            </table>
                        </div>
                    </div>

                    <?php } else { ?>

                    <div class="col_full">
                        <div>
                            <h3>Usuario incorrecto</h3>
                            <p>Usted no tiene acceso para ver esta página. Vuelva a la pantalla de acceso para entrar con el usuario proporcionado por el administrador del sistema.</p>
                        </div>
                    </div>
                    <?php } ?>
                </div>
            </div>
        </section>
    </div>
    <div id="seccionError"></div>

    <script type="text/javascript" src="js/jquery.js"></script>
    <script type="text/javascript" src="js/plugins.js"></script>
    <script type="text/javascript" src="js/busqueda.js"></script>
    <script type="text/javascript" src="js/functions.js"></script>

</body>
</html>
