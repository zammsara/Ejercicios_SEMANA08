#Ejercicio #2: Gestión de llamadas en un centro de atención al cliente
#Cree un sistema que simule la atención de llamadas en un Call Center. Cada llamada debe 
#ingresar a una cola con datos como el nombre del cliente y el motivo de la llamada. A medida 
#que los agentes estén disponibles, se debe atender al siguiente cliente en orden de llegada

import modulos

cola = modulos.ColaLlamadas()

while True:
    print("=" * 30)
    print("=== MENÚ - Centro de Atención al Cliente ===")
    print("1. Registrar nueva llamada")
    print("2. Atender siguiente llamada")
    print("3. Ver cola de llamadas")
    print("4. Salir")
    print("=" * 30)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del cliente: ")
        motivo = input("Motivo de la llamada: ")
        llamada = modulos.LlamadaCliente(nombre, motivo)
        cola.insertar(llamada)

    elif opcion == "2":
        cola.eliminar()

    elif opcion == "3":
        cola.imprimir()

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida. Intente nuevamente.\n")
