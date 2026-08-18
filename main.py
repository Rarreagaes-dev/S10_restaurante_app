from modelos.producto import Producto
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio

def menu():
    print("\n--- SISTEMA DE RESTAURANTE (S10) ---")
    print("1. Registrar Producto")
    print("2. Listar Productos")
    print("3. Actualizar Producto")
    print("4. Eliminar Producto")
    print("5. Salir")
    return input("Seleccione una opción: ")

def main():
    servicio_restaurante = Restaurante()
    servicio_archivo = ArchivoServicio("datos/productos.json")

    # CARGA INICIAL
    productos_cargados = servicio_archivo.cargar_productos()
    servicio_restaurante.set_productos(productos_cargados)
    print(f"--- Sistema iniciado. Se cargaron {len(productos_cargados)} productos. ---")

    while True:
        opcion = menu()

        if opcion == "1":
            try:
                id_p = int(input("ID: "))
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                cat = input("Categoría: ")
                nuevo = Producto(id_p, nombre, precio, cat)
                if servicio_restaurante.registrar_producto(nuevo):
                    servicio_archivo.guardar_productos(servicio_restaurante.listar_productos())
                    print("Producto guardado exitosamente.")
            except ValueError as e:
                print(f"Error en los datos: {e}")

        elif opcion == "2":
            productos = servicio_restaurante.listar_productos()
            if not productos:
                print("No hay productos registrados.")
            for p in productos:
                print(p)

        elif opcion == "3":
            try:
                id_p = int(input("ID del producto a editar: "))
                nombre = input("Nuevo nombre: ")
                precio = float(input("Nuevo precio: "))
                cat = input("Nueva categoría: ")
                if servicio_restaurante.actualizar_producto(id_p, nombre, precio, cat):
                    servicio_archivo.guardar_productos(servicio_restaurante.listar_productos())
                    print("Producto actualizado.")
                else:
                    print("Producto no encontrado.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            try:
                id_p = int(input("ID del producto a eliminar: "))
                if servicio_restaurante.eliminar_producto(id_p):
                    servicio_archivo.guardar_productos(servicio_restaurante.listar_productos())
                    print("Producto eliminado.")
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()