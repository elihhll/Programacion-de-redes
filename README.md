# Inventario de red

API sencilla hecha con FastAPI para consultar un inventario de dispositivos de red
(routers, switches y firewalls). Práctica 3 de Programación de Redes, UPQ.

- **Alumno:** Elizabeth
- **Matrícula:** 125054627

## Instalación

```bash
git clone https://github.com/elihhll/Programacion-de-redes.git
cd Programacion-de-redes

python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
```

## Ejecución

```bash
fastapi dev main.py
```

El servicio queda en http://127.0.0.1:8000 y la documentación interactiva en
http://127.0.0.1:8000/docs.

## Rutas de la API

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Comprueba que el servicio responde y muestra el total de equipos. |
| GET | `/dispositivos` | Lista el inventario. Con `?activo=true` o `?activo=false` filtra por estado. |
| GET | `/dispositivos/{nombre}` | Busca un equipo por nombre (sin distinguir mayúsculas). Responde 404 si no existe. |
