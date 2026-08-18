from modelos.producto import Producto

class Restaurante:
    def __init__(self):
        self.productos: list[Producto] = []

    def set_productos(self, productos: list[Producto]):
        self.productos = productos

    def registrar_producto(self, producto: Producto) -> bool:
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: Ya existe un producto con ese ID.")
            return False
        self.productos.append(producto)
        return True

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def buscar_producto(self, id_producto: int) -> Producto | None:
        for p in self.productos:
            if p.id_producto == id_producto:
                return p
        return None

    def actualizar_producto(self, id_producto: int, nombre: str, precio: float, categoria: str) -> bool:
        producto = self.buscar_producto(id_producto)
        if producto:
            producto.nombre = nombre
            producto.precio = precio
            producto.categoria = categoria
            return True
        return False

    def eliminar_producto(self, id_producto: int) -> bool:
        producto = self.buscar_producto(id_producto)
        if producto:
            self.productos.remove(producto)
            return True
        return False