// Arreglo inicial de productos con nombres y descripciones reales
const products = [
    { nombre: "Laptop HP Pavilion", precio: 750.00, descripcion: "Laptop HP con procesador Intel i5, 8GB RAM y 512GB SSD." },
    { nombre: "Auriculares Sony WH-1000XM4", precio: 299.99, descripcion: "Auriculares inalámbricos con cancelación de ruido y batería de larga duración." },
    { nombre: "Smartphone Samsung Galaxy S23", precio: 999.99, descripcion: "Teléfono inteligente con cámara de 200MP, 12GB RAM y 256GB de almacenamiento." },
    { nombre: "Mochila SwissGear", precio: 89.50, descripcion: "Mochila resistente con compartimentos para laptop y accesorios." },
    { nombre: "Teclado Mecánico Logitech", precio: 129.99, descripcion: "Teclado mecánico retroiluminado con switches táctiles y duraderos." }
];

// Seleccionamos el elemento UL donde se mostrarán los productos
const productList = document.getElementById("product-list");

// Función para renderizar la lista de productos
function renderProducts() {
    // Limpiar lista antes de renderizar (evita duplicados)
    productList.innerHTML = "";

    // Recorrer cada producto y crear un elemento li
    products.forEach((producto) => {
        const li = document.createElement("li");
        li.textContent = `${producto.nombre} - $${producto.precio.toFixed(2)}: ${producto.descripcion}`;
        productList.appendChild(li);
    });
}

// Llamamos a la función para mostrar los productos al cargar la página
renderProducts();

// Funcionalidad para agregar un nuevo producto desde el formulario
const addButton = document.getElementById("add-product");

addButton.addEventListener("click", () => {
    // Obtener valores de los inputs
    const nameInput = document.getElementById("product-name").value.trim();
    const priceInput = parseFloat(document.getElementById("product-price").value);
    const descInput = document.getElementById("product-description").value.trim();

    // Validar que los campos no estén vacíos
    if (nameInput === "" || isNaN(priceInput) || descInput === "") {
        alert("Por favor completa todos los campos correctamente.");
        return;
    }

    // Crear nuevo producto y agregarlo al arreglo
    const newProduct = {
        nombre: nameInput,
        precio: priceInput,
        descripcion: descInput
    };

    products.push(newProduct);

    // Renderizar de nuevo la lista
    renderProducts();

    // Limpiar campos del formulario
    document.getElementById("product-name").value = "";
    document.getElementById("product-price").value = "";
    document.getElementById("product-description").value = "";
});