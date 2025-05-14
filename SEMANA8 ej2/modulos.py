class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Contiene el objeto LlamadaCliente
        self.siguiente = None # Apunta al siguiente nodo en la cola

class LlamadaCliente:
    def __init__(self, nombre, motivo):
        self.nombre = nombre # Nombre del cliente
        self.motivo = motivo # Motivo de la llamada 

    def __str__(self):
        return f"{self.nombre} - Motivo: {self.motivo}" # Representación de la llamada en la terminal 

class ColaLlamadas: # Cola para gestionar las llamadas
    def __init__(self):
        self.frente = None # Apunta al primer nodo de la cola 
        self.final = None # Apunta al último nodo de la cola

    # Método para insertar una llamada en la cola
    def insertar(self, llamada):
        nuevo = Nodo(llamada)
        if self.final is None: # Si la cola está vacía
            self.frente = self.final = nuevo # Inicializa el frente y el final de la cola
        else: # Si la cola no está vacía
            self.final.siguiente = nuevo # Enlaza el nuevo nodo al final de la cola
            self.final = nuevo # Actualiza el final de la cola 

    def eliminar(self): # Método para eliminar una llamada de la cola 
        if self.frente is None: # Si la cola está vacía
            print("La cola está vacía.") # No hay clientes para atender 
            return None
        eliminado = self.frente.dato # Guarda el dato del nodo que se va a eliminar
        self.frente = self.frente.siguiente # Actualiza el frente de la cola 
        if self.frente is None: # Si la cola queda vacía después de eliminar
            self.final = None # Actualiza el final de la cola 
        print(f"Llamada de '{eliminado.nombre}' atendida.") # Imprime el nombre del cliente atendido
        return eliminado

    def imprimir(self): # Método para imprimir las llamadas en la cola 
        if self.frente is None: # Si la cola está vacía
            print("Cola vacía.")
            return
        print("Llamadas en cola:")
        actual = self.frente
        while actual is not None: # Recorre la cola
            print(f" - {actual.dato}") # Imprime el dato del nodo actual
            actual = actual.siguiente # Avanza al siguiente nodo 
