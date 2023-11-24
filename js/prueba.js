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
const apiUrl = 'http://localhost:8000/zonas/';

// Obtener la referencia al elemento de lista desplegable en el DOM
const listaDesplegable = document.getElementById('listadesplegable');

// Realizar la solicitud GET con Fetch
fetch(apiUrl)
  .then(response => {
    // Verificar si la respuesta es exitosa (código 200)
    if (!response.ok) {
      throw new Error(`Error en la solicitud: ${response.status}`);
    }

    // Convertir la respuesta a formato JSON
    return response.json();
  })
  .then(data => {
    // Manipular los datos recibidos
    data.forEach(item => {
      // Crear una opción para cada elemento en los datos y agregarlo a la lista desplegable
      const opcion = document.createElement('<option>');
      opcion.value = item.id; // Supongamos que hay un campo 'id' en los datos
      opcion.textContent = item.nombre; // Ajusta según la estructura de tus datos
      listaDesplegable.appendChild(opcion);
    });
  })
  .catch(error => {
    // Capturar y manejar errores
    console.error('Error en la solicitud:', error);
  });