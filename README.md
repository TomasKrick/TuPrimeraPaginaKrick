# Proyecto Final Django

Aplicación web estilo blog desarrollada con Django.

## Apps del proyecto

- `blog`: gestión de páginas, listado, detalle, creación, edición y borrado
- `accounts`: registro, login, logout, perfil, edición de perfil y cambio de contraseña
- `messaging`: envío y visualización de mensajes entre usuarios

## Funcionalidades

- Home
- About
- Pages
- Detalle de páginas con “Leer más”
- Crear, editar y borrar páginas
- Signup, login y logout
- Perfil de usuario
- Edición de perfil
- Cambio de contraseña
- Mensajería entre usuarios
- Panel de administración de Django

## Requisitos

- Python 3.x
- Django
- Dependencias listadas en `requirements.txt`

## Cómo correr el proyecto

1. Clonar el repositorio
2. Crear y activar entorno virtual
3. Instalar dependencias
4. Aplicar migraciones
5. Levantar servidor

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
