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
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Bienvenido al Call Center" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "1. Agregar llamada" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "2. Mostrar lista de llamadas" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "3. Buscar llamada" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "4. Atender llamada" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "5. Salir" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "-----------------------------------------" + Style.RESET_ALL)
    



# Inicializar colorama (necesario para Windows)
init(autoreset=True)

def pausa():
    print(Fore.LIGHTBLACK_EX + Style.DIM + "Presione Enter para continuar...")  # Gris y tenue
    input()