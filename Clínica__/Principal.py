# Programa "Clínica - Registro" desarrolado por: - Andrea Duarte, - Sara Zambrana, - Alicia Estrada, - Franco Aguilera, - David Sánchez
# Versión 1.1
# Fecha: 13.mayo.2025

# Descripción del programa solicitado:
# Desarrolle un programa en Python que simule una cola de atención en una clínica. El sistema
# debe permitir agregar pacientes a la cola (registro de llegada), atender al siguiente paciente
# (eliminar el primero en la cola) y mostrar en pantalla la lista actual de pacientes en espera.

# Importamos el módulo
import Modulo
cola = Modulo.Cola() # Incializamos la cola vacía

# Importamos la librería colorama para hacer el programa más agradable visualmente
from colorama import init, Fore, Style
init(autoreset=True)

# Librería que utilizaremos en el método "clear" para limpiar pantalla
import os

# Método para limpiar pantalla
def clear():
    # Limpiar la consola
    os.system('clear') 
    os.system('cls')
    

while True:
    print('='*35)
    print("\tClínica - Registro")
    print('='*35)
    print("1. Registrar llegada de paciente")
    print("2. Atender siguiente paciente")
    print("3. Mostrar pacientes en espera")
    print("4. Salir")
    print('='*35)
    
    try:
            opc = int(input("Seleccione una opción: "))
    except ValueError:
            print(Fore.RED+"Ingrese un número válido.\n")
            continue
        
    match opc:
        case 1:
            clear()
            print(Style.BRIGHT+"\tRegistro de llegada de paciente")
            nombre = input("\nIngrese el nombre del paciene: ")
            apellido = input("Ingrese el apellido del paciente: ")
            
            paciente = f"{nombre} {apellido}"
            cola.Agregar(paciente)
            print(Fore.GREEN+f"Llegada del paciente '{paciente}' registrada correctamente\n")
        
        case 2:
            clear()
            cola.Eliminar()
        
        case 3:
            clear()
            cola.MostrarPacientes()
        
        case 4: 
            clear()
            print(Fore.CYAN+Style.BRIGHT+"Saliendo del Registro...")
            break
        
        case _:
            print(Fore.RED+"Opción inválida\n")
