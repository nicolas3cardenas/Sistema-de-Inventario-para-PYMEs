from django.shortcuts import render
from rest_framework import viewsets

from .models import Rol, Proveedor, Cliente, Usuario, Categoria, Bodega
from .models import Producto, Inventario, TipoMovimiento, MovimientoInventario, Auditoria

from .serializer import RolSerializer, ProveedorSerializer, ClienteSerializer, UsuarioSerializer
from .serializer import CategoriaSerializer, BodegaSerializer, ProductoSerializer, InventarioSerializer
from .serializer import TipoMovimientoSerializer, MovimientoInventarioSerializer, AuditoriaSerializer

# Create your views here.
# inicio es una vista basada en función FBV
def inicio(request):
    return render(request, 'inicio.html')

# Creación de vistas basadas en clase (CBV), un ModelViewSet entrega
# automáticamente el CRUD completo (GET, POST, PUT, PATCH, DELETE)
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class TipoMovimientoViewSet(viewsets.ModelViewSet):
    queryset = TipoMovimiento.objects.all()
    serializer_class = TipoMovimientoSerializer

class MovimientoInventarioViewSet(viewsets.ModelViewSet):
    queryset = MovimientoInventario.objects.all()
    serializer_class = MovimientoInventarioSerializer

class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer
