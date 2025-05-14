import os
from colorama import Fore, Style, init

def limpiar_consola():
    # Detecta el sistema operativo y ejecuta el comando correspondiente
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # MacOS y Linux
        os.system('clear')

def mostrar_menu():
    limpiar_consola()  # Limpia la consola antes de mostrar el menú
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Bienvenido a la Clínica")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "1. Agregar Paciente")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "2. Mostrar Pacientes en espera")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "3. Buscar Paciente")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "4. Pasar a Paciente")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "5. Salir")
    



# Inicializar colorama (necesario para Windows)
init(autoreset=True)

def pausa():
    print(Fore.LIGHTBLACK_EX + Style.DIM + "Presione Enter para continuar...")  # Gris y tenue
    input()