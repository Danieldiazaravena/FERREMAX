document.getElementById("Form_contacto").addEventListener("submit", function(event){
    var Nombre = document.getElementById("name");
    var Correo = document.getElementById("email");
    var Telefono = document.getElementById("phone");
    var Mensaje = document.getElementById("message");

    if(Nombre.value == "" || Correo.value == "" || Telefono.value == "" || Mensaje.value == ""){
        alert("Todos los campos son obligatorios.");
        event.preventDefault();

      }else{}
        
    });
