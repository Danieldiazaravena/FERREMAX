-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 17, 2021 at 07:21 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.3.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--


-- --------------------------------------------------------

CREATE TABLE `Marca` (
  `id_marca` int(11) UNSIGNED NOT NULL,
  `nombre_marca` varchar(100) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id_marca`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Categoria` (
  `id_categoria` int(11) UNSIGNED NOT NULL,
  `nombre_categoria` varchar(100) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Producto` (
  `id_producto` int(11) UNSIGNED NOT NULL,
  `nombre_producto` varchar(100) CHARACTER SET utf8 NOT NULL,
  `precio` int(11) NOT NULL,
  `descripcion` varchar(400) CHARACTER SET utf8 NOT NULL,
  `stock_bodega` int(5) NOT NULL,
  `id_marca` int(11) NOT NULL,
  `id_categoria` int(11) NOT NULL,
  PRIMARY KEY (`id_producto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `Marca` MODIFY COLUMN `id_marca` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;
ALTER TABLE `Categoria` MODIFY COLUMN `id_categoria` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;
ALTER TABLE `Producto` MODIFY COLUMN `id_producto` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;

INSERT INTO `Categoria` 
VALUES (1,'Taladros');
INSERT INTO `Categoria`
VALUES (2,'Esmeriles');
INSERT INTO `Categoria` 
VALUES (3,'Cepillos');
INSERT INTO `Categoria`
VALUES (4,'Rotomartillo');
INSERT INTO `Categoria`
VALUES (5,'Pulidora');        
INSERT INTO `Categoria`
VALUES (6,'Sierra Circular'); 

INSERT INTO `Marca`
VALUES (1,'Bosch');
INSERT INTO `Marca`
VALUES (2,'Makita');
INSERT INTO `Marca`
VALUES (3,'DeWalt');

INSERT INTO `Producto` 
VALUES (1, 'Taladro Percutor Bosch GSB 550 RE 550W', 48990,'El Taladro Percutor Bosch GSB 550 RE, con potencia de 550 W, es la mejor elección para quien busca la confianza de la marca Bosch por un precio imbatible. Cómodo y liviano, con apenas 1,7 Kg, perfora albañilería, madera y metal, con y sin impacto, gracias al botón conmutador. Realiza también, atornillados a través de la función de reversión y realiza trabajos continuos con la ayuda del botón de bloqueo. Cuenta con 1 año de garantía Bosch.',2,1,1);
INSERT INTO `Producto`  
VALUES (2,'Esmeril angular Bosch GWS 9-125 S 900W',94700,'El Esmeril angular Bosch GWS 9 -125 S tiene 900 Watts de potencia siendo esta una solución para realizar cortes y desbastes en materiales metálicos, como hierro y acero, y también puede ser utilizada para corte en mampostería y concreto. Es importante mencionar que para cada tipo de aplicación existe un accesorio recomendado como los discos abrasivos o discos diamantados. El Esmeril angular Bosch GWS 9 -125 S cuenta con una cubierta de protección de 5" / 125 milímetros con sistema de fijación por medio de tornillo que garantiza que la cubierta no se mueva en caso de que el disco se rompa, proporcionando de esta manera más seguridad al operador de la herramienta.',2,1,2);
INSERT INTO `Producto`  
VALUES (3, 'Cepillo 82Mm 18V LXT Corte 2,0Mm 14.000Rpm', 220300,'Empuñadura antideslizante rallada, con mejor ergonomía y más manejable.Ajuste preciso de la profundidad mediante pomo con escala.Pie de apoyo en la base posterior del cepillo.Base en V para un sencillo achaflanado.Carcasa lateral en fundición de aluminio, para una mayor estabilidad de los rodamientos.Tipo de batería: LXTTensión de la batería: 18 VVelocidad: 14.000 RPMAncho de Cepillado: 82 mmProfundidad máx. De Corte: 2.0 mmProfundidad máx. De Galce: 9 mmEmisión de Vibración: 4.50 m/seg²Incertidumbre de Vibración: 1.50 m/seg²',2,2,3);
INSERT INTO `Producto` 
VALUES (4, 'Rotomartillo SDS PLUS de 9/16" (14mm) Inalámbrico 12V MAX* de 1.1J', 212990,'El motor sin carbones DEWALT y el mecanismo de ingeniería Alemana, ofrecen 1.1J de energía de impacto. Su diseño compacto y liviano hace que sea una herramienta ideal para montar perfiles estructurales, instalaciones de conductos, anclajes para tuberías y aplicaciones de mantenimiento, reparación y operaciones, cuando se usan con anclajes para mampostería livianos. Cuenta con 3 Años de Garantía Limitada, 1 Año de Mantenimiento Gratis y 90 Días de Satisfacción Garantizada',2,2,4);
INSERT INTO `Producto` 
VALUES (5, 'Pulidora giratoria de velocidad variable de 7” (180 mm) de 20V MAX', 129990,'Interruptor de bloqueo de encendido. Motor sin escobillas (Brushless) ofrece 57% más tiempo de ejecución que las herramientas con escobillas. Aplicaciones y uso para discos 7” (180 mm).Ergonomía del mango mejorada para mayor comodidad. Mango lateral Recubierto de goma. Control de velocidad variable. No incluye bateria  ',2,3,5);
INSERT INTO `Producto` 
VALUES (6,'Sierra Circular Eléctrica de 7 1/4" (185mm) de 1500W', 329990,'Nueva sierra circular con cable de 1500W y 7,1/4" (185mm), centrada en la durabilidad, el rendimiento, la asequibilidad y la facilidad de uso, ampliando la cartera actual de soluciones con una cartera de productos con una buena relación calidad-precio para profesionales. El soplador de polvo limpia el polvo y los residuos de la línea de corte. Puerto de extracción de polvo eficiente para minimizar las partículas de polvo en el aire cuando se conecta a una unidad de extracción de polvo ',2,3,6);




/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
