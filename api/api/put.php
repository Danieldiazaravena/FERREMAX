<?php
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');
header('Access-Control-Allow-Methods: PUT');

include_once '../config/Database.php';
include_once '../models/Ferremax_bodega.php';

if ($_SERVER['REQUEST_METHOD'] === 'PUT') {

    $db = new Database();
    $db = $db->connect();

    $data = json_decode(file_get_contents("php://input"));

    $id_producto = isset($data->id_producto) ? $data->id_producto : null;
    $nombre_producto = isset($data->nombre_producto) ? $data->nombre_producto : null;
    $precio = isset($data->precio) ? $data->precio : null;
    $descripcion = isset($data->descripcion) ? $data->descripcion : null;
    $stock_bodega = isset($data->stock_bodega) ? $data->stock_bodega : null;
    $id_marca = isset($data->id_marca) ? $data->id_marca : null;
    $id_categoria = isset($data->id_categoria) ? $data->id_categoria : null;

    if (!is_null($id_producto)) {
        $query = 'UPDATE Producto SET nombre_producto = :nombre_producto, precio = :precio, descripcion = :descripcion, stock_bodega = :stock_bodega, id_marca = :id_marca, id_categoria = :id_categoria WHERE id_producto = :id_producto';
        $stmt = $db->prepare($query);
        $stmt->bindParam(':id_producto', $id_producto);
        $stmt->bindParam(':nombre_producto', $nombre_producto);
        $stmt->bindParam(':precio', $precio);
        $stmt->bindParam(':descripcion', $descripcion);
        $stmt->bindParam(':stock_bodega', $stock_bodega);
        $stmt->bindParam(':id_marca', $id_marca);
        $stmt->bindParam(':id_categoria', $id_categoria);

        if ($stmt->execute()) {
            echo json_encode(array('message' => 'Producto actualizado'));
        } else {
            echo json_encode(array('message' => 'No se pudo actualizar el producto'));
        }
    } else {
        echo json_encode(array('message' => 'Error: Falta el ID del producto'));
    }
} else {
    echo json_encode(array('message' => 'Error: Método incorrecto'));
}
?>
