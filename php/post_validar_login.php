<?php
// Establecer las cabeceras CORS
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Allow-Headers: Content-Type");
// Decodificar los datos JSON recibidos
$datitos = json_decode(file_get_contents("php://input"), true);
// Se guardan los datos del lado del cliente en variables
$usuarioIngresado = $datitos["usuario"];
$contraseñaIngresada = $datitos["contraseña"];
// Obtener el hash almacenado
$contraseñaAlmacenada = obtenerHashDeLaBaseDeDatos($usuarioIngresado);
// Verificar la contraseña
if ($contraseñaAlmacenada !== null && password_verify($contraseñaIngresada, $contraseñaAlmacenada)) {
    // La contraseña es válida
    $respuesta = array("mensaje" => "Autenticación exitosa");
} else {
    // La contraseña no es válida o el usuario no fue encontrado
    $respuesta = array("mensaje" => "Error de autenticación", "contraseña" => $contraseñaAlmacenada);
}
// Enviar la respuesta en formato JSON
header('Content-Type: application/json');
echo json_encode($respuesta);

function obtenerHashDeLaBaseDeDatos($usuarioIngresado) {
    // Se manda a llamar la conexión a la base de datos
    include_once "conexion_bd.php";
    try {
        // Utilizar una consulta preparada para prevenir inyección SQL
        $sentencia = $base_de_datos->prepare("SELECT contraCliente FROM cliente WHERE idCliente = '$usuarioIngresado' OR correoCliente = '$usuarioIngresado'");
        // $sentencia->bindParam(':usuarioIngresado', $usuarioIngresado);
        // $sentencia->debugDumpParams();
        $sentencia->execute();
        // Verificar si la consulta se realizó correctamente
        if ($sentencia->rowCount() > 0) {
            // Obtener el hash almacenado
            $fila = $sentencia->fetch(PDO::FETCH_ASSOC);
            $hashAlmacenado = $fila['contraCliente'];
            // Devolver el hash obtenido
            return $hashAlmacenado;
        } else {
            // El usuario no fue encontrado en la base de datos
            return null;
        }
    } catch (PDOException $e) {
        // Manejar cualquier error de la base de datos
        // Puedes registrar el error, lanzar una excepción, o manejarlo de otra manera según tus necesidades
        echo "Error en la consulta2: " . $e->getMessage();
        return null;
    }
}
?>
