class Nodo:
    def __init__(self, cliente, descripcion):
        self.cliente = cliente
        self.descripcion = descripcion
        self.siguiente = None

class Cola: 
    def __init__(self):
        self.frente = None
        self.final = None

    def Agregar(self, cliente, descripcion):
        nuevo = Nodo(cliente, descripcion)
        if self.final is None:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo 
            self.final = nuevo
        print(f"Paciente '{cliente}', Descriocion '{descripcion}' agregado.")

    def Eliminar(self):
        if self.frente is None: 
            print("No hay clientes.")
            return None
        
        eliminado = self.frente.cliente 
        eliminado2 = self.frente.descripcion
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None
        print(f"Cliente '{eliminado}', Descripcion '{eliminado2}' atendido.")
        return eliminado, eliminado2
       
    
    
    

    def Mostrar(self):
        if self.frente is None:
            print("No hay clientes.")
        else:
            print("Clientes en espera:")
            actual = self.frente
            while actual is not None:
                print(f"- {actual.cliente} | Motivo: {actual.descripcion}")
                actual = actual.siguiente