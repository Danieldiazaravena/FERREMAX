<?php
    header('Access-Control-Allow-Origin: *');
    header('Content-Type: application/json');
    header('Access-Control-Allow-Methods: POST');

    include_once '../config/Database.php';
    include_once '../models/Ferremax_bodega.php';

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {

      $db = new Database();
      $db = $db->connect();

      $producto = new Producto($db);

      $data = json_decode(file_get_contents("php://input"));

      $producto->nombre_producto = $data->nombre_producto;
      $producto->precio = $data->precio;
      $producto->descripcion = $data->descripcion;
      $producto->stock_bodega = $data->stock_bodega;
      $producto->id_marca = $data->id_marca;
      $producto->id_categoria = $data->id_categoria;
    
      if($producto->postData()) {
        echo json_encode(array('message' => '¡Producto añadido!'));
      } else {
        echo json_encode(array('message' => 'Hubo un problema al añadir el producto'));
      }
    } else {
        echo json_encode(array('message' => "Error"));
    }