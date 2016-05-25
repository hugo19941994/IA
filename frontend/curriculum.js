var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};

$(document).ready(function() {

  var id_cv = getUrlParameter('id');
  var contenedor = $('#contenedorInfo');
  console.log(id_cv);

  $.ajax({
      type: 'GET',
      url: 'http://51.255.202.84:8080/curriculums/' + id_cv,
      data: {
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
              contenedor.empty();
              console.log(data);
              output += '<h2>' + data._source["Chunker - Datos Personales"].S.Personas[0] + '</h2><br>';

              output += '<h2>Datos personales</h2><br>';
              output += '<h3>Lugares</h3><br>';

              for (var i = 0; i < data._source["Chunker - Datos Personales"].S.Lugares.length; i++) {
                  output += data._source["Chunker - Datos Personales"].S.Lugares[i] + '<br>';
              }
              output += '<h3>Organizaciones</h3><br>';
              for (var p = 0; i < data._source["Chunker - Datos Personales"].S.Organizaciones.length; p++) {
                  output += data._source["Chunker - Datos Personales"].S.Organizaciones[i] + '<br>';
              }
              output += '<h3>Personas</h3><br>';
              for (var p = 0; i < data._source["Chunker - Datos Personales"].S.Personas.length; p++) {
                  output += data._source["Chunker - Datos Personales"].S.Personas[i] + '<br>';
              }

              output += '<h2>Emails</h2><br>';
              for (var i = 0; i < data._source["Chunker - Experiencia Laboral"].S.Lugares.length; i++) {
                  output += data._source["Chunker - Experiencia Laboral"].S.Lugares[i] + '<br>';
              }

              output += '<h2>Experiencia laboral</h2><br>';
              for (var i = 0; i < data._source["Chunker - Experiencia Laboral"].S.Organizaciones.length; i++) {
                  output += data._source["Chunker - Experiencia Laboral"].S.Organizaciones[i] + '<br>';
              }


              contenedor.append(output);

          } else {
              output += "Error en la conexión con el servidor de búsquedas. Intentalo de nuevo mas tarde.";
              contenedor.append(output);

          }
      },
      error: function(status) {
          var output = "<ul>";
          output += '<div class="alert alert-danger">';
          output += '<i class="icon-remove-sign"></i><strong>Ha habido al intentar conectar con el servidor de datos. Error: ' + status;
          output += '</div>';
          output += "</ul>";
/*          elementos.respuestaBusqueda.append(output);
          elementos.panelBusquedas.show();*/
      }

  });

});
