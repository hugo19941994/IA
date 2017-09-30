<?php session_start(); ?>
<!DOCTYPE html>
<html dir="ltr" lang="es">

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

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" type="text/css" />
    <link rel="icon" href="favicon.ico">

    <link rel="stylesheet" href="css/responsive.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <!--[if lt IE 9]>
		<script src="http://css3-mediaqueries-js.googlecode.com/svn/trunk/css3-mediaqueries.js"></script>
	<![endif]-->

    <title>Everis - Gestión de repositorio</title>

</head>

<?php
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
    <div id="wrapper" class="clearfix">
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
  							<li class="current"><a href="gestor.php"><div>Gestión de repositorio</div></a></li>
  							<li><a href="buscador.php"><div>Búsqueda de CV</div></a></li>

  							<?php
  								if ($allowed && $permisos_db == "administrador") {
  							?>
  							<li><a href="usuarios.php"><div>Gestión de usuarios</div></a> <!-- Solo para administradores-->
  							</li>
  							<br><br>
  							<?php } ?>
  							<li><a href="ayuda.php"><div>Ayuda</div></a></li>
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
                        <h3>Gestor del repositorio de curriculums</h3>
                        <span>Añada nuevos curriculums al repositorio para realizar búsquedas sobre ellos o elimine los que se hayan descartado.</span>
                    </div>
                </div>

                <div class="container clearfix">

                  <?php
                    if ($allowed) {
                  ?>
                    <div class="col_half">
                        <div class="panel panel-default">
                            <div class="panel-heading">
                                <div class="panel-title text-center">Subir Curriculums</div>
                            </div>

                            <div class="panel-body">

                                <p>Seleccione los curriculums que desea añadir a la plataforma</p>

                                <form class="form-horizontal">
                                    <fieldset>
                                        <div class="input-group image-preview">
                                            <label class="btn btn-default btn-file">
                                                Elegir Archivo
                                                <input type="file" id="file" name="document" class="findDocumentOnboarding" style="display:none;"multiple/>
                                            </label>
                                            <label class="btn btn-default">
                                                Subir
                                                <input type="button" id="upload-button" class="uploadDocumentOnboarding" value="Subir" style="display:none"/>
                                            </label>
<i id="uploadIndicator" class="fa fa-2x fa-spin fa-spinner" aria-hidden="true" style="visibility:hidden;"></i>

                                            <!-- don't give a name === doesn't send on POST/GET -->
                                            <!--<span class="input-group-btn">-->
                              <button type="button" class="btn btn-default image-preview-clear" style="display:none;">
                                  <span class="glyphicon glyphicon-remove"></span> Borrar
                                            </button>
                                            <!--<div class="btn btn-default image-preview-input">
                                                <span class="image-preview-input-title">Buscar</span>
                                                <input type="file" accept="image/png, image/jpeg, image/gif" name="input-file-preview" />
                                            </div>-->
                                            </span>
                                        </div>
                                    </fieldset>
                                </form>

                                <br>
                            </div>
                        </div>
                    </div>

                    <div class="col_half col_last">
                        <div class="panel panel-default">
                            <div class="panel-heading">
                                <div class="panel-title text-center">Borrar Curriculums</div>
                            </div>

                            <div class="panel-body">

                                <p>Introduzca el ID del Curriculum que desea eliminar del repositorio</p>
                                <fieldset>
                                    <div class="input-group image-preview">
                                        <input id="idCvBorrar"type="text" class="form-control image-preview-filename">
                                        <span class="input-group-btn">
                              <button id="borrarCv" class="btn btn-default image-preview-input" type="button" data-toggle="modal" data-target="#myModal">Borrar</button>

                              <div id="myModal" class="modal fade in">
                                  <div class="modal-dialog">
                                      <div class="modal-content">

                                          <div class="modal-header">
                                              <a class="btn btn-default" data-dismiss="modal"><span class="glyphicon glyphicon-remove"></span></a>

                                    </div>
                                    <div class="modal-body">
                                        <h4>¿Estas seguro que deseas borrar el Curriculum ?</h4>
                                    </div>
                                    <div class="modal-footer">
                                        <div class="btn-group">
                                            <button class="btn btn-danger" data-dismiss="modal"><span class="glyphicon glyphicon-remove"></span> Cancelar</button>
                                            <button class="btn btn-primary"><span class="glyphicon glyphicon-check"></span> Borrar</button>
                                        </div>
                                    </div>

                            </div>
                            <!-- /.modal-content -->
                        </div>
                        <!-- /.modal-dalog -->
                    </div>
                    <!-- /.modal -->

                    </span>
                </div>
                </fieldset>



            </div>
    </div>
    </div>
    <?php
  } else {
    ?>
    <div class="col_full">
      <div>
        <h3>Usuario incorrecto</h3>
        <p>Usted no tiene acceso para ver esta página. Vuelva a la pantalla de acceso para entrar con el usuario proporcionado por el administrador del sistema.</p>
      </div>
    </div>
    <?php
    }
    ?>
    </div>
    </div>


    </div>

    </div>

    </section>
    <!-- #content end -->

    </div>
    <!-- #wrapper end -->
    <div id="seccionExito"></div>
    <div class="modal-body" id="cargando" style="background:url(/img/loading.gif) no-repeat center center;width:32px;height:32px;"></div>

    <!-- JavaScripts externos
	============================================= -->
    <script type="text/javascript" src="js/jquery.js"></script>
    <script type="text/javascript" src="js/plugins.js"></script>
    <script type="text/javascript" src="js/gestor.js"></script>


    <!-- Footer Scripts
	============================================= -->
    <script type="text/javascript" src="js/functions.js"></script>
    <script type="text/javascript" src="js/upload.js"></script>

</body>

</html>
