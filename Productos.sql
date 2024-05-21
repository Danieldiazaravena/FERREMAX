INSERT INTO website_categoria (id_categoria, nombre_categoria)
VALUES (1,
		'Taladros');
INSERT INTO website_categoria (id_categoria, nombre_categoria)
VALUES (2,
		'Esmeriles');
INSERT INTO website_categoria (id_categoria, nombre_categoria)
VALUES (3,
		'Cepillos');
INSERT INTO website_categoria (id_categoria, nombre_categoria)
VALUES (4,
		'Rotomartillo');
INSERT INTO website_categoria (id_categoria, nombre_categoria)
VALUES (5,
		'Pulidora');        
INSERT INTO website_categoria (id_categoria, nombre_categoria)
VALUES (6,
		'Sierra Circular'); 

INSERT INTO website_marca(id_marca, nombre_marca)
VALUES (1,
		'Bosch');
INSERT INTO website_marca(id_marca, nombre_marca)
VALUES (2,
		'Makita');
INSERT INTO website_marca(id_marca, nombre_marca)
VALUES (3,
		'DeWalt');

INSERT INTO website_producto (id_producto, nombre_producto, precio, descripcion, id_categoria, cant_inventario, id_marca) 
VALUES (1, 
		'Taladro Percutor Bosch GSB 550 RE 550W', 
        48990,
        'El Taladro Percutor Bosch GSB 550 RE, con potencia de 550 W, es la mejor elección para quien busca la confianza de la marca Bosch por un precio imbatible. Cómodo y liviano, con apenas 1,7 Kg, perfora albañilería, madera y metal, con y sin impacto, gracias al botón conmutador. Realiza también, atornillados a través de la función de reversión y realiza trabajos continuos con la ayuda del botón de bloqueo. Cuenta con 1 año de garantía Bosch.',
        1,
        2,
        1);
INSERT INTO website_producto (id_producto, nombre_producto, precio, descripcion, id_categoria, cant_inventario, id_marca) 
VALUES (2, 
		'Esmeril angular Bosch GWS 9-125 S 900W', 
        94700,
        'El Esmeril angular Bosch GWS 9 -125 S tiene 900 Watts de potencia siendo esta una solución para realizar cortes y desbastes en materiales metálicos, como hierro y acero, y también puede ser utilizada para corte en mampostería y concreto. Es importante mencionar que para cada tipo de aplicación existe un accesorio recomendado como los discos abrasivos o discos diamantados. El Esmeril angular Bosch GWS 9 -125 S cuenta con una cubierta de protección de 5" / 125 milímetros con sistema de fijación por medio de tornillo que garantiza que la cubierta no se mueva en caso de que el disco se rompa, proporcionando de esta manera más seguridad al operador de la herramienta.',
        1,
        2,
        1);
INSERT INTO website_producto (id_producto, nombre_producto, precio, descripcion, id_categoria, cant_inventario, id_marca) 
VALUES (3, 
		'Cepillo 82Mm 18V LXT Corte 2,0Mm 14.000Rpm', 
        220300,
        'Empuñadura antideslizante rallada, con mejor ergonomía y más manejable.Ajuste preciso de la profundidad mediante pomo con escala.Pie de apoyo en la base posterior del cepillo.Base en V para un sencillo achaflanado.Carcasa lateral en fundición de aluminio, para una mayor estabilidad de los rodamientos.Tipo de batería: LXTTensión de la batería: 18 VVelocidad: 14.000 RPMAncho de Cepillado: 82 mmProfundidad máx. De Corte: 2.0 mmProfundidad máx. De Galce: 9 mmEmisión de Vibración: 4.50 m/seg²Incertidumbre de Vibración: 1.50 m/seg²',
        3,
        2,
        2);
INSERT INTO website_producto (id_producto, nombre_producto, precio, descripcion, id_categoria, cant_inventario, id_marca) 
VALUES (4, 
		'Rotomartillo SDS PLUS de 9/16" (14mm) Inalámbrico 12V MAX* de 1.1J', 
        212990,
        'El motor sin carbones DEWALT y el mecanismo de ingeniería Alemana, ofrecen 1.1J de energía de impacto. Su diseño compacto y liviano hace que sea una herramienta ideal para montar perfiles estructurales, instalaciones de conductos, anclajes para tuberías y aplicaciones de mantenimiento, reparación y operaciones, cuando se usan con anclajes para mampostería livianos. Cuenta con 3 Años de Garantía Limitada, 1 Año de Mantenimiento Gratis y 90 Días de Satisfacción Garantizada',
        4,
        2,
        3);
INSERT INTO website_producto (id_producto, nombre_producto, precio, descripcion, id_categoria, cant_inventario, id_marca) 
VALUES (5, 
		'Pulidora giratoria de velocidad variable de 7” (180 mm) de 20V MAX', 
        129990,
        'Interruptor de bloqueo de encendido. Motor sin escobillas (Brushless) ofrece 57% más tiempo de ejecución que las herramientas con escobillas. Aplicaciones y uso para discos 7” (180 mm).Ergonomía del mango mejorada para mayor comodidad. Mango lateral Recubierto de goma. Control de velocidad variable. No incluye bateria  ',
        5,
        2,
        3);
        
INSERT INTO website_producto (id_producto, nombre_producto, precio, descripcion, id_categoria, cant_inventario, id_marca) 
VALUES (6, 
		'Sierra Circular Eléctrica de 7 1/4" (185mm) de 1500W', 
        329990,
        'Nueva sierra circular con cable de 1500W y 7,1/4" (185mm), centrada en la durabilidad, el rendimiento, la asequibilidad y la facilidad de uso, ampliando la cartera actual de soluciones con una cartera de productos con una buena relación calidad-precio para profesionales. El soplador de polvo limpia el polvo y los residuos de la línea de corte. Puerto de extracción de polvo eficiente para minimizar las partículas de polvo en el aire cuando se conecta a una unidad de extracción de polvo ',
        6,
        2,
        3);
        
INSERT INTO website_estado (id_envio, nombre)
VALUES(1,
	   'Pendiente');
INSERT INTO website_estado (id_envio, nombre)
VALUES(2,
	   'En Despacho');
INSERT INTO website_estado (id_envio, nombre)
VALUES(3,
	   'Entregado');
       
INSERT INTO auth_group(id, name)
VALUES(1,
	   'vendedor');
INSERT INTO auth_group(id, name)
VALUES(2,
	   'bodeguero');
INSERT INTO auth_group(id, name)
VALUES(3,
	   'contador');
INSERT INTO auth_group(id, name)
VALUES(4,
	   'cliente');

INSERT INTO website_imagen_producto(id_imagen_p, imagen_producto, id_producto)
VALUES(1,
	   'productos/1.webp',
       1);
INSERT INTO website_imagen_producto(id_imagen_p, imagen_producto, id_producto)
VALUES(2,
	   'productos/2.webp',
       2);
INSERT INTO website_imagen_producto(id_imagen_p, imagen_producto, id_producto)
VALUES(3,
	   'productos/3.webp',
       3);
INSERT INTO website_imagen_producto(id_imagen_p, imagen_producto, id_producto)
VALUES(4,
	   'productos/4.jpg',
       4);
INSERT INTO website_imagen_producto(id_imagen_p, imagen_producto, id_producto)
VALUES(5,
	   'productos/5.jpg',
       5);
INSERT INTO website_imagen_producto(id_imagen_p, imagen_producto, id_producto)
VALUES(6,
	   'productos/6.jpg',
       6);
