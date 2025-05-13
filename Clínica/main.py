# Desarrolle un programa en Python que simule una cola de atención en una clínica. El sistema
# debe permitir agregar pacientes a la cola (registro de llegada), atender al siguiente paciente
# (eliminar el primero en la cola) y mostrar en pantalla la lista actual de pacientes en espera.

import Modulo
import os

cola = Modulo.Cola()

while True: 
    print("-" * 30)
    print("       MENU DE CLÍNICA")
    print("-" * 30)
    print("1. Agregar Paciente")
    print("2. Atender al Siguiente Paciente")
    print("3. Mostrar Pacientes en Espera")
    print("4. Salir")

    try:
        op = int(input("Opción: "))
    except ValueError:
        print("Opción inválida. Intente de nuevo.")
        continue

    match op:
        case 1:
            paciente = input("Nombre del paciente: ")
            cola.Agregar(paciente)
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
