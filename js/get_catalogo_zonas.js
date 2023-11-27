const tabla = document.getElementById('catalogoZonas'); // Obtener la referencia a la tabla
const tbody = tabla.querySelector('tbody'); // Obtener la referencia al cuerpo de la tabla

fetch('http://localhost:8000/api/zonas/') // Devuelve una promesa
    .then(response => response.json()) // Devuelve otra promesa
    .then(data => { // Devuelve otra promesa
        // Llenar la tabla con los datos recibidos
        data.zonas.sort((a, b) => a.codigopostal - b.codigopostal); // Ordenar los datos por código postal
        data.zonas.forEach(item => { // Supongamos que los datos son un array
            const row = document.createElement('tr'); // Crear una fila
            row.innerHTML = `<td>${item.codigopostal}</td><td>${item.colonia}</td>`; // Ajustar según la estructura de tus datos
            // Añadir más celdas según tus datos
            tbody.appendChild(row); // Agregar la fila al cuerpo de la tabla
        });
    })
    .catch(error => console.error('Error al obtener datos de la API:', error)); // Imprimir en consola