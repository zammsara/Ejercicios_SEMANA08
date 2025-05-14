#Definienfo la clase nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

#El que llama al call center
class Caller:
    def __init__(self, nombre, motivo):
        self.nombre = nombre
        self.motivo = motivo
    def __str__(self):
        return f"Nombre: {self.nombre}, Motivo: {self.motivo}"
    
        
        

#Definiendo la clase Cola
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    #Insertar un cliente en la cola
    def Insertar(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
    
    #[Atendemos] eliminamos un cliente de la cola
    def Eliminar(self):
        if self.primero is None:
            return None
        else:
            dato = self.primero.dato
            self.primero = self.primero.siguiente
            if self.primero is None:
                self.ultimo = None
            return dato
    
    #Imprimir la lista de clientes     
    def Imprimir(self):
        actual = self.primero
        if actual is None:
            print("Cola vacía.")
            return
        while actual is not None:
            print(actual.dato, end="\n")
            actual = actual.siguiente
            
    #Buscar un cliente por nombre
    #Si devolvemos None, significa que no hay clientes en la cola, sino se devuelve el cliente
    def Buscar(self, nombre):
        actual = self.primero
        #Si devolvemos None, significa que no hay pacientes en la cola, sino se devuelve el paciente
        while actual is not None:
            if actual.dato.nombre == nombre:
                return actual.dato
            actual = actual.siguiente
        