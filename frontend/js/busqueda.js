$(document).ready(function() {

    var elementos = {
        formBusqueda: $('#formularioBusqueda'),
        contenedorOpcional: $("#contenedorOpcional"),
        panelBusquedas: $('#panelBusquedas'),
        botonBuscar: $('#buscarAhora'),
        botonBuscarOtraVez: $('#volverBuscar'),
        respuestaBusqueda: $('#contenidoBusqueda')
    };

    var elementosFormulario = {
        nombre: $('#nombre'),
        dni: $("#dni"),
        empresa: $('#empresa'),
        direccion: $('#direccion'),
        habilidad: $('#habilidad'),
        tecnologia: $('#tecnologia'),
        idioma: $('#idiomas')
    };

    var listado = {
        nombres: [],
        dni: [],
        empresas: [],
        direcciones: [],
        tecnologias: [],
        habilidades: [],
        idiomas: []
    };

    elementos.contenedorOpcional.hide();
    elementos.panelBusquedas.hide();



    // Añadir nombre
    $(document).on('click', '#addNombre', function() {
        var output = "";
        $('#seccionError').empty();

        if (listado.nombres.length < 5) {
            listado.nombres.push(elementosFormulario.nombre.val());
            $('#nombresConsulta').empty();
            output += "<b style='margin-right: 3%;'>Nombres: </b>"
            for (var nombre in listado.nombres) {
                output += "<button id='removeNombre' class='btn btn-labeled btn-warning' type='button' style='margin-right: 2%;'><span class='btn-label'><i class='icon-remove-sign' style='margin-right: 3%;'></i></span>" + listado.nombres[nombre] + "</button>";
            }
            $('#nombresConsulta').append(output);
        } else {
            output += "<div id='toast-container' class='toast-top-right' aria-live='polite' role='alert'><div class='toast toast-error' style=''><div class='toast-message'> <i id='iconC'class='icon-remove-sign';></i> No se pueden añadir más nombres a la búsqueda.</div></div></div>";
            $('#seccionError').append(output);
        }
    });

    // Borrar nombre
    $(document).on('click', '#removeNombre', function() {
        for (var i = listado.nombres.length - 1; i >= 0; i--) {
            if (listado.nombres[i] === this.innerText) {
                listado.nombres.splice(i, 1);
            }
        }
        if (listado.nombres.length === 0) {
            $('#nombresConsulta').empty();
        }
        this.remove();
    });

    // Añadir DNI
    $(document).on('click', '#addDNI', function() {
        var output = "";
        $('#seccionError').empty();

        if (listado.dni.length < 5) {
            listado.dni.push(elementosFormulario.dni.val());
            $('#dniConsulta').empty();
            output += "<b style='margin-right: 3%;'>DNIs: </b>"
            for (var dni in listado.dni) {
                output += "<button id='removeDNI' class='btn btn-labeled btn-warning' type='button' style='margin-right: 2%;'><span class='btn-label'><i class='icon-remove-sign' style='margin-right: 3%;'></i></span>" + listado.dni[dni] + "</button>";
            }
            $('#dniConsulta').append(output);
        } else {
            output += "<div id='toast-container' class='toast-top-right' aria-live='polite' role='alert'><div class='toast toast-error' style=''><div class='toast-message'> <i id='iconC'class='icon-remove-sign';></i> No se pueden añadir más DNIs a la búsqueda.</div></div></div>";
            $('#seccionError').append(output);
        }
    });

    // Borrar DNI
    $(document).on('click', '#removeDNI', function() {
        for (var i = listado.dni.length - 1; i >= 0; i--) {
            if (listado.dni[i] === this.innerText) {
                listado.dni.splice(i, 1);
            }
        }
        if (listado.dni.length === 0) {
            $('#dniConsulta').empty();
        }
        this.remove();
    });

    // Añadir Empresa
    $(document).on('click', '#addEmpresa', function() {
        var output = "";
        $('#seccionError').empty();

        if (listado.empresas.length < 5) {
            listado.empresas.push(elementosFormulario.empresa.val());
            $('#empresasConsulta').empty();
            output += "<b style='margin-right: 3%;'>Empresas: </b>"
            for (var empresa in listado.empresas) {
                output += "<button id='removeEmpresa' class='btn btn-labeled btn-warning' type='button' style='margin-right: 2%;'><span class='btn-label'><i class='icon-remove-sign' style='margin-right: 3%;'></i></span>" + listado.empresas[empresa] + "</button>";
            }
            $('#empresasConsulta').append(output);
        } else {
            output += "<div id='toast-container' class='toast-top-right' aria-live='polite' role='alert'><div class='toast toast-error' style=''><div class='toast-message'> <i id='iconC'class='icon-remove-sign';></i> No se pueden añadir más empresas a la búsqueda.</div></div></div>";
            $('#seccionError').append(output);
        }
    });

    // Borrar Empresa
    $(document).on('click', '#removeEmpresa', function() {
        for (var i = listado.empresas.length - 1; i >= 0; i--) {
            if (listado.empresas[i] === this.innerText) {
                listado.empresas.splice(i, 1);
            }
        }
        if (listado.empresas.length === 0) {
            $('#empresasConsulta').empty();
        }
        this.remove();
    });

    // Añadir Direcciones
    $(document).on('click', '#addDireccion', function() {
        var output = "";
        $('#seccionError').empty();

        if (listado.direcciones.length < 5) {
            listado.direcciones.push(elementosFormulario.direccion.val());
            $('#direccionesConsulta').empty();
            output += "<b style='margin-right: 3%;'>Direcciones: </b>"
            for (var direccion in listado.direcciones) {
                output += "<button id='removeDireccion' class='btn btn-labeled btn-warning' type='button' style='margin-right: 2%;'><span class='btn-label'><i class='icon-remove-sign' style='margin-right: 3%;'></i></span>" + listado.direcciones[direccion] + "</button>";
            }
            $('#direccionesConsulta').append(output);
        } else {
            output += "<div id='toast-container' class='toast-top-right' aria-live='polite' role='alert'><div class='toast toast-error' style=''><div class='toast-message'> <i id='iconC'class='icon-remove-sign';></i> No se pueden añadir más direcciones a la búsqueda.</div></div></div>";
            $('#seccionError').append(output);
        }
    });

    // Borrar Direcciones
    $(document).on('click', '#removeDireccion', function() {
        for (var i = listado.direcciones.length - 1; i >= 0; i--) {
            if (listado.direcciones[i] === this.innerText) {
                listado.direcciones.splice(i, 1);
            }
        }
        if (listado.direcciones.length === 0) {
            $('#direccionesConsulta').empty();
        }
        this.remove();
    });

    // Añadir habilidades
    $(document).on('click', '#addHabilidad', function() {
        var output = "";
        $('#seccionError').empty();

        if (listado.habilidades.length < 5) {
            listado.habilidades.push(elementosFormulario.habilidad.val());
            $('#habilidadesConsulta').empty();
            output += "<b style='margin-right: 3%;'>Habilidades: </b>"
            for (var habilidad in listado.habilidades) {
                output += "<button id='removeHabilidad' class='btn btn-labeled btn-warning' type='button' style='margin-right: 2%;'><span class='btn-label'><i class='icon-remove-sign' style='margin-right: 3%;'></i></span>" + listado.habilidades[habilidad] + "</button>";
            }
            $('#habilidadesConsulta').append(output);
        } else {
            output += "<div id='toast-container' class='toast-top-right' aria-live='polite' role='alert'><div class='toast toast-error' style=''><div class='toast-message'> <i id='iconC'class='icon-remove-sign';></i> No se pueden añadir más habilidades a la búsqueda.</div></div></div>";
            $('#seccionError').append(output);
        }
    });

    // Borrar habilidades
    $(document).on('click', '#removeHabilidad', function() {
        for (var i = listado.habilidades.length - 1; i >= 0; i--) {
            if (listado.habilidades[i] === this.innerText) {
                listado.habilidades.splice(i, 1);
            }
        }
        if (listado.habilidades.length === 0) {
            $('#habilidadesConsulta').empty();
        }
        this.remove();
    });

    // Añadir tecnologias
    $(document).on('click', '#addTecnologia', function() {
        var output = "";
        $('#seccionError').empty();

        if (listado.tecnologias.length < 5) {
            listado.tecnologias.push(elementosFormulario.tecnologia.val());
            $('#tecnologiasConsulta').empty();
            output += "<b style='margin-right: 3%;'>Tecnologías: </b>"
            for (var tecnologia in listado.tecnologias) {
                output += "<button id='removeTecnologia' class='btn btn-labeled btn-warning' type='button' style='margin-right: 2%;'><span class='btn-label'><i class='icon-remove-sign' style='margin-right: 3%;'></i></span>" + listado.tecnologias[tecnologia] + "</button>";
            }
            $('#tecnologiasConsulta').append(output);
        } else {
            output += "<div id='toast-container' class='toast-top-right' aria-live='polite' role='alert'><div class='toast toast-error' style=''><div class='toast-message'> <i id='iconC'class='icon-remove-sign';></i> No se pueden añadir más tecnologías a la búsqueda.</div></div></div>";
            $('#seccionError').append(output);
        }
    });

    // Borrar tecnologias
    $(document).on('click', '#removeTecnologia', function() {
        for (var i = listado.tecnologias.length - 1; i >= 0; i--) {
            if (listado.tecnologias[i] === this.innerText) {
                listado.tecnologias.splice(i, 1);
            }
        }
        if (listado.tecnologias.length === 0) {
            $('#tecnologiasConsulta').empty();
        }
        this.remove();
    });

    // Añadir idiomas
    $(document).on('click', '#addIdioma', function() {
        var output = "";
        $('#seccionError').empty();

        if (listado.idiomas.length < 5) {
            listado.idiomas.push(elementosFormulario.idioma.val());
            $('#idiomasConsulta').empty();
            output += "<b style='margin-right: 3%;'>Idiomas: </b>"
            for (var idioma in listado.idiomas) {
                output += "<button id='removeIdioma' class='btn btn-labeled btn-warning' type='button' style='margin-right: 2%;'><span class='btn-label'><i class='icon-remove-sign' style='margin-right: 3%;'></i></span>" + listado.idiomas[idioma] + "</button>";
            }
            $('#idiomasConsulta').append(output);
        } else {
            output += "<div id='toast-container' class='toast-top-right' aria-live='polite' role='alert'><div class='toast toast-error' style=''><div class='toast-message'> <i id='iconC'class='icon-remove-sign';></i> No se pueden añadir más idiomas a la búsqueda.</div></div></div>";
            $('#seccionError').append(output);
        }
    });

    // Borrar idiomas
    $(document).on('click', '#removeIdioma', function() {
        for (var i = listado.idiomas.length - 1; i >= 0; i--) {
            if (listado.idiomas[i] === this.innerText) {
                listado.idiomas.splice(i, 1);
            }
        }
        if (listado.idiomas.length === 0) {
            $('#idiomasConsulta').empty();
        }
        this.remove();
    });




    $(document).on('click', '#iconC', function() {
        $('#seccionError').empty();
    });

    $(document).on('click', '#buscarAhora', function() {
        cargarCurriculum();
    });




    $(document).on('click', '#volverBuscar', function() {
        elementos.contenedorOpcional.hide();
        elementos.panelBusquedas.hide();
        elementos.formBusqueda.show();
    });

    function cargarCurriculum() {

        elementos.formBusqueda.hide();
        elementos.contenedorOpcional.show();
        elementos.panelBusquedas.show();

        //Deserializacion de arrays

        var getNombres = "";
        for (var n in listado.nombres) {
            getNombres += listado.nombres[n] + ",";
        }
        getNombres = getNombres.slice(0, -1);

        var getDni = "";
        for (var p in listado.dni) {
            getDni += listado.dni[p] + ",";
        }
        getDni = getDni.slice(0, -1);

        var getEmpresas = "";
        for (var e in listado.empresas) {
            getEmpresas += listado.empresas[e] + ",";
        }
        getEmpresas = getEmpresas.slice(0, -1);

        var getDirecciones = "";
        for (var e in listado.direcciones) {
            getDirecciones += listado.direcciones[e] + ",";
        }
        getDirecciones = getDirecciones.slice(0, -1);

        var getTecnologias = "";
        for (var e in listado.tecnologias) {
            getTecnologias += listado.tecnologias[e] + ",";
        }
        getTecnologias = getTecnologias.slice(0, -1);

        var getHabilidades = "";
        for (var e in listado.habilidades) { //MALLLLL ES HABILIDADES
            getHabilidades += listado.habilidades[e] + ",";
        }
        getHabilidades = getHabilidades.slice(0, -1);

        var getIdiomas = "";
        for (var e in listado.idiomas) { //MALLLLL ES HABILIDADES
            getIdiomas += listado.idiomas[e] + ",";
        }
        getIdiomas = getIdiomas.slice(0, -1);


        $.ajax({
            type: 'GET',
            url: 'http://hugofs.com:8080/buscador/all',
            data: {
                nombre: getNombres,
                dni: getDni,
                empresa: getEmpresas,
                direccion: getDirecciones,
                tecnologia: getTecnologias,
                estudios: getHabilidades,
                idiomas: getIdiomas
            }, //Especifica los datos que se enviarán al servidor
            async: true, //Cuidado con el true! esto es asíncrono puede generar problemas con otros fragmentos de código. Hace que el código se ejecute de manera concurrente
            beforeSend: function(xhr) {
                if (xhr && xhr.overrideMimeType) {
                    xhr.overrideMimeType('application/json;charset=utf-8');
                }
            },
            dataType: 'json',
            success: function(data, status) {

                //Do stuff with the JSON data
                if (status == "success") {
                    var output = '';
                    elementos.respuestaBusqueda.empty();
                    output += '<table class="table"><thead><tr><td><strong>ID del Curriculum</strong></thead><tbody>';

                    for (var j = 0; j < data.searchVector.length; j++) {

                        output += '<tr>'
                        output += '<td>' + data.searchVector[j].curriculumId + '</td>';
                        // Disabled "visualizar" as the route wasn't working
                        //output += '<td><a class="pull-right" style="margin-right: 2%;" href="curriculum.html?id=' + data.searchVector[j].curriculumId + '" class="btn btn-info" role="button">Visualizar</a></td>';
                        output += '<td><a class="pull-right" style="margin-right: 2%;" href="' + data.searchVector[j].downloadCvLink + '" class="btn btn-info" role="button">Descargar</a></td>';
                        output += '<td><a class="pull-right" style="margin-right: 2%;" href="#" class="btn btn-danger" role="button">Score: ' + data.searchVector[j].curriculumScore * 100 + '</a></td>';
                        output += '</tr>'
                    }

                    output += '</tbody>';

                    elementos.respuestaBusqueda.append(output);
                    elementos.panelBusquedas.show();

                    $.ajax({
                        type: "POST",
                        url: 'gestionUsuarios.php',
                        data: {
                            function: 'true',
                        },
                        success: function(data) {
                        }
                    });

                } else {
                    output += "Error en la conexión con el servidor de búsquedas. Intentalo de nuevo mas tarde.";
                    elementos.respuestaBusqueda.append(output);
                    elementos.panelBusquedas.show();
                }
            },
            error: function(status) {
                var output = "<ul>";
                output += '<div class="alert alert-danger">';
                output += '<i class="icon-remove-sign"></i><strong>Ha habido al intentar conectar con el servidor de datos. Error: ' + status;
                output += '</div>';
                output += "</ul>";
                elementos.respuestaBusqueda.append(output);
                elementos.panelBusquedas.show();
            }

        });

    }

});
