from django.db import models

# CATEGORIA DEL PRODUCTO
class Categoria(models.Model):
    id_categoria = models.AutoField(db_column="id_categoria", primary_key=True)
    nombre_categoria = models.CharField(max_length=45)

    def __str__(self):
        return str(self.nombre_categoria)
    
#Producto
class Producto(models.Model):
    id_producto = models.AutoField(db_column="id_producto", primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=400)
    id_categoria = models.ForeignKey(
        "Categoria", on_delete=models.CASCADE, db_column="id_categoria"
    )

    def __str__(self):
        return str(self.nombre_producto)
    
class Imagen_producto(models.Model):
    id_imagen_p = models.AutoField(db_column="id_imagen_p", primary_key=True)
    imagen_producto = models.FileField(upload_to="productos/", null=True)
    id_producto = models.ForeignKey(
        "Producto", on_delete=models.CASCADE, db_column="id_producto"
    )

    def __str__(self):
        return str(self.id_imagen_p)