class Boleto:
    def __init__(self, pelicula, fecha, hora, no_boletos, no_sala, nombre,  nit, direccion, usuario, listaBoletos):
        self.pelicula = pelicula
        self.fecha = fecha
        self.hora = hora
        self.no_boletos = no_boletos
        self.no_sala = no_sala
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.usuario = usuario
        self.next = None
        self.previous = None
        self.total = 42
        self.listaBoletos = listaBoletos

    def mostrar(self): 
        print('---------------FACTURA-------------')
        print(f'Pelicula: {self.pelicula}\nFecha: {self.fecha}\nHora: {self.hora}\nNo.Sala: {self.no_sala}\nNo. boletos: {self.no_boletos}\nNombre: {self.nombre}\nNIT: {self.nit}\nDireccion: {self.direccion}\nUsuario: {self.usuario}')
        print('----------LISTA ASIENTOS-----------')
        for bol in self.listaBoletos:
            print(bol)
        print('--------------Total---------------')
        print('Q', self.total*int(self.no_boletos))
        print('----------------------------------')


class Boletos():
    def __init__(self):
        self.cabeza = None

    def vacia(self):
        return self.cabeza is None
    
    def add_compra(self, pelicula, fecha, hora, no_boletos, no_sala, nombre, nit, direccion, usuario, listaBoletos):
        nuevo_boleto = Boleto(pelicula, fecha, hora, no_boletos, no_sala, nombre, nit, direccion, usuario, listaBoletos)
        if self.vacia():
            self.cabeza = nuevo_boleto
        else:
            boleto_actual = self.cabeza
            while boleto_actual.next is not None:
                boleto_actual = boleto_actual.next
            boleto_actual.next = nuevo_boleto
            nuevo_boleto.previous = boleto_actual

    def imprimir_boletos(self):
        boleto_actual = self.cabeza
        while boleto_actual is not None:
            boleto_actual.mostrar()
            boleto_actual = boleto_actual.next



