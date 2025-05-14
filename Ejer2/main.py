# Desarrollado por: Aguilera Franco, Estrada Alicia, Duarte Andrea, Sanchez David, Zambrana Sara
# CALL CENTER || Versión 1.0
# 14.mayo.2025

#Descripción del programa: 
# Registro de llamadas
#Agente call center responde

from mod_cola import Cola
from mod_cola import Caller
import mod_menu as menu
from colorama import Fore, Style, init

respuesta = 0
cola = Cola()

while respuesta != 5:
    menu.mostrar_menu()
    #Verificamos que ingresen un numero entero
    try:
        respuesta = int(input(Fore.LIGHTBLACK_EX + Style.DIM + "Seleccione una opción: "+Style.RESET_ALL))
    except ValueError:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Error: Debe ingresar un número entero." + Style.RESET_ALL)
        menu.pausa()
        continue
    match respuesta:
        # Agregar llamada
        case 1:
            nombre = input("\nIngrese el nombre del cliente: ").upper().strip()
            # Verificamos que el nombre no esté vacío
            if not nombre.strip():
                print(Fore.LIGHTRED_EX + Style.BRIGHT + "Error: El nombre del cliente no puede estar vacío." + Style.RESET_ALL)
                menu.pausa()
                continue
            motivo = input("Ingrese el motivo de la llamada: ")
            # Verificamos que el motivo no esté vacío
            if not motivo.strip():
                print(Fore.LIGHTRED_EX + Style.BRIGHT + "Error: El motivo de la llamada no puede estar vacío." + Style.RESET_ALL)
                menu.pausa()
                continue
            #insertamos el que llamo en la cola
            cliente = Caller(nombre, motivo)
            cola.Insertar(cliente)
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Llamada registrada con éxito." + Style.RESET_ALL)
            menu.pausa()
        case 2:
            # Imprimimos la lista de llamadas
            cola.Imprimir()
            menu.pausa()
        case 3:
            # Buscamos una llamada por nombre
            nombre_buscar = input("\nIngrese el nombre del cliente a buscar: ")
            encontrado = cola.Buscar(nombre_buscar.upper())  # lo pasamos a mayusculas para que no haya problemas con la busqueda
            if encontrado is not None:  # si devolvio algo, significa que lo encontro
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"Llamada encontrada: \n{encontrado}" + Style.RESET_ALL)
                menu.pausa()
            else:
                print(Fore.LIGHTRED_EX + Style.BRIGHT + "Llamada no encontrada." + Style.RESET_ALL)
                menu.pausa()
        case 4:
            # Eliminamos la primera llamada que habiamos ingresado *(FIFO)*
            eliminado = cola.Eliminar()
            if eliminado is not None:
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"Atendiendo llamada de: \n{eliminado}" + Style.RESET_ALL)
                menu.pausa()
            else:
                print(Fore.LIGHTRED_EX + Style.BRIGHT + "No hay llamadas para atender." + Style.RESET_ALL)
                menu.pausa()
        # Salir del programa
        case 5:
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Saliendo del programa..." + Style.RESET_ALL)
            menu.pausa()
        case _:
            print(Fore.LIGHTRED_EX + Style.BRIGHT + "Opción no válida. Intente nuevamente." + Style.RESET_ALL)
            menu.pausa()
            
