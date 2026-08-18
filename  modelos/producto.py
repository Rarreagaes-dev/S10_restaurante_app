class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float, categoria: str):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor

    def to_dict(self) -> dict:
        """Convierte el objeto Producto a un diccionario para JSON."""
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }

    @staticmethod
    def from_dict(datos: dict) -> 'Producto':
        """Crea un objeto Producto a partir de un diccionario."""
        return Producto(
            id_producto=datos["id_producto"],
            nombre=datos["nombre"],
            precio=datos["precio"],
            categoria=datos["categoria"]
        )

    def __str__(self) -> str:
        return f"[{self.id_producto}] {self.nombre} ({self.categoria}) - ${self.precio:.2f}"