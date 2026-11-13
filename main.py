"""Inventario de red — Práctica 3.

Alumno:    Elizabeth
Matrícula: 125054627
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Inventario de red")


class Dispositivo(BaseModel):
    nombre: str
    tipo: str
    ip: str
    activo: bool = True


inventario = [
    Dispositivo(nombre="R1", tipo="router", ip="10.0.0.1"),
    Dispositivo(nombre="SW1", tipo="switch", ip="10.0.0.10",
                activo=False),
    Dispositivo(nombre="FW1", tipo="firewall", ip="10.0.0.254"),
]


@app.get("/")
async def estado():
    """Comprueba que el servicio responde."""
    return {"servicio": "Inventario de red", "total": len(inventario)}


@app.get("/dispositivos")
async def listar(activo: bool | None = None):
    """Lista el inventario. Con ?activo=true filtra los que están en línea."""
    if activo is None:
        return inventario
    return [equipo for equipo in inventario if equipo.activo == activo]


@app.get("/dispositivos/{nombre}")
async def obtener(nombre: str):
    """Busca un equipo por su nombre."""
    for equipo in inventario:
        if equipo.nombre.upper() == nombre.upper():
            return equipo
    raise HTTPException(status_code=404,
                        detail=f"No existe el equipo {nombre}")
