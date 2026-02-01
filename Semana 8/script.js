// Botón de alerta
function mostrarAlerta() {
    alert("¡Gracias por visitar nuestra página web interactiva!");
}

// Validación del formulario
document.getElementById("formularioContacto").addEventListener("submit", function (event) {
    event.preventDefault();

    let nombre = document.getElementById("nombre").value.trim();
    let correo = document.getElementById("correo").value.trim();
    let mensaje = document.getElementById("mensaje").value.trim();

    let valido = true;

    // Limpiar errores
    document.getElementById("errorNombre").textContent = "";
    document.getElementById("errorCorreo").textContent = "";
    document.getElementById("errorMensaje").textContent = "";

    if (nombre === "") {
        document.getElementById("errorNombre").textContent = "El nombre es obligatorio";
        valido = false;
    }

    if (correo === "") {
        document.getElementById("errorCorreo").textContent = "El correo es obligatorio";
        valido = false;
    }

    if (mensaje === "") {
        document.getElementById("errorMensaje").textContent = "El mensaje es obligatorio";
        valido = false;
    }

    if (valido) {
        alert("Formulario enviado correctamente");
        document.getElementById("formularioContacto").reset();
    }
});
