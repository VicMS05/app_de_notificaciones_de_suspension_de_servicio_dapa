<?php
// Establecer las cabeceras CORS
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Allow-Headers: Content-Type");
// Decodificar los datos JSON recibidos
$datos = json_decode(file_get_contents("php://input"), true);
// Se guardan los datos del lado del cliente en variables
$nombreadmin = $datos["nombreadmin"];
$appatadmin = $datos["appatadmin"];
$apmatadmin = $datos["apmatadmin"];
$contraadmin = password_hash($datos["contraadmin"], PASSWORD_DEFAULT);
$correoadmin = $datos["correoadmin"];
// Se manda a llamar la conexión a la base de datos
include_once "conexion_bd.php";
/*	Al incluir el archivo "base_de_datos.php", todas sus variables están a nuestra disposición. Por lo que podemos acceder a ellas tal como si hubiéramos copiado y pegado el código*/
$sentencia = $base_de_datos->prepare("INSERT INTO administrador(nombreAdmin, apPatAdmin, apMatAdmin, contraAdmin, correoAdmin) VALUES (?, ?, ?, ?, ?);");
# Pasar en el mismo orden de los ?
$resultado = $sentencia->execute([$nombreadmin, $appatadmin, $apmatadmin, $contraadmin, $correoadmin]); 
# execute regresa un booleano. True en caso de que todo vaya bien, falso en caso contrario. #Con eso podemos evaluar
if ($resultado === TRUE) {
    echo "Insertado correctamente";
} else {
    echo "Algo salió mal. Por favor verifica que la tabla exista";
}
