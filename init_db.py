import sqlite3

conn = sqlite3.connect("inventario.db")
cursor = conn.cursor()

# Crear tabla productos
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    punto_reorden INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    proveedor TEXT NOT NULL
)
""")

# Crear tabla pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurante_id INTEGER NOT NULL,
    mesa TEXT NOT NULL,
    mesero TEXT NOT NULL
)
""")

# Crear tabla pedido_items
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedido_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
)
""")

conn.commit()
conn.close()

print("Base de datos inicializada correctamente.")
