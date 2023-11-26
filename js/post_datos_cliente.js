async function hashearContraseña(contraseña) { // Función para encriptar la contraseña
    const encoder = new TextEncoder(); // Creo un objeto de tipo TextEncoder
    const data = encoder.encode(contraseña); // Codifico la contraseña
    const hashBuffer = await crypto.subtle.digest('SHA-256', data); // Creo un objeto de tipo SHA-256
    const hashArray = Array.from(new Uint8Array(hashBuffer)); // Creo un objeto de tipo Uint8Array
    const hashHex = hashArray.map(byte => byte.toString(16).padStart(2, '0')).join(''); // Creo un objeto de tipo Uint8Array
    return hashHex; // Devuelvo el hash de la contraseña
}

async function enviarFormularioCliente() { // Función para enviar los datos del formulario al servidor
    var datitos = { // Creo un objeto con los datos del formulario (JSON)
        idcliente: document.getElementById("numContrato").value, // document.getElementById("idcliente") es un objeto de tipo input
        nombrecliente: document.getElementById("nombre").value.toUpperCase(), // document.getElementById("nombre") es un objeto de tipo input
        appatcliente: document.getElementById("apellidoP").value.toUpperCase(), // document.getElementById("apellidoP") es un objeto de tipo input
        apmatcliente: document.getElementById("apellidoM").value.toUpperCase(), // document.getElementById("apellidoM") es un objeto de tipo input
        contracliente: await hashearContraseña(document.getElementById("password-input").value), // document.getElementById("password-input") es un objeto de tipo input donde se usa la función para encriptar la contraseña
        correocliente: document.getElementById("email").value, // document.getElementById("email") es un objeto de tipo input
        callecliente: document.getElementById("calle").value.toUpperCase(), // document.getElementById("calle") es un objeto de tipo input
        colcliente: document.getElementById("listadesplegable").value.toUpperCase(), // document.getElementById("colonia") es un objeto de tipo input
        numextcliente: document.getElementById("numext").value, // document.getElementById("numext") es un objeto de tipo input
        cpcliente: document.getElementById("cp").value, // document.getElementById("cp") es un objeto de tipo input
    }

    fetch('http://localhost:8000/api/clientes/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(datitos)
    }) // Hago una petición POST al servidor
        .then(response => response.json()) // Devuelve otra promesa
        .then(data => { // Devuelve otra promesa
            // Manejar la respuesta de la API
            alert("Se ha registrado correctamente");
        })
        .catch(error => { // Devuelve otra promesa
            console.error('Error al enviar los datos:', error); // Imprimir en consola
        });
}