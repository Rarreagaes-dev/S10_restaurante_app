import json
import os
from modelos.producto import Producto

class ArchivoServicio:
    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo

    def guardar_productos(self, lista_productos: list[Producto]) -> None:
        try:
            # Convertimos la lista de objetos a lista de diccionarios
            datos_json = [p.to_dict() for p in lista_productos]
            
            # Asegurar que el directorio existe
            os.makedirs(os.path.dirname(self.ruta_archivo), exist_ok=True)
            
            with open(self.ruta_archivo, 'w', encoding='utf-8') as f:
                json.dump(datos_json, f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar: {e}")

    def cargar_productos(self) -> list[Producto]:
        productos_recuperados = []
        if not os.path.exists(self.ruta_archivo):
            return []

        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                for item in datos:
                    try:
                        productos_recuperados.append(Producto.from_dict(item))
                    except (KeyError, ValueError) as e:
                        print(f"Advertencia: Saltando registro corrupto. Detalle: {e}")
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: El archivo JSON está corrupto o tiene un formato inválido.")
        except PermissionError:
            print("Error: No se tienen permisos para leer el archivo.")
        
        return productos_recuperados