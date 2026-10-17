from django.urls import path, include
from rest_framework import routers
from biblio_app import views

enrutador = routers.DefaultRouter()

enrutador.register(r'roles', views.RolViewSet)
enrutador.register(r'proveedores', views.ProveedorViewSet)
enrutador.register(r'clientes', views.ClienteViewSet)
enrutador.register(r'usuarios', views.UsuarioViewSet)
enrutador.register(r'categorias', views.CategoriaViewSet)
enrutador.register(r'bodegas', views.BodegaViewSet)
enrutador.register(r'productos', views.ProductoViewSet)
enrutador.register(r'inventario', views.InventarioViewSet)
enrutador.register(r'tipos-movimiento', views.TipoMovimientoViewSet)
enrutador.register(r'movimientos', views.MovimientoInventarioViewSet)
enrutador.register(r'auditoria', views.AuditoriaViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
]
