function validarInicioSesion(entidad) { // Función para validar el inicio de sesión del cliente, es async porque se usa la función hashearContraseña y esta es async
    var url; // Variable para almacenar la url de la API

    datitos = { // Creo un objeto con los datos del formulario (JSON)
        usuario: document.getElementById("usuario").value, // Se obtiene el valor del usuario
        contraseña: document.getElementById("contraseña").value // Se obtiene el valor de la contraseña y se encripta con la funcion hashearContraseña
    }

    switch (entidad) { // Seleccionar la entidad a la que se va a acceder
        case 'administrador':
            url = '../../php/post_validar_login_administrador.php'; // Se establece la url de la API para que ingrese con el correo
            break;
        case 'cliente':
            url = 'php/post_validar_login_cliente.php'; // Se establece la url de la API para que ingrese con el numero de contrato            
            break;
    }

    console.log(JSON.stringify(datitos));
    console.log(url);

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(datitos)
    })
        .then(response => response.json())
        .then(data => {
            switch (entidad) {
                case 'administrador':
                    if (data.mensaje == "Autenticación exitosa") { // Si la validación es correcta
                        alert("Bienvenidx " + datitos.usuario); // Se muestra un mensaje de bienvenida
                        window.open("panel_admin.html", "_self"); // Se redirecciona a la página del administrador
                    } else {
                        console.log(data);
                        alert("Error al iniciar sesión, verifique sus datos"); // Se muestra un mensaje de error
                    }
                    break;
                case 'cliente':
                    if (data.mensaje == "Autenticación exitosa") { // Si la validación es correcta
                        alert("Bienvenidx " + datitos.usuario); // Se muestra un mensaje de bienvenida
                        window.open("src/panel_cliente.html", "_self"); // Se redirecciona a la página del cliente
                    } else {
                        console.log(data);
                        alert("Error al iniciar sesión, verifique sus datos"); // Se muestra un mensaje de error
                    }
                    break;
            }
        })
        .catch(error => console.error('Error al obtener datos de la API:', error)); // Imprimir en consola

}