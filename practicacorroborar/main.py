
import modulos
import os

cola = modulos.Cola()

while True: 
    print("-" * 30)
    print("       CENTRO DE ATENCION AL CLIENTE    ")
    print("-" * 30)
    print("1. Agregar Cliente")
    print("2. Atender al Siguiente Cliente")
    print("3. Mostrar Clientes en Espera")
    print("4. Salir")

    try:
        op = int(input("Opción: "))
    except ValueError:
        print("Opción inválida. Intente de nuevo.")
        continue

    match op:
        case 1:
            cliente = input("Nombre del cliente: ")
            descripcion = input(" Descripcion del cliente: ")
            cola.Agregar(cliente,descripcion )
        case 2:
            cola.Eliminar()  
        case 3:
            cola.Mostrar()
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Opción no válida.")

    input("\nPresione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
