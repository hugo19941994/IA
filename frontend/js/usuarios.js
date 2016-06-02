$(document).ready(function(){
 $("#bajaUsuario").click(function(){
   var del_id = $('#borrarUsuarioId').val();
   $.ajax({
      type:'POST',
      url:'borrar_usuario.php',
      data:'delete_id=' + del_id,
      success:function(data) {
        if(data) {   // DO SOMETHING
        } else { // DO SOMETHING }
      }
   });
 });
});
