class Pelicula:
    def __init__(self,categoria, titulo, director, anio, fecha, hora):
        self.categoria = categoria
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora
        self.next = None
        self.previous = None

    def mostrar(self):
        print(f'Categoria: {self.categoria}\nTitulo: {self.titulo}\nDirector: {self.director}\nAnio: {self.anio}\nFecha: {self.fecha}\nHora: {self.hora}\n')

class Peliculas: 
    def __init__(self):
        self.cabeza = None

    def vacia(self):
        return self.cabeza is None
    
    def add_pelicula(self, categoria, titulo, director, anio, fecha, hora):
        nueva_pelicula = Pelicula(categoria, titulo, director, anio, fecha, hora)
        if self.vacia():
            self.cabeza = nueva_pelicula
        else:
            pelicula_actual = self.cabeza
            while pelicula_actual.next is not None:
                pelicula_actual = pelicula_actual.next
            pelicula_actual.next = nueva_pelicula
            nueva_pelicula.previous = pelicula_actual

    def buscar_pelicula(self, titulo, hora, fecha):
        actual = self.cabeza
        while actual is not None:
            if actual.titulo == titulo:
                if actual.hora == hora:
                    if actual.fecha == fecha:
                        actual.mostrar()
                        return True
            actual = actual.next
        return False
    
    def datos_pelicula(self, titulo, hora, fecha):
        actual = self.cabeza
        while actual is not None:
            if actual.titulo == titulo:
                if actual.hora == hora:
                    if actual.fecha == fecha:
                        return Pelicula(actual.categoria, actual.titulo, actual.director, actual.anio, actual.fecha, actual.hora)
            actual = actual.next
        return False
    
    def actualizar_pelicula(self, titulo, hora, fecha):
        actual = self.cabeza
        while actual is not None:
            if actual.titulo == titulo:
                if actual.hora == hora:
                    if actual.fecha == fecha:
                        actual.mostrar()
                        print('----------INGRESE LOS DATOS NUEVOS------')
                        categoria = input('Categoria: ')
                        actual.categoria = categoria
                        titulo = input('Titulo: ')
                        actual.titulo = titulo
                        director = input('Director: ')
                        actual.director = director
                        anio = input('Anio: ')
                        actual.anio = anio
                        fecha = input('fecha: ')
                        actual.fecha = fecha
                        hora = input('Hora: ')
                        actual.hora = hora
                        return True
            actual = actual.next
        return False
    
    def eliminar_pelicula(self, titulo, hora, fecha):
        actual = self.cabeza
        while actual is not None:
            if actual.titulo == titulo:
                if actual.hora == hora:
                    if actual.fecha == fecha:
                        if self.cabeza is None:
                            return False
                        if self.cabeza.titulo == titulo:
                            self.cabeza = self.cabeza.next
                            return True
                        while actual.next is not None:
                            if actual.next.titulo == titulo:
                                actual.next = actual.next.next
                                return True
                        return True
            actual = actual.next
        return False

    def imprimir_pelicula(self):
        pelicula_actual = self.cabeza
        while pelicula_actual is not None:
            pelicula_actual.mostrar()
            pelicula_actual = pelicula_actual.next




