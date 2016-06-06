$(document).ready(function() {

  $(document).on('click', '#borrarCv', function() {
    idCvBorrar = $('#idCvBorrar').val()
    $.ajax({
        type: 'POST',
        url: 'http://hugofs.com:8080/borrar/' + idCvBorrar,
        //data: {}, //Especifica los datos que se enviarán al servidor
        async: true, //Cuidado con el true! esto es asíncrono puede generar problemas con otros fragmentos de código. Hace que el código se ejecute de manera concurrente
        beforeSend: function(xhr) {
            if (xhr && xhr.overrideMimeType) {
                xhr.overrideMimeType('application/json;charset=utf-8');
            }
        },
        dataType: 'text',
    	contentType: "text/plain; charset=utf-8",
        success: function(data, status) {

            //Do stuff with the JSON data
            if (status == "success") {
                var output = '';
                output += "<div id='toast-container' class='toast-top-right' aria-live='polite' role='alert'><div class='toast toast-success' style=''><div class='toast-message'> <i id='iconC'class='icon-remove-sign';></i> Se ha eliminado el curriculum especificado correctamente.</div></div></div>";
                $('#seccionExito').append(output);

            }
        },
        error: function(status) {
            var output = "<ul>";
            output += '<div class="alert alert-danger">';
            output += '<i class="icon-remove-sign"></i><strong>Ha habido al intentar conectar con el servidor de datos. Error: ' + status;
            output += '</div>';
            output += "</ul>";
        }

    });
  });

});
