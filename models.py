from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    id: Optional[int]
    nombre: str
    categoria: str
    cantidad: int
    punto_reorden: int
    precio_unitario: float
    proveedor: str

class Pedido(BaseModel):
    id: Optional[int]
    restaurante_id: int
    mesa: str
    mesero: str
    items: list  # lista de dicts: {"producto_id": int, "cantidad": int}
