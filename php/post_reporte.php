<?php
// Establecer las cabeceras CORS
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Allow-Headers: Content-Type");
// Decodificar los datos JSON recibidos
$datitos = json_decode(file_get_contents("php://input"), true);
// Se guardan los datos del lado del cliente en variables
$sectorrep = $datitos["sectorrep"];
$motivorep = $datitos["motivorep"];
$fecharep = $datitos["fecharep"];
$estatusrep = $datitos["estatusrep"];
$clavecliente = $datitos["clavecliente"];
// Se manda a llamar la conexión a la base de datos
include_once "conexion_bd.php";
/*	Al incluir el archivo "base_de_datos.php", todas sus variables están a nuestra disposición. Por lo que podemos acceder a ellas tal como si hubiéramos copiado y pegado el código*/
$sentencia = $base_de_datos->prepare("INSERT INTO reportefallas(sectorRep, motivoRep, fechaRep, estatusRep, claveCliente) VALUES (?, ?, ?, ?, ?);");
# Pasar en el mismo orden de los ?
$resultado = $sentencia->execute([$sectorrep, $motivorep, $fecharep, $estatusrep, $clavecliente]); 
# execute regresa un booleano. True en caso de que todo vaya bien, falso en caso contrario. #Con eso podemos evaluar
if ($resultado === TRUE) {
    echo "Insertado correctamente";
} else {
    echo "Algo salió mal. Por favor verifica que la tabla exista";
}
