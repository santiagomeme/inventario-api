from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class Producto(BaseModel):
    id: Optional[int] = None  # Se genera automáticamente si no se incluye
    nombre: str
    categoria: str
    cantidad: int = Field(..., ge=0, description="Cantidad en inventario (≥ 0)")
    punto_reorden: int = Field(..., ge=0, description="Nivel mínimo antes de reordenar (≥ 0)")
    precio_unitario: float = Field(..., ge=0, description="Precio por unidad (≥ 0)")
    proveedor: str

class Pedido(BaseModel):
    id: Optional[int] = None
    restaurante_id: int
    mesa: str
    mesero: str
    items: List[Dict[str, int]]  # Ejemplo: [{"producto_id": 1, "cantidad": 2}]
