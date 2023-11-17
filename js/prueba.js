console.log('Jake')

const URL = 'https://api.thecatapi.com/v1/images/search';

fetch(URL)
    .then(res => res.json())
    .then(data => {
        const img = document.querySelector('img');
        img.src = data[0].url;
});

document.getElementById('boton-fetch').addEventListener('click', function() {
fetch(URL)
    .then(res => res.json())
    .then(data => {
        const img = document.querySelector('img');
        img.src = data[0].url;
    });
});

function mostrarMensajeBienvenida() {
    window.alert("¡Bienvenido a nuestro sitio web!");
}

function confirmarAccion() {
    var resultado = window.confirm("¿Estás seguro?");
    if (resultado === true) {
        window.alert("¡Estás seguro!");
    } else {
        window.alert("Pareces indeciso");
    }
}

function solicitarInformacion() {
    var edad = prompt("¿Cuántos años tienes?", "100");
    if (edad !== null) {
        window.alert("Tienes " + edad + " años.");
    }
}
document.getElementById('msj-login').addEventListener('click', function(){
    mostrarMensajeBienvenida();
});


