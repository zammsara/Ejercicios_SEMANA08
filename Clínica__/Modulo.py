# Importamos la librería colorama para hacer el programa más agradable visualmente
from colorama import init, Fore, Style
init(autoreset=True)


# Definimos la clase Nodo
class Nodo:
    def __init__(self, paciente):
        self.paciente = paciente
        self.siguiente = None
        
# Definimos la clase cola con sus respectivos método
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        
    # Método para agregar pacientes
    def Agregar(self, paciente):
        nuevo = Nodo(paciente) #creamos un nuevo Nodo
        if self.final is None:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
    
    def Eliminar(self):
        if self.frente is None:
            print(Fore.YELLOW+"\nNo hay paciente registrados\n") 
            return None
        
        pacienteEliminado = self.frente.paciente
        self.frente = self.frente.siguiente
        
        if self.frente is None: #si la cola queda vacía
            self.final = None
            
        print(Fore.YELLOW+f"\nPaciente '{pacienteEliminado}' atendido.\nRegistro actualizado.\n")
    
    # Método para mostrar la lista actual de pacientes en espera   
    def MostrarPacientes(self):
        if self.frente is None: #si la cola está vacía
            print(Fore.YELLOW+"\nNo hay pacientes por atender.\n")
        else:
            print(Fore.YELLOW+Style.BRIGHT+"\nPacientes por atender:")
            actual = self.frente 
            while actual is not None:
                print(actual.paciente)
                actual = actual.siguiente
        
            
        
    