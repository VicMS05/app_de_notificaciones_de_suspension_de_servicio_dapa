function enviarFormularioCliente() {
    var datitos = { // Creo un objeto con los datos del formulario (JSON)
        idcliente: document.getElementById("numContrato").value, // document.getElementById("idcliente") es un objeto de tipo input
        nombrecliente: document.getElementById("nombre").value.toUpperCase(), // document.getElementById("nombre") es un objeto de tipo input
        appatcliente: document.getElementById("apellidoP").value.toUpperCase(), // document.getElementById("apellidoP") es un objeto de tipo input
        apmatcliente: document.getElementById("apellidoM").value.toUpperCase(), // document.getElementById("apellidoM") es un objeto de tipo input
        contracliente: document.getElementById("password-input").value, // document.getElementById("password-input") es un objeto de tipo input
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
            console.log(data); // Imprimir en consola
            alert("Se ha registrado correctamente");
        })
        .catch(error => { // Devuelve otra promesa
            console.error('Error al enviar los datos:', error); // Imprimir en consola
        });
}