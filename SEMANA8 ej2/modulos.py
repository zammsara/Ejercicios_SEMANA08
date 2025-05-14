class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class LlamadaCliente:
    def __init__(self, nombre, motivo):
        self.nombre = nombre
        self.motivo = motivo

    def __str__(self):
        return f"{self.nombre} - Motivo: {self.motivo}"

class ColaLlamadas:
    def __init__(self):
        self.frente = None
        self.final = None

    def insertar(self, llamada):
        nuevo = Nodo(llamada)
        if self.final is None:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def eliminar(self):
        if self.frente is None:
            print("La cola está vacía.")
            return None
        eliminado = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        print(f"Llamada de '{eliminado.nombre}' atendida.")
        return eliminado

    def imprimir(self):
        if self.frente is None:
            print("Cola vacía.")
            return
        print("Llamadas en cola:")
        actual = self.frente
        while actual is not None:
            print(f" - {actual.dato}")
            actual = actual.siguiente
