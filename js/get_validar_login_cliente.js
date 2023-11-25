
function validarInicioSesionCliente() {
    
    var usuario = document.getElementById("usuario").value;
    var contraseña = document.getElementById("password-input1").value;
    
    fetch('http://localhost:8000/api/clientes/' + usuario)
    .then(response => response.json())
    .then(data => {
        if (data.cliente && data.cliente.nombrecliente != null && data.cliente.contracliente == contraseña) {
            window.open('http://localhost:5500/src/panel_cliente.html', "_self")
        } else {
            alert("Usuario o contraseña incorrectos");
        }
    })
    .catch(error => console.error('Error al obtener datos de la API:', error)); // Imprimir en consola
    
}