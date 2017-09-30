<?php session_start(); ?>
<!DOCTYPE html>
<html dir="ltr" lang="en-US">
<head>

	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<meta name="author" content="jdecastroc" />

	<!-- Stylesheets
	============================================= -->
	<link href="https://fonts.googleapis.com/css?family=Lato:300,400,400italic,600,700|Raleway:300,400,500,600,700|Crete+Round:400italic" rel="stylesheet" type="text/css">
	<link rel="stylesheet" href="css/bootstrap.min.css" type="text/css">
	<link rel="stylesheet" href="style.min.css" type="text/css">
	<link rel="stylesheet" href="css/swiper.css" type="text/css">
	<link rel="stylesheet" href="css/dark.min.css" type="text/css">
	<link rel="stylesheet" href="css/font-icons.css" type="text/css">
	<link rel="stylesheet" href="css/animate.min.css" type="text/css">
	<link rel="stylesheet" href="css/magnific-popup.css" type="text/css">

	<link rel="icon" href="favicon.ico">

	<link rel="stylesheet" href="css/responsive.css" type="text/css">
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<!--[if lt IE 9]>
		<script src="http://css3-mediaqueries-js.googlecode.com/svn/trunk/css3-mediaqueries.js"></script>
	<![endif]-->

	<!-- Document Title
	============================================= -->
	<title>Everis - Gestor de curriculums</title>

</head>

<?php
  require 'functions.php';
  $lang = "es";
	$allowed = false;
  if(isset($_SESSION["usuario"]) && isset($_SESSION["password"]))
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
  }
?>

<body class="stretched side-header">

	<!-- Document Wrapper
	============================================= -->
	<div id="wrapper" class="clearfix">

		<!-- Header
		============================================= -->
		<header id="header" class="no-sticky">
			<div id="header-wrap">

				<div class="container clearfix">

					<div id="primary-menu-trigger"><i class="icon-reorder"></i></div>

					<!-- Logo
					============================================= -->
					<div id="logo" class="nobottomborder">
						<a href="index.php" class="standard-logo" data-dark-logo="img/logo-everis.png"><img src="img/logo-everis.png" alt="Everis logo"></a>
					</div><!-- #logo end -->

					<!-- Primary Navigation
					============================================= -->
					<nav id="primary-menu">
						<ul>
							<li><a href="index.php"><div>Índice</div></a></li>
							<li><a href="gestor.php"><div>Gestión de repositorio</div></a></li>
							<li><a href="buscador.php"><div>Búsqueda de CV</div></a></li>
              <?php
                if ($allowed && $permisos_db == "administrador") {
              ?>
              <li><a href="usuarios.php"><div>Gestión de usuarios</div></a> <!-- Solo para administradores-->
              </li>
              <br><br>
              <?php } ?>
							<li class="current"><a href="ayuda.php"><div>Ayuda</div></a></li>
							<li><a href="contacto.php"><div>Contacto</div></a></li>
						</ul>

					</nav><!-- #primary-menu end -->

					<div class="clearfix visible-md visible-lg">
						<a href="https://github.com/hugo19941994/CV-Parser" class="social-icon si-small si-borderless si-github">
							<i class="icon-github"></i>
							<i class="icon-github"></i>
						</a>
					</div>

				</div>

			</div>

		</header>
			<!-- #header end -->


		<!-- Content
		============================================= -->

		<section id="content">

			<div class="content-wrap">

				<div class="promo promo-full promo-border header-stick bottommargin-lg">
					<div class="container clearfix">
						<h3>Ayuda - gestor de curriculums de Everis</h3>
					</div>
				</div>
				<div class="container clearfix">
					<div class="col_full">
						<div>
							<h3>Documentación y Ayuda</h3>
                            <ul>
                            <li><a href="<?php $_ENV["URL"] ?>/swagger-ui.html">Swagger</a></li>
                                <li><a href="https://github.com/hugo19941994/CV-Parser/raw/master/docs/Documentacion%20Proyecto%20Integrador.pdf">Documentacion del proyecto</a></li>
                                <li><a href="https://github.com/hugo19941994/CV-Parser/raw/master/docs/Manual%20de%20usuario%20PBS.pdf">Manual de Usuario</a></li>
                            </ul>
						</div>
					</div>
				</div>
			</div>

		</section><!-- #content end -->


	</div><!-- #wrapper end -->

	<!-- JavaScripts externos
	============================================= -->
	<script type="text/javascript" src="js/jquery.js"></script>
	<script type="text/javascript" src="js/plugins.js"></script>

	<!-- Footer Scripts
	============================================= -->
	<script type="text/javascript" src="js/functions.js"></script>

</body>
</html>
