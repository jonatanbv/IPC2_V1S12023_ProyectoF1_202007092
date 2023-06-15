class Cine:
    def __init__(self, nombre, sala_numero, asientos):
        self.nombre = nombre
        self.sala_numero = sala_numero
        self.asientos = asientos
        self.next = None
        self.previous = None

    def mostrar(self):
        print(f'Nombre Cine: {self.nombre}\nNo. sala: {self.sala_numero}\nAsientos: {self.asientos}\n')



class Cines: 
    def __init__(self):
        self.cabeza = None
    
    def vacia(self):
        return self.cabeza is None
    
    def add_cine(self, nombre, sala_numero, asientos):
        nuevo_cine = Cine(nombre, sala_numero, asientos)
        if self.vacia():
            self.cabeza = nuevo_cine
        else:
            cine_actual = self.cabeza
            while cine_actual.next is not None:
                cine_actual = cine_actual.next
            cine_actual.next = nuevo_cine
            nuevo_cine.previous = cine_actual
    
    def modificar_cine(self, cine, numero_sala):
        actual = self.cabeza
        while actual is not None:
            if actual.cine == cine:
                if actual.sala_numero == numero_sala:
                    actual.mostrar()
                    print('-------------INGRESE LOS DATOS NUEVOS------------')
                    nombre = input('Nombre del Cine: ')
                    actual.nombre = nombre
                    sala = input('Sala No.: ')
                    actual.sala_numero = sala
                    asientos = input('Asientos: ')
                    actual.asientos = asientos
                    return True
            actual = actual.next
        return False
    
    def eliminar_cine(self, nombre, salaNo):
        actual = self.cabeza
        while actual is not None:
            if actual.nombre == nombre:
                if actual.sala_numero == salaNo:
                    if self.cabeza is None:
                        return False
                    if self.cabeza.nombre == nombre:
                        self.cabeza = self.cabeza.next
                        return True
                    while actual.next is not None:
                        if actual.next.nombre == nombre:
                            actual.next = actual.next.next
                            return True
                        actual = actual.next
                    return True
            actual = actual.next
        return False
    
    def buscar_cine(self, nombre, noSala):
        actual = self.cabeza
        while actual is not None:
            if actual.nombre == nombre:
                if actual.sala_numero == noSala:
                    actual.mostrar()
                    return True
            actual = actual.next
        return False
    
    def buscar_sala(self, noSala):
        actual = self.cabeza
        while actual is not None:
            if actual.sala_numero == noSala:
                return True
            actual = actual.next
        return False
    
    def imprimir_cines(self):
        cine_actual = self.cabeza
        while cine_actual is not None:
            cine_actual.mostrar()
            cine_actual = cine_actual.next

    


