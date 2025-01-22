const now = new Date();
const formattedDateTime = now.toISOString().slice(0, 16); // Formato para datetime-local
document.querySelector('input[type="datetime-local"]').value = formattedDateTime;

// Seleccionar todos los activadores de acordeón
document.querySelectorAll('.activar-arcodion').forEach(function(trigger) {
    trigger.addEventListener('click', function(event) {
        event.preventDefault(); // Prevenir la acción por defecto del enlace

        // Buscar el contenedor del acordeón relacionado
        const acordeon = this.closest('.acordeon-item').querySelector('.arcodion');

        // Alternar visibilidad del acordeón
        if (acordeon.style.display === 'none' || acordeon.style.display === '') {
            acordeon.style.display = 'block'; // Mostrar acordeón
        } else {
            acordeon.style.display = 'none'; // Ocultar acordeón
        }

        // Alternar la clase "activo" en el activador
        this.classList.toggle('activo');
    });
});


$(document).ready(function(){
    $("#Btn-coord").click(function(){
      $("#dynamicCooordinarModal").modal();
    });
  });


  