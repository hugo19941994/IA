$(document).ready(function() {

    $("#bajaUsuario").click(function() {
        var del_id = $('#borrarUsuarioId').val();

        var output = "";
        $('#seccionError').empty();
        $.ajax({
            type: 'POST',
            url: 'gestionUsuarios.php',
            data: {
                delete_id: del_id,
            },
            async: true,
            success: function(data) {
                if (data) { // DO SOMETHING
                    output += "<div id='toast-container' class='toast-top-right' aria-live='polite' role='alert'><div class='toast toast-success' style=''><div class='toast-message'> <i id='iconC'class='icon-remove-sign';></i> Usuario eliminado con exito.</div></div></div>";
                    $('#seccionError').append(output);
                } else { // DO SOMETHING }
                    output += "<div id='toast-container' class='toast-top-right' aria-live='polite' role='alert'><div class='toast toast-error' style=''><div class='toast-message'> <i id='iconC'class='icon-remove-sign';></i> No se ha podido eliminar el usuario, compruebe que existe.</div></div></div>";
                    $('#seccionError').append(output);
                }
            }
        });
    });

    $("#altaUsuario").click(function() {
        var nuevoUsuario = $('#nuevoUsuarioNombre').val();
        var nuevaPassword = $('#nuevoUsuarioPassword').val();
        var nuevoPermiso = $('#nuevoUsuarioPermisos').val();

        var output = "";
        $('#seccionError').empty();

        $.ajax({
            type: 'POST',
            url: 'gestionUsuarios.php',
            data: {
                nuevoUsuario: nuevoUsuario,
                nuevaPassword: nuevaPassword,
                nuevoPermiso: nuevoPermiso,
            },
            async: true,
            success: function(data) {
                if (data) { // DO SOMETHING
                    output += "<div id='toast-container' class='toast-top-right' aria-live='polite' role='alert'><div class='toast toast-success' style=''><div class='toast-message'> <i id='iconC'class='icon-remove-sign';></i> Usuario registrado con exito.</div></div></div>";
                    $('#seccionError').append(output);
                } else { // DO SOMETHING }
                    output += "<div id='toast-container' class='toast-top-right' aria-live='polite' role='alert'><div class='toast toast-error' style=''><div class='toast-message'> <i id='iconC'class='icon-remove-sign';></i> No se ha podido registrar el usuario. Intentelo de nuevo.</div></div></div>";
                    $('#seccionError').append(output);
                }
            }
        });
    });

    $(document).on('click', '#iconC', function() {
        $('#seccionError').empty();
    });

});
