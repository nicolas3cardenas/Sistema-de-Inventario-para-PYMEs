# StockPYME — Sistema de Inventario para PYMEs

Proyecto backend desarrollado con Python, Django y Django REST Framework para la
asignatura de Programación Backend (INACAP). Corresponde a la **Evaluación N.° 2**:
API REST completa con operaciones CRUD sobre el modelo de datos del proyecto
individual asignado.

**Problema que resuelve:** una PYME necesita centralizar el seguimiento de su
inventario de productos (actualmente disperso en distintos registros), controlar
el stock por bodega, mantener un histórico de movimientos (entradas de
proveedores, salidas a clientes, ajustes) y dejar un registro de auditoría de
los eventos relevantes del sistema.

## Arquitectura del proyecto

```
IEI_N4_C1-main/
├── core/                      # Núcleo Django
│   ├── settings.py            # Configuración (DB MySQL vía .env, DRF, apps)
│   ├── urls.py                # Enrutador principal del proyecto
│   ├── wsgi.py / asgi.py
├── biblio_app/                 # Aplicación del proyecto
│   ├── models.py               # Modelo de datos (11 entidades)
│   ├── serializer.py           # Serializadores DRF (Modelo -> JSON)
│   ├── views.py                 # ModelViewSets (CRUD) + vista de bienvenida
│   ├── urls.py                  # Router DRF: registra cada ViewSet
│   ├── admin.py                 # Registro de modelos en el panel admin
│   ├── templates/                # inicio.html, 404.html, base.html
│   ├── migrations/
├── sql/                         # Scripts SQL obligatorios
│   ├── 01_crear_base_datos.sql
│   ├── 02_crear_usuario.sql
│   └── 03_asignar_permisos.sql
├── manage.py
├── requirements.txt
├── .env.example                 # Plantilla de variables de entorno (.env NO se sube)
└── .gitignore
```

## Modelo de datos

| Entidad | Propósito |
|---|---|
| `Rol` | Perfiles de acceso (Administrador, Proveedor, etc.) |
| `Usuario` | Login del sistema, asociado a un `Rol` |
| `Proveedor` | Empresas que abastecen productos |
| `Cliente` | Destinatarios de salidas/ventas de stock |
| `Categoria` | Clasificación de productos |
| `Bodega` | Sucursales/ubicaciones físicas de almacenamiento |
| `Producto` | Catálogo de productos (SKU, precio, stock mínimo) |
| `Inventario` | Stock actual de un producto en una bodega |
| `TipoMovimiento` | Catálogo de movimientos (Entrada, Salida, Ajuste, Devolución) |
| `MovimientoInventario` | Histórico de cada movimiento de stock, con usuario, fecha y proveedor/cliente asociado |
| `Auditoria` | Registro general de acciones relevantes del sistema |

## Instalación y ejecución

1. Clonar el repositorio y ubicarse en la carpeta del proyecto:
   ```
   git clone <url-del-repositorio>
   cd IEI_N4_C1-main
   ```

2. Crear y activar el ambiente virtual:
   ```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Preparar la base de datos en MySQL ejecutando en orden los scripts de `sql/`:
   ```
   sql/01_crear_base_datos.sql
   sql/02_crear_usuario.sql
   sql/03_asignar_permisos.sql
   ```

5. Configurar las variables de entorno: copiar `.env.example` como `.env` y
   completar `SECRET_KEY`, `NAME`, `HOST`, `PORT`, `USER` y `PASSWORD` con los
   datos usados en los scripts SQL del paso anterior.

6. Generar y aplicar las migraciones:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Crear un usuario administrador (opcional, para el panel `/admin/`):
   ```
   python manage.py createsuperuser
   ```

8. Levantar el servidor:
   ```
   python manage.py runserver
   ```

## Endpoints disponibles

Página de bienvenida: `http://127.0.0.1:8000/`
Panel de administración: `http://127.0.0.1:8000/admin/`

API REST (`http://127.0.0.1:8000/biblio_app/...`), cada uno con CRUD completo
(`GET`, `POST`, `PUT`, `PATCH`, `DELETE`):

| Endpoint | Recurso |
|---|---|
| `/biblio_app/roles/` | Roles |
| `/biblio_app/proveedores/` | Proveedores |
| `/biblio_app/clientes/` | Clientes |
| `/biblio_app/usuarios/` | Usuarios |
| `/biblio_app/categorias/` | Categorías |
| `/biblio_app/bodegas/` | Bodegas |
| `/biblio_app/productos/` | Productos |
| `/biblio_app/inventario/` | Stock por producto/bodega |
| `/biblio_app/tipos-movimiento/` | Tipos de movimiento |
| `/biblio_app/movimientos/` | Movimientos de inventario (histórico) |
| `/biblio_app/auditoria/` | Registro de auditoría |

## Notas técnicas

- `SECRET_KEY` y las credenciales de base de datos se leen con `python-decouple`
  desde `.env`, nunca quedan escritas en `settings.py`.
- `DATABASES` apunta a MySQL (`django.db.backends.mysql`), usando el usuario y
  base de datos creados por los scripts de `sql/`.
- `rest_framework` está agregado a `INSTALLED_APPS` para habilitar serializers,
  `ModelViewSet` y el `DefaultRouter`.
