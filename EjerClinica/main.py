# Desarrollado por: Aguilera Franco, Estrada Alicia, Duarte Andrea, Sanchez David, Zambrana Sara
# Clinica || Versión 1.0
# 13.mayo.2025

#Descripción del programa: 
# Este programa simula una clínica donde se pueden agregar pacientes a una cola de espera, 
# buscar pacientes por nombre, eliminar pacientes de la cola y mostrar la lista de pacientes en espera.

from mod_cola import Cola
from mod_cola import Paciente
import mod_menu as menu
from colorama import Fore, Style, init

respuesta = 0
cola = Cola()

while respuesta != 5:
    menu.mostrar_menu()
    respuesta = int(input(Fore.LIGHTBLACK_EX + Style.DIM + "Seleccione una opción: "+Style.RESET_ALL)) 
    match respuesta:
        case 1:
            nombre = input("\nIngrese el nombre del paciente: ").upper()
            #Verificamos que ingresen una edad valida
            try:
                edad = int(input("Ingrese la edad del paciente: "))
                if edad < 0 or edad > 120:
                    print(Fore.LIGHTRED_EX + Style.BRIGHT + "Error: La edad debe ser un número entero entre 0 y 120." + Style.RESET_ALL)
                    menu.pausa()
                    continue
            except ValueError:
                print(Fore.LIGHTRED_EX + Style.BRIGHT + "Error: La edad debe ser un número entero."+ Style.RESET_ALL)
                menu.pausa()
                continue
            
            #pedimos los datos del paciente y lo insertamos en la cola
            enfermedad = input("Ingrese la enfermedad del paciente: ")
            paciente = Paciente(nombre, edad, enfermedad)
            cola.Insertar(paciente)
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Paciente agregado con éxito."+ Style.RESET_ALL)
            menu.pausa()
            
        case 2:
            #Imprimimos la lista de pacientes
            cola.Imprimir()
            menu.pausa()
        case 3:
            #Buscamos un paciente por nombre
            nombre_buscar = input("\nIngrese el nombre del paciente a buscar: ")
            encontrado = cola.Buscar(nombre_buscar.upper())#lo pasamos a mayusculas para que no haya problemas con la busqueda
            if encontrado is not None:#si devolvio algo, significa que lo encontro
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"Paciente encontrado: \n{encontrado}"+ Style.RESET_ALL)
                menu.pausa()
            else:
                print(Fore.LIGHTRED_EX + Style.BRIGHT + "Paciente no encontrado."+ Style.RESET_ALL)
                menu.pausa()

        case 4:
            #Eliminamos al primer paciente que habiamos ingresado *(FIFO)*
            eliminado = cola.Eliminar()
            if eliminado is not None:
                print(Fore.LIGHTRED_EX + Style.BRIGHT + f"Paciente que paso a consulta: {eliminado}"+ Style.RESET_ALL)
                menu.pausa()
            else:
                print(Fore.LIGHTRED_EX + Style.BRIGHT + "No hay pacientes en la cola."+ Style.RESET_ALL)
                menu.pausa()
        case 5:
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Saliendo..."+ Style.RESET_ALL)
            menu.pausa()
        case _:
            print(Fore.LIGHTRED_EX + Style.BRIGHT + "Opción no válida. Intente de nuevo."+ Style.RESET_ALL)
            menu.pausa()
