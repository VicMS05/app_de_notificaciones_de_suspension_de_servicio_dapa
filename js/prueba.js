const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');
const registerBtn1 = document.getElementById('registarBtn1');

registerBtn.addEventListener('click', () => {
  container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
  container.classList.remove("active");
});

registerBtn1.addEventListener('click', () => {
  container.classList.remove("active");
});

registerBtn1.addEventListener('click', (e) => {
  e.preventDefault();
});

//Metodo get para la lista desplegable
// URL del endpoint de la API Django, asumiendo que está en el mismo servidor
const apiUrl = 'http://localhost:8000/api/zonas/';

// Obtener la referencia al elemento de lista desplegable en el DOM
const listaDesplegable = document.getElementById('listadesplegable');

// Realizar la solicitud GET con Fetch
fetch(apiUrl) // Devuelve una promesa
  .then(response => { // Devuelve otra promesa
    // Verificar si la respuesta es exitosa (código 200)
    if (!response.ok) { // ok devuelve true si el código de estado HTTP está en el rango 200-299
      throw new Error(`Error en la solicitud: ${response.status}`); // Lanzar un error
    }

    // Convertir la respuesta a formato JSON
    return response.json(); // Devuelve otra promesa
  })
  .then(data => { // Devuelve otra promesa
    // Manipular los datos recibidos
    if (Array.isArray(data.zonas)) {
      data.zonas.forEach(item => { // Supongamos que los datos son un array
        // Crear una opción para cada elemento en los datos y agregarlo a la lista desplegable
        const opcion = document.createElement('option'); // Crear un elemento option
        opcion.textContent = item.colonia; // Ajusta según la estructura de tus datos
        listaDesplegable.appendChild(opcion); // Agregar la opción a la lista desplegable
      });
    } else {
      console.error('La propiedad "zonas" no es un array:', data.zonas);
    }
  })
  .catch(error => { // Devuelve otra promesa
    // Capturar y manejar errores
    console.error('Error en la solicitud:', error); // Imprimir en consola
  });