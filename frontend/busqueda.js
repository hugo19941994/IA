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
        tecnologia: $('#tecnologia'),
        idiomas: $('#idiomas')
    };

    elementos.contenedorOpcional.hide();
    elementos.panelBusquedas.hide();


    /*    elementos.botonBuscar.click(function() {
          cargarCurriculum();
        });


        elementos.botonBuscarOtraVez.click(function() {
          elementos.contenedorOpcional.hide();
          elementos.panelBusquedas.hide();
          elementos.formBusqueda.show();
        });*/

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

        $.ajax({
            type: 'GET',
            url: 'http://51.255.202.84:8080/buscador/all',
            data: {
                nombre: elementosFormulario.nombre.val(),
                dni: elementosFormulario.dni.val(),
                empresa: elementosFormulario.empresa.val(),
                direccion: elementosFormulario.direccion.val(),
                tecnologia: elementosFormulario.tecnologia.val(),
                idiomas: elementosFormulario.idiomas.val(),
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
                        output += '<td><a class="pull-right" style="margin-right: 2%;" href="curriculum.html?id=' + data.searchVector[j].curriculumId + '" class="btn btn-info" role="button">Visualizar</a></td>';
                        output += '<td><a class="pull-right" style="margin-right: 2%;" href="' + data.searchVector[j].downloadCvLink + '" class="btn btn-info" role="button">Descargar</a></td>';
                        output += '<td><a class="pull-right" style="margin-right: 2%;" href="#" class="btn btn-danger" role="button">Borrar</a></td>';
                        output += '</tr>'
                    }

                    output += '</tbody>';

                    elementos.respuestaBusqueda.append(output);
                    elementos.panelBusquedas.show();

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
