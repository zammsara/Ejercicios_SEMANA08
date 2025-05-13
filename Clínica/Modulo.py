class Nodo:
    def __init__(self, paciente):
        self.paciente = paciente
        self.siguiente = None

class Cola: 
    def __init__(self):
        self.frente = None
        self.final = None

    def Agregar(self, paciente):
        nuevo = Nodo(paciente)
        if self.final is None:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo 
            self.final = nuevo
        print(f"Paciente '{paciente}' agregado.")

    def Eliminar(self):
        if self.frente is None: 
            print("No hay pacientes.")
            return None
        
        eliminado = self.frente.paciente
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None
        print(f"Paciente '{eliminado}' atendido.")
        return eliminado

    def Mostrar(self):
        if self.frente is None:
            print("No hay pacientes.")
        else:
            print("Pacientes en espera:")
            actual = self.frente
            while actual is not None:
                print(f"- {actual.paciente}")
                actual = actual.siguiente