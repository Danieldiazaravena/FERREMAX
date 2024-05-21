<?php
    header('Access-Control-Allow-Origin: *');
    header('Content-Type: application/json');
    header('Access-Control-Allow-Methods: POST');

    include_once '../config/Database.php';
    include_once '../models/Ferremax_bodega.php';

	if ($_SERVER['REQUEST_METHOD'] === 'DELETE') {

		$db = new Database();
		$db = $db->connect();

		$producto = new Producto($db);

		$data = json_decode(file_get_contents("php://input"));

		$producto->id_producto = isset($data->id_producto) ? $data->id_producto : NULL;

		if(! is_null($producto->id_producto)) {
	
			if($producto->delete()) {
			echo json_encode(array('message' => 'Producto borrado'));
			} else {
			echo json_encode(array('message' => 'No se pudo borrar el producot, vuelva a intentarlo'));
			}
		} else {
		echo json_encode(array('message' => "Error: ¡Falta el ID del producto!"));
		}
	} else {
		echo json_encode(array('message' => "Error: ¡Método incorrecto!"));
	}