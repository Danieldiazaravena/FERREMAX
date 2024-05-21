<?php
    header('Access-Control-Allow-Origin: *');
    header('Content-Type: application/json');

    include_once '../config/Database.php';
    include_once '../models/Ferremax_bodega.php';

    if ($_SERVER['REQUEST_METHOD'] === 'GET') {

        $db = new Database();
        $db = $db->connect();

        $producto = new Producto($db);

        $res = $producto->fetchAll();
        $resCount = $res->rowCount();

        if($resCount > 0) {

            $producto = array();

            while($row = $res->fetch(PDO::FETCH_ASSOC)) {

                extract($row);
                array_push($producto, array( 'id_producto' => $id_producto, 'nombre_producto' => $nombre_producto, 'precio' => $precio, 'descripcion' => $descripcion, 'stock_bodega' => $stock_bodega, 'id_marca' => $id_marca, 'id_categoria' => $id_categoria));
            }
            
            echo json_encode($producto);

        } else {
            echo json_encode(array('message' => "No records found!"));
        }
    } else {
        echo json_encode(array('message' => "Error: incorrect Method!"));
    }