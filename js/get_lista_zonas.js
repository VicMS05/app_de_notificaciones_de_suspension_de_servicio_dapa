// Obtener la referencia al elemento de lista desplegable en el DOM
const listaDesplegable = document.getElementById('sector');

// Realizar la solicitud GET con Fetch
fetch('php/get_zonas.php') // Devuelve una promesa
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
    console.log('Datos recibidos:', data); // Imprimir en consola
    if (Array.isArray(data)) {
      data.forEach(item => { // Supongamos que los datos son un array
        // Crear una opción para cada elemento en los datos y agregarlo a la lista desplegable
        const opcion = document.createElement('option'); // Crear un elemento option
        opcion.textContent = item.colonia; // Ajusta según la estructura de tus datos
        listadesplegable.appendChild(opcion); // Agregar la opción a la lista desplegable
      });
    } else {
      console.error('La propiedad "zonas" no es un array:', data.zonas);
    }
  })
  .catch(error => { // Devuelve otra promesa
    // Capturar y manejar errores
    console.error('Error en la solicitud:', error); // Imprimir en consola
  });