<?php

class Database {
    private $host = "localhost";
    private $user = "root";
    private $db = "test";
    private $pwd = "";
    private $conn = NULL;

    public function connect() {

        try{
            $this->conn = new PDO("mysql:host=$this->host;port=3308;dbname=$this->db", $this->user, $this->pwd, );
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch(PDOException $e) {
            echo "Connection Error: " . $e->getMessage();
        }

        return $this->conn;
    }
}