from rest_framework import serializers

from .models import Rol, Proveedor, Cliente, Usuario, Categoria, Bodega
from .models import Producto, Inventario, TipoMovimiento, MovimientoInventario, Auditoria

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('__all__')

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('__all__')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = ('__all__')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('__all__')

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ('__all__')

class TipoMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMovimiento
        fields = ('__all__')

class MovimientoInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoInventario
        fields = ('__all__')

class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria
        fields = ('__all__')
