<?php
// Incluimos el archivo que contiene la conexión a la base de datos
include_once "conexion_bd.php";
// Realizamos una consulta a la base de datos para obtener todas las personas
$sentencia = $base_de_datos->query("SELECT * FROM administrador;");
// Obtenemos todas las filas de la consulta como objetos
$administradores = $sentencia->fetchAll(PDO::FETCH_OBJ);
// Convertimos el array de objetos a formato JSON
$json_result = json_encode($administradores);
// Devolvemos el resultado JSON
echo $json_result;
?>