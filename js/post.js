async function post(entidad) { // Función para enviar los datos del formulario al servidor
    var datitos, url, cp; // Variables para almacenar los datos del formulario y la url de la API

    switch (entidad) {
        case 'administrador':
            datitos = { // Creo un objeto con los datos del formulario (JSON)
                nombreadmin: document.getElementById("nombre").value.toUpperCase(), // document.getElementById("nombre") es un objeto de tipo input
                appatadmin: document.getElementById("apellidoP").value.toUpperCase(), // document.getElementById("apellidoP") es un objeto de tipo input
                apmatadmin: document.getElementById("apellidoM").value.toUpperCase(), // document.getElementById("apellidoM") es un objeto de tipo input
                contraadmin: document.getElementById("password-input").value, // document.getElementById("password-input") es un objeto de tipo input donde se usa la función para encriptar la contraseña
                correoadmin: document.getElementById("email").value, // document.getElementById("email") es un objeto de tipo input
            }
            break;
        case 'zona':
            datitos = { // Creo un objeto con los datos del formulario (JSON)
                colonia: document.getElementById("sector").value.toUpperCase(), // document.getElementById("colonia") es un objeto de tipo input
                codigopostal: document.getElementById("cp").value, // document.getElementById("codigopostal") es un objeto de tipo input
            }
            url = '../../php/post_zona.php'; // Asigno la url de la API
            break;
        case 'cliente':
            contra1 = document.getElementById("password-input").value;
            contra2 = document.getElementById("password-input2").value;
            if (contra1 == contra2) {
                datitos = { // Creo un objeto con los datos del formulario (JSON)
                    idcliente: document.getElementById("numContrato").value, // document.getElementById("idcliente") es un objeto de tipo input
                    nombrecliente: document.getElementById("nombre").value.toUpperCase(), // document.getElementById("nombre") es un objeto de tipo input
                    appatcliente: document.getElementById("apellidoP").value.toUpperCase(), // document.getElementById("apellidoP") es un objeto de tipo input
                    apmatcliente: document.getElementById("apellidoM").value.toUpperCase(), // document.getElementById("apellidoM") es un objeto de tipo input
                    contracliente: contra1,
                    correocliente: document.getElementById("email").value, // document.getElementById("email") es un objeto de tipo input
                    callecliente: document.getElementById("calle").value.toUpperCase(), // document.getElementById("calle") es un objeto de tipo input
                    colcliente: document.getElementById("listadesplegable").value.toUpperCase(), // document.getElementById("colonia") es un objeto de tipo input
                    numextcliente: document.getElementById("numext").value, // document.getElementById("numext") es un objeto de tipo input
                    cpcliente: document.getElementById("cp").value, // document.getElementById("cp") es un objeto de tipo input
                }
                url = 'php/post_cliente.php'; // Asigno la url de la API
            } else {
                alert("Las contraseñas no coinciden");
                return;
            }
            break;
        case 'reporte':
            datitos = { // Creo un objeto con los datos del formulario (JSON)
                motivorep: document.getElementById("motivo").value.toUpperCase(), // document.getElementById("motivorep") es un objeto de tipo input
                fecharep: document.getElementById("fecha").value, // document.getElementById("fechareporte") es un objeto de tipo input
                estatusrep: "Enviado", // document.getElementById("estatusrep") es un objeto de tipo input
                clavecliente: document.getElementById("numContrato").value, // document.getElementById("clavecliente") es un objeto de tipo input
            }
            break;
    }

    console.log(JSON.stringify(datitos));

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(datitos)
    }) // Hago una petición POST al servidor
    .then(response => response.text()) // Devuelve otra promesa
    alert("Se ha registrado correctamente")
        .then(data => { // Devuelve otra promesa
            // Manejar la respuesta de la API
            console.log(data);
        })
        .catch(error => { // Devuelve otra promesa
            console.error('Error al enviar los datos:', error); // Imprimir en consola
        });
}

// function get_cp_zona(zona) {
//     return fetch('php/get_zonas.php') // Devuelve una promesa
//         .then(response => response.text()) // Devuelve otra promesa
//         .then(data => {
//             data.forEach(item => {
//                 if(item.colonia == zona)
//                     return item.codigoPostal;
//             });
//         })
//         .catch(error => { // Devuelve otra promesa
//             // Capturar y manejar errores
//             console.error('Error en la solicitud:', error); // Imprimir en consola
//             throw error; // Lanzar excepción
//         });
// }