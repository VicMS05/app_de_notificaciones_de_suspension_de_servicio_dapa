async function hashearContraseña(contraseña) { // Función para encriptar la contraseña
    const encoder = new TextEncoder(); // Creo un objeto de tipo TextEncoder
    const data = encoder.encode(contraseña); // Codifico la contraseña
    const hashBuffer = await crypto.subtle.digest('SHA-256', data); // Creo un objeto de tipo SHA-256
    const hashArray = Array.from(new Uint8Array(hashBuffer)); // Creo un objeto de tipo Uint8Array
    const hashHex = hashArray.map(byte => byte.toString(16).padStart(2, '0')).join(''); // Creo un objeto de tipo Uint8Array
    return hashHex; // Devuelvo el hash de la contraseña
}

async function validarInicioSesionCliente() { // Función para validar el inicio de sesión del cliente, es async porque se usa la función hashearContraseña y esta es async

    var usuario = document.getElementById("usuario").value; // Se obtiene el valor del usuario
    var contraseña = await hashearContraseña(document.getElementById("password-input1").value); // Se obtiene el valor de la contraseña y se encripta con la funcion hashearContraseña
    var url; // Variable para almacenar la url de la API

    if (isNaN(usuario)) { // Si el usuario no es un número
        url = 'http://localhost:8000/api/cliente_correo/' + usuario; // Se establece la url de la API para que ingrese con el correo
    } else {
        url = 'http://localhost:8000/api/cliente_id/' + usuario; // Se establece la url de la API para que ingrese con el numero de contrato
    }

    console.log(url + " | " + usuario)

    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.cliente && data.cliente.nombrecliente != null && data.cliente.contracliente == contraseña) {
                alert("Bienvenido " + data.cliente.nombrecliente + " " + data.cliente.appatcliente + " " + data.cliente.apmatcliente);
                window.open('http://localhost:5500/src/panel_cliente.html', "_self")
            } else {
                alert("Usuario o contraseña incorrectos");
            }
        })
        .catch(error => console.error('Error al obtener datos de la API:', error)); // Imprimir en consola

}