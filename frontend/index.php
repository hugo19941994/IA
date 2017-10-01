<?php session_start(); ?>
<!DOCTYPE html>
<html dir="ltr" lang="en-US">
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
$lang = "es";
$allowed = false;
if (isset($_POST['usuario']) && isset($_POST['password'])) {
    $usuario = $_POST['usuario'];
    $password = $_POST['password'];
    $_SESSION["usuario"] = $usuario;
    $_SESSION["password"] = $password;
}
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
            $_SESSION["permisos"] = $permisos_db;
        }
    }

    $result_search = mysqli_query($db, "SELECT busquedas FROM metricas");
    while ($row = mysqli_fetch_array($result_search)) {
        $numeroCv = $row['busquedas'];
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
                            <li class="current"><a href="index.php"><div>Índice</div></a></li>
                            <li><a href="gestor.php"><div>Gestión de repositorio</div></a></li>
                            <li><a href="buscador.php"><div>Búsqueda de CV</div></a></li>
                            <?php if ($allowed && $permisos_db == "administrador") { ?>
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
                        <h3>Bienvenido al gestor de curriculums de Everis</h3>
                        <span>Gestione los curriculums y ejecute búsquedas sobre los mismos para encontrar el personal adecuado para el puesto que necesita cubrir.</span>
                    </div>
                </div>

                <div class="container clearfix">

                <?php if ($allowed) { ?>

                <div class="widget clearfix">
                    <div class="row">
                        <div class="col_half bottommargin-sm">
                            <div class="counter counter-small"><span data-from="1" data-to="20" data-refresh-interval="80" data-speed="2000" data-comma="true"></span></div>
                            <h5 class="nobottommargin">Curriculums en el repositorio</h5>
                        </div>

                        <div class="col_half col_last bottommargin-sm">
                            <div class="counter counter-small"><span data-from="1" data-to="<?php echo $numeroCv; ?>" data-refresh-interval="50" data-speed="2000" data-comma="true"></span></div>
                            <h5 class="nobottommargin">Búsquedas realizadas</h5>
                        </div>
                    </div>
                </div>

                <div class="col_full">
                    <div>
                        <h3>Noticias</h3>
                        <h4>Gestión de curriculums versión 1.0.0</h4>
                        <p>Liberada la última versión del gestor de CV de Everis. A partir de ahora será posible filtrar las búsquedas para obtener resultados más precisos basados en las siguientes categorías: </p>
                        <ul>
                            <li>Skill (herramientas o conocimientos de la persona).</li>
                            <li>Empresas (empresas en las que ha trabajado o realizado prácticas).</li>
                            <li>Experiencia (años de antigüedad en el mundo laboral).</li>
                            <li>Idiomas</li>
                        </ul>
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
        </section>
    </div>

    <script type="text/javascript" src="js/jquery.js"></script>
    <script type="text/javascript" src="js/plugins.js"></script>
    <script type="text/javascript" src="js/functions.js"></script>
</body>
</html>
