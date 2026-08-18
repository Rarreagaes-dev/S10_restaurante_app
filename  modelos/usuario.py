class Usuario:
    def __init__(self, username: str, rol: str):
        self.username = username
        self.rol = rol

    def __str__(self) -> str:
        return f"Usuario: {self.username} | Rol: {self.rol}"