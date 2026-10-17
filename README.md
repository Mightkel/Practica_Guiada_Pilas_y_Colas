# Práctica Guiada: Retos de Pilas y Colas

**Asignatura:** Programación Estructurada
**Equipo:** 2
**Institución:** Universidad Americana (UAM)

## Integrantes

- Maykel Josue Cruz Zamora
- Jose Alfredo Baca Moreno
- Justin Leandro Ruiz Madrigal
- Humberto Rene Ruiz Rodriguez

## Descripción del proyecto

Este repositorio contiene los ejercicios y retos prácticos de estructuras de datos desarrollados en Python. El objetivo es comprender el funcionamiento de las pilas y las colas mediante programas que permiten registrar, consultar, agregar y retirar elementos, aplicando sus reglas de organización.

Los códigos fuente se encuentran en sus respectivos archivos `.py`.

## Programas desarrollados

### Parte A. Análisis del funcionamiento de una pila

Se analiza el comportamiento de una pila, identificando qué elemento se retira primero mediante `pop()` y qué sucede cuando se intenta retirar un elemento de una pila vacía.

¿Qué libro se retira primero? 

Base de datos.

¿Por qué? 

`Pop()` elimina el ultimo elemento de un arreglo, en este caso, el ultimo libro de la pila.

¿Qué sucede cuando se intenta retirar de una pila vacía?

Salta `IndexError`, en este caso, la condicional lo permite y retorna que la pila esta vacía.

### Parte B. Reto 1: Sistema de almacenamiento de cajas

Implementa una pila para administrar cajas identificadas mediante códigos únicos.

**Funciones principales:**

- Apilar cajas nuevas.
- Rechazar códigos vacíos o duplicados.
- Retirar la caja ubicada en el tope.
- Consultar la caja del tope.
- Mostrar las cajas almacenadas.
- Evitar errores cuando la pila está vacía.

### Parte C. Historial de acciones

Simula un sistema para registrar acciones y deshacer la última operación realizada.

**Funciones principales:**

- Registrar acciones.
- Deshacer la última acción.
- Consultar el historial de acciones pendientes.
- Validar que la descripción de una acción no esté vacía.

Este ejercicio demuestra cómo una pila permite implementar operaciones de deshacer mediante el principio LIFO.

### Parte D. Reto 2: Simulador de navegación web

Simula el funcionamiento del historial de navegación de un navegador.

**Funciones principales:**

- Registrar una página web nueva.
- Regresar a la página anterior.
- Consultar la página actual.
- Mostrar el historial de retroceso.
- Indicar la cantidad de páginas anteriores disponibles.

El programa utiliza una pila para almacenar las páginas anteriores y recuperar la última página guardada al regresar.

En este programa, `append()` logra añadir la pagina web a la pila `historial`, mientras que `pop()`, deshace el ultimo `append()` y nos muestra la pagina web (elemento) retirado de `historial`, así mismo, nos hace regresar a la pagina anterior y lo almacena en la variable `pagina_actual`, la que nos informa la ultima pagina ingresada con `append()` o la pagina a la que regresamos con `pop()`.

### Parte E. Cola de pacientes

Implementa una cola utilizando `collections.deque` para organizar la atención de pacientes.

**Funciones principales:**

- Registrar pacientes.
- Atender al siguiente paciente.
- Mostrar los pacientes en espera.
- Manejar correctamente la cola vacía.

Este ejercicio aplica el principio FIFO, donde el primer paciente registrado es el primero en ser atendido.

También se analiza la diferencia entre `pop()` y `popleft()`, destacando cómo cada operación permite retirar elementos siguiendo un orden distinto.

Diferencias entre `pop()` y `popleft()`:

`pop()` elimina siempre el ultimo elemento de una lista, haciendo que funcione como una pila, mientras que `popleft()` elimina el primer elemento, haciento que funcione como una cola.

Si en este caso se utilizara una pila en lugar de una cola, la lista de atención se acumularía en los primeros pacientes ingresados, y en lugar de dar atención a estos, se atenderían a los recién ingresados y los primeros nunca serian atendidos, creando un cuello de botella cuando el sistema sea utilizado regularmente.


### Parte F. Reto 3: Sistema de turnos para clientes

Desarrolla un sistema de turnos para organizar la atención de los clientes de una empresa mediante `collections.deque`.

**Funciones principales:**

- Registrar clientes con un número de turno consecutivo.
- Atender al siguiente cliente según el orden de llegada.
- Consultar al próximo cliente sin retirarlo de la cola.
- Mostrar todos los clientes en espera.
- Consultar la cantidad de turnos pendientes.
- Rechazar nombres vacíos.
- Manejar la cola vacía sin generar errores.
- Mostrar un menú interactivo hasta seleccionar la opción de salir.

## Conceptos fundamentales

### LIFO (Last In, First Out)

Significa «último en entrar, primero en salir». El último elemento agregado es el primero que se retira.

Se aplica en los programas de pilas, como el almacenamiento de cajas, el historial de acciones y la navegación web.

**Ejemplo:** si se agregan A, B y C, el primer elemento retirado será C.

### FIFO (First In, First Out)

Significa «primero en entrar, primero en salir». El primer elemento agregado es el primero que se retira.

Se aplica en la cola de pacientes y en el sistema de turnos para clientes.

**Ejemplo:** si se registran A, B y C, el primer elemento atendido será A.

### Diferencia entre las operaciones

| Operación   | Funcionamiento                                  |
| ----------- | ----------------------------------------------- |
| `append()`  | Agrega un elemento al final.                    |
| `pop()`     | Retira el último elemento de una lista o deque. |
| `popleft()` | Retira el primer elemento de un deque.          |
| `cola[0]`   | Consulta el primer elemento sin retirarlo.      |
| `len(cola)` | Devuelve la cantidad de elementos pendientes.   |

## Requisitos

- Python 3 instalado.
- Editor de código compatible con Python, como Visual Studio Code.
- Archivos `.py` incluidos en el repositorio.

La biblioteca `collections`, utilizada en los ejercicios de colas, forma parte de Python y no requiere una instalación adicional.

## Instrucciones de ejecución

1. Clonar o descargar el repositorio.
2. Abrir la carpeta del proyecto en el editor de código.
3. Abrir una terminal dentro de esa carpeta.
4. Ejecutar el archivo correspondiente al ejercicio que se desea probar.

Comando general:

```bash
python nombre_del_archivo.py
```

En Windows también puede utilizarse:

```bash
py nombre_del_archivo.py
```

**Nota:** reemplazar `nombre_del_archivo.py` por el nombre real del archivo que se desea ejecutar. Cada ejercicio debe ejecutarse de acuerdo con su implementación.

## Conclusión

La práctica permitió aplicar estructuras de datos fundamentales en Python mediante situaciones prácticas. Las pilas facilitan operaciones donde el último elemento agregado debe procesarse primero, mientras que las colas permiten organizar la atención según el orden de llegada. El uso de estas estructuras ayuda a desarrollar soluciones ordenadas y a comprender mejor la administración de datos en programas interactivos.
