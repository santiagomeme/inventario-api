from fastapi import APIRouter, HTTPException
from models import Producto, Pedido
from database import get_db

router = APIRouter()

@router.get("/productos")
def listar_productos():
    db = get_db()
    productos = db.execute("SELECT * FROM productos").fetchall()
    return [dict(p) for p in productos]

@router.post("/productos")
def crear_producto(p: Producto):
    db = get_db()
    db.execute("""
        INSERT INTO productos (nombre, categoria, cantidad, punto_reorden, precio_unitario, proveedor)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (p.nombre, p.categoria, p.cantidad, p.punto_reorden, p.precio_unitario, p.proveedor))
    db.commit()
    return {"mensaje": "Producto creado"}

@router.post("/pedidos")
def crear_pedido(p: Pedido):
    db = get_db()
    db.execute("""
        INSERT INTO pedidos (restaurante_id, mesa, mesero)
        VALUES (?, ?, ?)
    """, (p.restaurante_id, p.mesa, p.mesero))
    pedido_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
    for item in p.items:
        db.execute("""
            INSERT INTO pedido_items (pedido_id, producto_id, cantidad)
            VALUES (?, ?, ?)
        """, (pedido_id, item["producto_id"], item["cantidad"]))
        db.execute("""
            UPDATE productos SET cantidad = cantidad - ?
            WHERE id = ?
        """, (item["cantidad"], item["producto_id"]))
    db.commit()
    return {"mensaje": "Pedido creado", "pedido_id": pedido_id}
