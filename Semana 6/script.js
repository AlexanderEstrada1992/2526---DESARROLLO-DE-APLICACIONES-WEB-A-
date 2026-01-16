const formulario = document.getElementById("formulario");
const nombre = document.getElementById("nombre");
const botonEnviar = document.getElementById("enviar");

function validarNombre() {
    const error = nombre.nextElementSibling;

    if (nombre.value.length < 3) {
        nombre.classList.add("invalido");
        nombre.classList.remove("valido");
        error.textContent = "El nombre debe tener al menos 3 caracteres";
        return false;
    } else {
        nombre.classList.add("valido");
        nombre.classList.remove("invalido");
        error.textContent = "";
        return true;
    }
}

nombre.addEventListener("input", validarNombre);

const correo = document.getElementById("correo");

function validarCorreo() {
    const error = correo.nextElementSibling;
    const expresion = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!expresion.test(correo.value)) {
        correo.classList.add("invalido");
        correo.classList.remove("valido");
        error.textContent = "Correo electrónico no válido";
        return false;
    } else {
        correo.classList.add("valido");
        correo.classList.remove("invalido");
        error.textContent = "";
        return true;
    }
}

correo.addEventListener("input", validarCorreo);

const password = document.getElementById("password");

function validarPassword() {
    const error = password.nextElementSibling;
    const expresion = /^(?=.*\d)(?=.*[\W_]).{8,}$/;

    if (!expresion.test(password.value)) {
        password.classList.add("invalido");
        password.classList.remove("valido");
        error.textContent = "Debe tener 8 caracteres, un número y un carácter especial";
        return false;
    } else {
        password.classList.add("valido");
        password.classList.remove("invalido");
        error.textContent = "";
        return true;
    }
}

password.addEventListener("input", validarPassword);

const confirmar = document.getElementById("confirmar");

function validarConfirmacion() {
    const error = confirmar.nextElementSibling;

    if (confirmar.value !== password.value || confirmar.value === "") {
        confirmar.classList.add("invalido");
        confirmar.classList.remove("valido");
        error.textContent = "Las contraseñas no coinciden";
        return false;
    } else {
        confirmar.classList.add("valido");
        confirmar.classList.remove("invalido");
        error.textContent = "";
        return true;
    }
}

confirmar.addEventListener("input", validarConfirmacion);

const edad = document.getElementById("edad");

function validarEdad() {
    const error = edad.nextElementSibling;

    if (edad.value < 18) {
        edad.classList.add("invalido");
        edad.classList.remove("valido");
        error.textContent = "Debe ser mayor o igual a 18 años";
        return false;
    } else {
        edad.classList.add("valido");
        edad.classList.remove("invalido");
        error.textContent = "";
        return true;
    }
}

edad.addEventListener("input", validarEdad);

function validarFormulario() {
    if (
        validarNombre() &&
        validarCorreo() &&
        validarPassword() &&
        validarConfirmacion() &&
        validarEdad()
    ) {
        botonEnviar.disabled = false;
    } else {
        botonEnviar.disabled = true;
    }
}

formulario.addEventListener("input", validarFormulario);

formulario.addEventListener("submit", function (e) {
    e.preventDefault();
    alert("Formulario enviado correctamente");
});
