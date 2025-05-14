#Ejercicio #2: Gestión de llamadas en un centro de atención al cliente
#Cree un sistema que simule la atención de llamadas en un Call Center. Cada llamada debe 
#ingresar a una cola con datos como el nombre del cliente y el motivo de la llamada. A medida 
#que los agentes estén disponibles, se debe atender al siguiente cliente en orden de llegada

import modulos
import os

cola = modulos.ColaLlamadas() # Inicializa la cola de llamadas

def limpiar_pantalla():
    """Limpia la pantalla de la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
    #pausa
    

limpiar_pantalla()



# Menú y gestionar las opciones
while True:
    print("=" * 30)
    print("=== MENÚ - Centro de Atención al Cliente ===")
    print("1. Registrar nueva llamada")
    print("2. Atender siguiente llamada")
    print("3. Ver cola de llamadas")
    print("4. Salir")
    print("=" * 30)

    opcion = int(input("Seleccione una opción: "))
    
    match opcion: 
        case 1: 
            nombre = input("Nombre del cliente: ")
            motivo = input("Motivo de la llamada: ")
            llamada = modulos.LlamadaCliente(nombre, motivo)
            cola.insertar(llamada)
            input("Llamada registrada. Presione Enter para continuar...")
            limpiar_pantalla()
            
        case 2:
            cola.eliminar()
            input("Presione Enter para continuar...")
            limpiar_pantalla()
        case 3:
            cola.imprimir()
            input("Presione Enter para continuar...")
            limpiar_pantalla()
        case 4:
            print("Saliendo del sistema...")
            limpiar_pantalla()
            break
        case _:
            print("Opción inválida. Intente nuevamente.\n")
            input("Presione Enter para continuar...")
            limpiar_pantalla()
            

    
