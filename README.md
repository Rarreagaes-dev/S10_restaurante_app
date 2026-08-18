# Restaurante App - Semana 10

**Estudiante:** Ruth Arreaga Espinoza  
**Asignatura:** Programación Orientada a Objetos

## Descripción del Sistema

En esta semana continué trabajando sobre el proyecto que venía desarrollando, agregando una mejora muy importante: ahora los productos se guardan en un archivo JSON y se recuperan automáticamente cada vez que abro la aplicación. Esto significa que la información ya no se pierde al cerrar el programa, sino que se conserva de forma permanente, como corresponde a un sistema real. Seguí manteniendo la misma estructura modular, separando los modelos, los servicios y el punto de entrada, para que cada parte tenga una responsabilidad clara.

## Estructura del Proyecto
```text
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

## Organización y responsabilidad de cada componente

En la carpeta modelos dejé las clases que representan la información. Producto ahora incluye además un método para convertirse en diccionario y otro para reconstruirse desde esos datos, de forma que pueda guardarse y leerse sin perder su naturaleza de objeto. Usuario se mantiene tal como estaba, ya que en esta versión no se solicitó guardarla.
En la carpeta servicios agregué archivo_servicio.py, que es quien se encarga exclusivamente de leer y escribir el archivo JSON. Así separo la lógica de guardado de la lógica del negocio, que sigue quedando en la clase Restaurante. De esta forma, si en el futuro cambia la manera de guardar, no tengo que modificar todo el sistema, solo el servicio correspondiente.
Por último, en main.py coordino todo: al iniciar el programa pido al servicio de archivos que cargue los productos guardados, se los entrego al restaurante para que trabaje normalmente con ellos, y cada vez que registro, actualizo o elimino algo, solicito que se guarde el cambio en el archivo JSON.

Persistencia en formato JSON
El sistema funciona de la siguiente manera: al iniciar, lee el archivo datos/productos.json, convierte cada registro en un objeto Producto y lo carga en memoria. Cuando realizo alguna modificación, la lista de productos se transforma en diccionarios y se escribe nuevamente en el archivo utilizando json.dump(), manteniendo siempre la información actualizada.
Manejo de Excepciones
Implementé el manejo de excepciones para asegurar la robustez del sistema:
FileNotFoundError: Si el archivo todavía no existe, el sistema inicia normalmente con una lista vacía.
json.JSONDecodeError: Si el archivo está dañado o tiene un formato incorrecto, el programa informa el error y permite continuar.
PermissionError: Se controla en caso de que el sistema operativo no permita leer o escribir en la carpeta de datos.
KeyError/ValueError: Se manejan al reconstruir objetos para evitar que registros incompletos detengan la aplicación.

## Cómo comprobé que funciona la persistencia

Realicé las siguientes pruebas:
1. Registro y Cierre:
 Registré un producto, verifiqué que apareciera en el JSON, cerré el programa y al abrirlo de nuevo el producto seguía ahí.

2. Actualización y Eliminación:
 Modifiqué un precio y eliminé un producto existente; al reiniciar la aplicación, los cambios persistían correctamente.

3. Archivo Inexistente:
 Borré el archivo productos.json e inicié el programa; verifiqué que el sistema no falló y creó el archivo automáticamente al realizar el primer registro.

## Ejecución
Para poner en marcha el programa solo necesitas tener Python 3 instalado. Debes ubicarte en la carpeta raíz del proyecto y escribir en la terminal:

```text
python main.py
```

## Reflexión
Esta versión me ayudó a comprender la importancia de separar las responsabilidades dentro de un sistema. Al tener un servicio dedicado exclusivamente al manejo del archivo, el código queda mucho más ordenado y fácil de mantener. Además, aprendí que trabajar con persistencia no significa guardar directamente objetos en memoria, sino convertirlos a un formato que pueda almacenarse y luego reconstruirlos cuando se necesiten. También entendí por qué es tan importante controlar las excepciones de forma específica para que una aplicación esté preparada para situaciones del mundo real sin dejar de funcionar.
