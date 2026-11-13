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
