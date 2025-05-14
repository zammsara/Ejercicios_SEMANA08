class Nodo:
    def __init__(self, paciente):
        self.paciente = paciente  # Guarda el nombre del paciente
        self.siguiente = None     # Apunta al siguiente nodo (paciente)
   

class Cola: 
    def __init__(self):
        self.frente = None  # Primer paciente en la cola
        self.final = None   # Último paciente en la cola

    def Agregar(self, paciente):
        nuevo = Nodo(paciente)            # Crear nodo con el paciente
        if self.final is None:            # Si la cola está vacía
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo  # Enlazar al final actual
            self.final = nuevo            # Actualizar puntero final
        print(f"Paciente '{paciente}' agregado.")

    def Eliminar(self):
        if self.frente is None:
            print("No hay pacientes.")    # Cola vacía
            return None

        eliminado = self.frente.paciente  # Guardar paciente para mostrar
        self.frente = self.frente.siguiente  # Mover al siguiente

        if self.frente is None:
            self.final = None             # Si la cola queda vacía
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