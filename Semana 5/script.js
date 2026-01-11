// Referencias a elementos del DOM
const imageUrlInput = document.getElementById("imageUrl");
const addImageBtn = document.getElementById("addImageBtn");
const deleteImageBtn = document.getElementById("deleteImageBtn");
const gallery = document.getElementById("gallery");

let selectedImage = null;

// Evento para agregar imagen
addImageBtn.addEventListener("click", () => {
    const imageUrl = imageUrlInput.value;

    if (imageUrl === "") {
        alert("Por favor ingresa una URL de imagen");
        return;
    }

    // Crear elemento img
    const img = document.createElement("img");
    img.src = imageUrl;

    // Evento click para seleccionar imagen
    img.addEventListener("click", () => {
        // Quitar selección anterior
        if (selectedImage) {
            selectedImage.classList.remove("selected");
        }

        // Seleccionar nueva imagen
        img.classList.add("selected");
        selectedImage = img;
    });

    // Agregar imagen a la galería
    gallery.appendChild(img);

    // Limpiar input
    imageUrlInput.value = "";
});
// Evento para eliminar imagen seleccionada
deleteImageBtn.addEventListener("click", () => {
    if (!selectedImage) {
        alert("No hay ninguna imagen seleccionada");
        return;
    }

    gallery.removeChild(selectedImage);
    selectedImage = null;
});
// Evento input (detecta escritura en el campo URL)
imageUrlInput.addEventListener("input", () => {
    imageUrlInput.style.borderColor = imageUrlInput.value ? "#28a745" : "#ccc";
});

// Atajos de teclado
document.addEventListener("keydown", (event) => {
    // Enter agrega imagen
    if (event.key === "Enter") {
        addImageBtn.click();
    }

    // Delete elimina imagen seleccionada
    if (event.key === "Delete") {
        deleteImageBtn.click();
    }
});
