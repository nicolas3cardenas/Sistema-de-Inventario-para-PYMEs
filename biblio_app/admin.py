from django.contrib import admin
from .models import Rol
from .models import Proveedor
from .models import Cliente
from .models import Usuario
from .models import Categoria
from .models import Bodega
from .models import Producto
from .models import Inventario
from .models import TipoMovimiento
from .models import MovimientoInventario
from .models import Auditoria

# Register your models here.
admin.site.register(Rol)
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Bodega)
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(TipoMovimiento)
admin.site.register(MovimientoInventario)
admin.site.register(Auditoria)
