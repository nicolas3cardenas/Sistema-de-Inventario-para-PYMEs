from django.db import models

str_habilitado = "Habilitado"
str_fecha_creacion = "Fecha Creación"
str_fecha_actualizacion = "Fecha Actualización"
str_nombre = "Nombre"
str_descripcion = "Descripción"
str_email = "Email"
str_telefono = "Teléfono"
str_direccion = "Dirección"

class Rol(models.Model):
    nombre = models.CharField(str_nombre,max_length=30,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    class Meta:
        db_table_comment = "Perfiles de acceso al sistema (Administrador, Proveedor, etc.)."

class Proveedor(models.Model):
    nombre = models.CharField(str_nombre,max_length=100,null=False)
    razon_social = models.CharField("Razón Social",max_length=150,null=True)
    rut = models.CharField("RUT",max_length=12,null=False)
    correo = models.EmailField(str_email,null=True)
    telefono = models.CharField(str_telefono,max_length=15,null=True)
    direccion = models.CharField(str_direccion,max_length=150,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Proveedores que abastecen de productos a la PYME."

class Cliente(models.Model):
    nombre = models.CharField(str_nombre,max_length=100,null=False)
    rut = models.CharField("RUT",max_length=12,null=True)
    correo = models.EmailField(str_email,null=True)
    telefono = models.CharField(str_telefono,max_length=15,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Clientes a quienes se les realizan salidas (ventas) de productos."

class Usuario(models.Model):
    nombre = models.CharField(str_nombre,max_length=150,null=False)
    rut = models.CharField("RUT",max_length=12,null=False)
    correo = models.EmailField(str_email,null=True)
    telefono = models.CharField(str_telefono,max_length=15,null=True)
    contrasenia = models.CharField(max_length=128,null=True)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE,null=False)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Usuarios del sistema (administradores y proveedores) con su perfil de acceso."

class Categoria(models.Model):
    nombre = models.CharField(str_nombre,max_length=50,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Categorías para clasificar los productos."

class Bodega(models.Model):
    nombre = models.CharField(str_nombre,max_length=50,null=False)
    direccion = models.CharField(str_direccion,max_length=150,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Bodegas o sucursales donde se almacena el stock de productos."

class Producto(models.Model):
    sku = models.CharField("SKU",max_length=30,null=False)
    nombre = models.CharField(str_nombre,max_length=100,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    precio = models.DecimalField("Precio",max_digits=10,decimal_places=2,null=False)
    stock_minimo = models.IntegerField("Stock Mínimo",default=0,null=False)
    es_publico = models.BooleanField("Información Pública",default=True,null=False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=False)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Productos gestionados por la PYME."

class Inventario(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,null=False)
    bodega = models.ForeignKey(Bodega,on_delete=models.CASCADE,null=False)
    cantidad = models.IntegerField("Cantidad",default=0,null=False)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    class Meta:
        db_table_comment = "Stock actual de un producto en una bodega específica."

class TipoMovimiento(models.Model):
    nombre = models.CharField(str_nombre,max_length=30,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(str_habilitado,default=True,null=False)
    class Meta:
        db_table_comment = "Tipos de movimiento de inventario (Entrada, Salida, Ajuste, Devolución)."

class MovimientoInventario(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,null=False)
    bodega = models.ForeignKey(Bodega,on_delete=models.CASCADE,null=False)
    tipo_movimiento = models.ForeignKey(TipoMovimiento,on_delete=models.CASCADE,null=False)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True)
    cantidad = models.IntegerField("Cantidad",null=False)
    observacion = models.CharField("Observación",max_length=255,null=True)
    fecha_movimiento = models.DateTimeField("Fecha Movimiento",auto_now_add=True)
    class Meta:
        db_table_comment = "Histórico de entradas, salidas y ajustes de stock, asociados a un proveedor o cliente según corresponda."

class Auditoria(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True)
    entidad = models.CharField("Entidad Afectada",max_length=50,null=False)
    accion = models.CharField("Acción",max_length=30,null=False)
    detalle = models.CharField("Detalle",max_length=255,null=True)
    fecha_evento = models.DateTimeField("Fecha Evento",auto_now_add=True)
    class Meta:
        db_table_comment = "Registro de auditoría de acciones relevantes realizadas en el sistema."