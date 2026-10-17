acciones = []
 
def registrar_accion(descripcion):
    acciones.append(descripcion)
    print("Acción registrada:", descripcion)
 
def deshacer():
    if not acciones:
        print("No existen acciones para deshacer")
        return
    ultima = acciones.pop()
    print("Se deshizo:", ultima)
 
def historial():
    print("Acciones pendientes:", acciones)
 
registrar_accion("Escribir título")
registrar_accion("Agregar párrafo")
registrar_accion("Cambiar formato")
historial()
deshacer()
historial()

def menu():
    while True:
        print("=== Menú ===")
        print("1. Registrar Accion")
        print("2. Deshacer Accion")
        print("3. Historial de Acciones")
        print("4. Salir")
        opcion = int(input("Ingrese el # de opcion: "))
        if opcion == 1:
            while True:
                descripcion = input("Ingrese la descripcion de la accion: ")
                if descripcion != "":
                    registrar_accion(descripcion)
                    break
                else:
                    print("La descripcion no puede estar vacia.")
        elif opcion == 2:
            deshacer()
        elif opcion == 3:
            historial()
        elif opcion == 4:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida, seleccione una de las disponibles.")

menu()