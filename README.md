# Proyecto Final Django Blog

Aplicación web estilo blog desarrollada en Python con Django.

## Apps
- blog: páginas, listado, detalle, creación, edición y borrado
- accounts: registro, login, logout, perfil, edición de perfil y cambio de contraseña
- messaging: mensajería entre usuarios

## Funcionalidades
- Home
- About (`/about/`)
- Pages (`/pages/`)
- Detalle de páginas con “Leer más”
- CRUD de páginas
- Login, logout y signup
- Perfil de usuario
- Edición de perfil y cambio de contraseña
- Mensajería
- Panel admin

## Requisitos
- Python
- Django
- dependencias listadas en `requirements.txt`

## Cómo correr el proyecto
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
