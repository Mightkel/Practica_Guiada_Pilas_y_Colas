from collections import deque
 
cola = deque()
 
def registrar_paciente(nombre):
    cola.append(nombre)
    print(f"Registrado: {nombre}")
 
def atender_paciente():
    if not cola:
        print("No hay pacientes en espera")
    else:
        paciente = cola.popleft()
        print(f"Atendiendo a: {paciente}")
 
def mostrar_cola():
    if not cola:
        print("La cola está vacía")
    else:
        print("Pacientes en espera:")
        for posicion, paciente in enumerate(cola, 1):
            print(f"{posicion}. {paciente}")
 
registrar_paciente("Ana")
registrar_paciente("Luis")
registrar_paciente("María")
mostrar_cola()
atender_paciente()
mostrar_cola()

def menu():
    while True:
        print("=== Menú ===")
        print("1. Registrar paciente")
        print("2. Atender paciente")
        print("3. Pacientes en espera")
        print("4. Salir")
        opcion = int(input("Ingrese el # de opcion: "))
        if opcion == 1:
            while True:
                nombre = input("Ingrese la descripcion de la accion: ")
                if nombre != "":
                    registrar_paciente(nombre)
                    break
                else:
                    print("El nombre no puede estar vacio.")
        elif opcion == 2:
            atender_paciente()
        elif opcion == 3:
            mostrar_cola()
        elif opcion == 4:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida, seleccione una opcion disponible")
            
menu()