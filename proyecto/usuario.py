class Usuario:
    def __init__(self,rol, nombre, apellido, telefono, correo, contra):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contra = contra
        self.siguiente = None
    
    def mostrar(self):
        print('\n---DATOS--')
        print(f'rol: {self.rol}\nnombre: {self.nombre} {self.apellido}\ntelefono: {self.telefono}\ncorreo: {self.correo}')
        print('------\n')


class Usuarios:
    def __init__(self):
        self.cabeza = None

    def add_usuario(self, rol, nombre, apellido, telefono, correo, contra):
        nuevo_usuario = Usuario(rol, nombre, apellido, telefono, correo, contra)

        if self.cabeza is None:
            self.cabeza = nuevo_usuario
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_usuario

    def buscar_usuario(self, correo, contra):
        actual = self.cabeza
        while actual is not None:
            if actual.correo == correo:
                if actual.contra == contra:
                    actual.mostrar()
                    return True
            actual = actual.siguiente
        return False
    
    def rol_usuario(self, correo, contra):
        actual = self.cabeza
        while actual is not None:
            if actual.correo == correo:
                if actual.contra == contra:
                    return actual.rol
            actual = actual.siguiente

    def search_user(self, correo, nombre):
        actual = self.cabeza
        while actual is not None:
            if actual.correo == correo:
                if actual.nombre == nombre:
                    actual.mostrar()
                    return True
            actual = actual.siguiente
        return False 
    
    def actualizar_user(self, correo, nombre):
        actual = self.cabeza
        while actual is not None:
            if actual.correo == correo:
                if actual.nombre == nombre:
                    actual.mostrar()
                    print('\n--Ingrese los datos Nuevos--')
                    rol = input('ROL: ')
                    actual.rol = rol
                    nom = input('Nombre: ')
                    actual.nombre = nom
                    apellido = input('Apellido: ')
                    actual.apellido = apellido
                    telefono = input('Telefono: ')
                    actual.telefono = telefono
                    corr = input('Correo: ')
                    actual.correo = corr
                    contra = input('Contrasenia: ')
                    actual.contra = contra
                    return True
            actual = actual.siguiente
        return False 
    
    def eliminar_user(self, nombre, correo):
        actual = self.cabeza
        while actual is not None:
            if actual.correo == correo:
                if actual.nombre == nombre:
                    if self.cabeza is None: 
                        return False
                    if self.cabeza.nombre == nombre:
                        self.cabeza = self.cabeza.siguiente
                        return True
                    actual = self.cabeza
                    while actual.siguiente is not None:
                        if actual.siguiente.nombre == nombre:
                            actual.siguiente = actual.siguiente.siguiente
                            return True
                        actual = actual.siguiente
                    return True
            actual = actual.siguiente
        return False 
        
    def imprimir_usuarios(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            nodo_actual.mostrar()
            nodo_actual = nodo_actual.siguiente
