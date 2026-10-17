from collections import deque
cola = deque()
siguiente_turno = 1

def registrar_turno(nombre):
    global siguiente_turno
    turno = siguiente_turno
    cliente = (turno, nombre)
    cola.append(cliente)
    siguiente_turno += 1
    print(f"Turno {turno} registrado para: {nombre}")

def atender_cliente():
    if not cola:
        print("No hay clientes en espera.")
    else:
        turno, nombre = cola.popleft()
        print(f"Atendiendo turno {turno}: {nombre}")

def consultar_proximo():
    if not cola:
        print("No hay clientes pendientes.")
    else:
        turno, nombre = cola[0]
        print(f"Proximo cliente: Turno {turno} - {nombre}")

def mostrar_cola():
    if not cola:
        print("La cola esta vacia.")
    else:
        print("Clientes en espera:")
        for turno, paciente in enumerate(cola, 1):
            print(f"{turno}. {paciente}")

def cantidad_pendientes():
    print(f"Clientes pendientes: {len(cola)}")


def menu():
    while True:
        print("=== Menú ===")
        print("1. Registrar turno")
        print("2. Atender siguiente cliente")
        print("3. Consultar proximo cliente")
        print("4. Mostrar clientes en espera")
        print("5. Mostrar cantidad de pendientes")
        print("6. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            while True:
                nombre = input("Ingrese el nombre del cliente: ")
                if nombre != "":
                    registrar_turno(nombre)
                    break
                else:
                    print("El nombre no puede estar vacio.")
        elif opcion == 2:
            atender_cliente()
        elif opcion == 3:
            consultar_proximo()
        elif opcion == 4:
            mostrar_cola()
        elif opcion == 5:
            cantidad_pendientes()
        elif opcion == 6:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida. Seleccione una opcion del 1 al 6.")

menu()