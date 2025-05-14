#Definienfo la clase nodo
class Nodo:
    def __init__(self, paciente):
        self.paciente = paciente
        self.siguiente = None

class Paciente:
    def __init__(self, nombre, edad, enfermedad):
        self.nombre = nombre
        self.edad = edad
        self.enfermedad = enfermedad
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Enfermedad: {self.enfermedad}"


#Definiendo la clase Cola
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        

    def Insertar(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
    
    def Eliminar(self):
        if self.primero is None:
            return None
        else:
            dato = self.primero.paciente
            self.primero = self.primero.siguiente
            if self.primero is None:
                self.ultimo = None
            return dato
            
    def Imprimir(self):
        actual = self.primero
        if actual is None:
            print("Cola vacía.")
            return
        while actual is not None:
            print(actual.paciente, end="\n")
            actual = actual.siguiente
            
    def Buscar(self, nombre):
        actual = self.primero
        while actual is not None:
            if actual.paciente.nombre == nombre:
                return actual.paciente
            actual = actual.siguiente
        return None
        