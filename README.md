# Restaurante App - Semana 10

**Estudiante:** Ruth Arreaga Espinoza  
**Asignatura:** Programación Orientada a Objetos

## Descripción del Sistema

En esta semana continué trabajando sobre el proyecto que venía desarrollando, agregando una mejora muy importante: ahora los productos se guardan en un archivo JSON y se recuperan automáticamente cada vez que abro la aplicación. Esto significa que la información ya no se pierde al cerrar el programa, sino que se conserva de forma permanente, como corresponde a un sistema real. Seguí manteniendo la misma estructura modular, separando los modelos, los servicios y el punto de entrada, para que cada parte tenga una responsabilidad clara.

## Estructura del Proyecto

```
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

## Organización y responsabilidad de cada componente

En la carpeta modelos dejé las clases que representan la información. Producto ahora incluye además un método para convertirse en diccionario y otro para reconstruirse desde esos datos, de forma que pueda guardarse y leerse sin perder su naturaleza de objeto. Usuario se mantiene tal como estaba, ya que en esta versión no se solicitó guardarla.
En la carpeta servicios agregué archivo_servicio.py, que es quien se encarga exclusivamente de leer y escribir el archivo JSON. Así separo la lógica de guardado de la lógica del negocio, que sigue quedando en la clase Restaurante. De esta forma, si en el futuro cambia la manera de guardar, no tengo que modificar todo el sistema, solo el servicio correspondiente.
Por último, en main.py coordino todo: al iniciar el programa pido al servicio de archivos que cargue los productos guardados, se los entrego al restaurante para que trabaje normalmente con ellos, y cada vez que registro, actualizo o elimino algo, solicito que se guarde el cambio en el archivo JSON.
```
