<?php
/*
	CRUD con MySQL y PHP
	Esta es una conexión a la base de datos MySQL utilizando PDO en PHP.
	El archivo se conecta a la base de datos "pruebas" en localhost utilizando el usuario "root" y sin contraseña.
*/
$contraseña = "";
$usuario = "root";
$nombre_base_de_datos = "serviciodapa";
try{
	$base_de_datos = new PDO('mysql:host=localhost;dbname=' . $nombre_base_de_datos, $usuario, $contraseña);
}catch(Exception $e){
	echo "Ocurrió algo con la base de datos: " . $e->getMessage();
}
?>