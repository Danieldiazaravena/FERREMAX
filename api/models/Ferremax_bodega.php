<?php

class Producto {

    private $conn;

    public $id_producto;
    public $nombre_producto;
    public $precio;
    public $descripcion;
    public $stock_bodega;
    public $id_marca;
    public $id_categoria;


    

    public function __construct($db){
        $this->conn = $db;
    }

    public function fetchAll() {
        
        $stmt = $this->conn->prepare('SELECT * FROM Producto');
        $stmt->execute();
        return $stmt;
    }

    public function fetchOne() {

        $stmt = $this->conn->prepare('SELECT  * FROM Producto WHERE id_producto = ?');
        $stmt->bindParam(1, $this->id_producto);
        $stmt->execute();        

        if($stmt->rowCount() > 0) {
            
            $row = $stmt->fetch(PDO::FETCH_ASSOC);

            $this->id_producto = $row['id_producto'];
            $this->nombre_producto = $row['nombre_producto'];
            $this->precio = $row['precio'];
            $this->descripcion = $row['descripcion'];
            $this->stock_bodega = $row['stock_bodega'];
            $this->id_marca = $row['id_marca'];
            $this->id_categoria = $row['id_categoria'];
            

            return TRUE;

        }
        
        return FALSE;
    }

    public function postData() {

        $stmt = $this->conn->prepare('INSERT INTO Producto SET id_producto = :id_producto, nombre_producto = :nombre_producto, precio = :precio, descripcion = :descripcion, stock_bodega = :stock_bodega, id_marca = :id_marca, id_categoria = :id_categoria');

        $stmt->bindParam(':id_producto', $this->id_producto);
        $stmt->bindParam(':nombre_producto', $this->nombre_producto);
        $stmt->bindParam(':precio', $this->precio);
        $stmt->bindParam(':descripcion', $this->descripcion);
        $stmt->bindParam(':stock_bodega', $this->stock_bodega);
        $stmt->bindParam(':id_marca', $this->id_marca);
        $stmt->bindParam(':id_categoria', $this->id_categoria);

        if($stmt->execute()) {
            return TRUE;
        }

        return FALSE;
    }

    public function putData() {

        $stmt = $this->conn->prepare('UPDATE Producto SET nombre_producto = :nombre_producto, precio = :precio, descripcion = :descripcion, stock_bodega = :stock_bodega, id_marca = :id_marca, id_categoria = :id_categoria');

        $stmt->bindParam(':nombre_producto', $this->nombre_producto);
        $stmt->bindParam(':precio', $this->precio);
        $stmt->bindParam(':descripcion', $this->descripcion);
        $stmt->bindParam(':stock_bodega', $this->stock_bodega);
        $stmt->bindParam(':id_marca', $this->id_marca);
        $stmt->bindParam(':id_categoria', $this->id_categoria);

        if($stmt->execute()) {
            return TRUE;
        }

        return FALSE;
    }

    public function delete() {

        $stmt = $this->conn->prepare('DELETE FROM Producto WHERE id_producto = :id_producto');
        $stmt->bindParam(':id_producto', $this->id_producto);

        if($stmt->execute()) {
            return TRUE;
        }

        return FALSE;
    }


}