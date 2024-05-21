<?php
    header('Access-Control-Allow-Origin: *');
    header('Content-Type: application/json');

    include_once '../config/Database.php';
    include_once '../models/Ferremax_bodega.php';

    if ($_SERVER['REQUEST_METHOD'] === 'GET') {

        $db = new Database();
        $db = $db->connect();

        $producto = new Producto($db);

        $data = json_decode(file_get_contents("php://input"));

        if(isset($data->id_producto)) {
            $producto->id_producto = $data->id_producto;

            if($producto->fetchOne()) {

                print_r(json_encode(array(
                    'id_producto' => $producto->id_producto,
                    'nombre_producto' => $producto->nombre_producto,
                    'precio' => $producto->precio,
                    'descripcion' => $producto->descripcion,
                    'stock_bodega' => $producto->stock_bodega,
                    'id_marca' => $producto->id_marca,
                    'id_categoria' => $producto->id_categoria,
                )));

            } else {
                echo json_encode(array('message' => "¡No se encontraron registros!"));
            }

        } else {
            echo json_encode(array('message' => "Error: ¡Ingrese ID del producto!"));
        }
    } else {
        echo json_encode(array('message' => "Error: ¡Método incorrecto!"));
    }