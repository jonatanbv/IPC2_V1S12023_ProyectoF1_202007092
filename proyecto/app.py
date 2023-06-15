import xml.etree.ElementTree as ET
from pelicula import Peliculas
from usuario import Usuarios
from cine import Cines
from tkinter import filedialog
from boleto import Boletos




lista_usuarios_fin = Usuarios()
lista_usuarios_fin.add_usuario('administrador', 'Jonatan', 'Vasquez', 'desc', 'jonatanbv', '1234')
lista_peliculas = Peliculas()
lista_cines = Cines()
lista_boletos = Boletos()


def leerXML_usuarios(ruta_xml):

    tree = ET.parse(ruta_xml)
    root = tree.getroot()
    lista_usuarios = Usuarios()

    for elemento in root.iter('usuarios'):
        for el in elemento.findall('usuario'):
            rol = el.find('rol').text
            nombre = el.find('nombre').text
            apellido = el.find('apellido').text
            telefono = el.find('telefono').text
            correo = el.find('correo').text
            contra = el.find('contrasena').text

            lista_usuarios_fin.add_usuario(rol, nombre, apellido, telefono, correo, contra)

def leerXML_cines(ruta_xml):
    tree = ET.parse(ruta_xml)
    root = tree.getroot()
   

    for cines in root.iter('cine'):
        nombre = cines.find('nombre').text
        #print('Nombre: ', nombre)
        for cine in cines.iter('salas'):
            for sala in cine.findall('sala'):
                numero = sala.find('numero').text
                asientos = sala.find('asientos').text

                lista_cines.add_cine(nombre,numero, asientos)
    
                
                

def leerXML_peliculas(ruta_xml):
    tree = ET.parse(ruta_xml)
    root = tree.getroot()


    for categoria in root.iter('categoria'):
        nombre = categoria.find('nombre').text
        #print('Nombre: ', nombre)
        for peliculas in categoria.iter('peliculas'):
            for pelicula in peliculas.findall('pelicula'):
                titulo = pelicula.find('titulo').text
                director = pelicula.find('director').text
                anio = pelicula.find('anio').text
                fecha = pelicula.find('fecha').text
                hora = pelicula.find('hora').text

                lista_peliculas.add_pelicula(nombre, titulo, director, anio, fecha, hora)
       



def modo_cliente(usuario):
    salir = True
    
    while salir:
        print('1-Listado Peliculas\n2-Peliculas Favoritas\n3-Comprar Boletos\n4-Boletos Comprados\n5-salir')
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            lista_peliculas.imprimir_pelicula()
        elif opcion == '2':
            print("se muestra listado peliculas favoritas")
        elif opcion == '3':
            lista_cines.imprimir_cines()
            print('INGRESE LOS DATOS DE LA PELICULA Y SALA')
            titulo = input('Titulo: ')
            hora = input('Hora: ')
            fecha = input('Fecha: ')
            pasar = lista_peliculas.buscar_pelicula(titulo, hora, fecha)
            if pasar:
                no_boletos = input('No. boletos: ')
                no_sala = input('No. Sala: ')
                sala_exis = lista_cines.buscar_sala(no_sala)
                if sala_exis:
                    nombre = input('Nombre: ')
                    nit = input('nit: ')
                    direccion = input('direccion: ')
                    
                    lista = []
                    for bols in range(int(no_boletos)):
                        dato = '202007092'+str(bols)
                        lista.append(dato)
                    
                    lista_boletos.add_compra(titulo, fecha, hora, no_boletos, no_sala, nombre, nit, direccion, usuario, lista)
                    
                else:
                    print("NO EXISTE EL NUMERO DE SALA")
            else:
                print('NO EXISTEN PELICULAS CON ESTOS DATOS')

        elif opcion == '4':
            lista_boletos.imprimir_boletos()
        elif opcion == '5':
            salir = False
        else:
            print('Opción inválida. Por favor, seleccione una opción válida.')

#--------------------- GESTION EN MODO AMDMINISTRADOR ---------------------------

def modo_administrador():
    salir = True
    while salir:
        print('1-Gestionar Usuarios\n2-Gestionar Peliculas\n3-Gestionar Salas\n4-Salir')
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            #------------ Gestiones de usuarios en modo administrador
            sal = True
            while sal:
                print('gestiona Usuarios')
                print('1-Ingresar XML\n2-Ingresar Usuario\n3-Buscar Usuario\n4-Actualizar Usuario\n5-Eliminar usuario\n6-Ver usuarios\n7-Salir')
                op = input('ingrese la opcion: ')
                if op == '1':
                    rut = filedialog.askopenfilename(title='Abrir')
                    leerXML_usuarios(rut)
                    
                elif op == '2':
                    print('\n--Ingrese los siguientes datos--')
                    rol = input('ROL: ')
                    nombre = input('Nombre: ')
                    apellido = input('Apellido: ')
                    telefono = input('Telefono: ')
                    correo = input('Correo: ')
                    contra = input('Contrasenia: ')

                    lista_usuarios_fin.add_usuario(rol, nombre, apellido, telefono, correo, contra)

                    print('Se ha cargado el usuario correctamente! :D')
                elif op == '3':
                    print('buscar Usuario')
                    nom = input('Ingrese el Nombre: ')
                    cor = input('Ingrese el correo: ')
                    existencia = lista_usuarios_fin.search_user(cor, nom)
                    if existencia:
                        print('USUARIO ENCONTRADO CON EXITO')
                    else:
                        print('EL USUARIO NO EXISTE')
                elif op == '4':
                    nom = input('Ingrese el nombre: ')
                    cor = input('Ingrese el correo')
                    lista_usuarios_fin.actualizar_user(cor, nom)
                elif op == '5':
                    nom = input('Ingrese el nombre de usuario a eliminar: ')
                    cor = input('Ingrese el correo del usuario a eliminar: ')
                    delete = lista_usuarios_fin.eliminar_user(nom, cor)
                    if delete:
                        print('Se elimino con Exito el usuario indicado')
                    else:
                        print('No se encontro datos del usuario indicado')
                elif op == '6':
                    lista_usuarios_fin.imprimir_usuarios()
                elif op == '7':
                    sal = False
                else:
                    print('Opción inválida. Por favor, seleccione una opción válida.')
            #------------ finalizan las gestiones de usuarios en modo administrador

        elif opcion == '2':
            #------------------------------- GESTION DE PELICULAS MODO USUARIO 
            print('se gestionan peliculas')
            sal = True
            while sal:
                print('1-Ingresar XML\n2-Ingresar Pelicula\n3-Buscar Pelicula\n4-Actualizar Pelicula\n5-Eliminar Pelicula\n6-Ver Peliculas\n7-Salir')
                op = input('ingrese la opcion: ')
                if op =='1':
                    rut = filedialog.askopenfilename(title='Abrir')
                    leerXML_peliculas(rut)
                elif op =='2':
                    print('------------INGRESE LOS SIGUIENTES DATOS--------------')
                    categoria = input('Categoria: ')
                    titulo = input('Titulo: ')
                    director = input('Director: ')
                    anio = input('Anio: ')
                    fecha = input('Fecha: ')
                    hora = input('Hora: ')

                    lista_peliculas.add_pelicula(categoria, titulo, director, anio, fecha, hora)
                    print('SE INGRESARON LOS DATOS CORRECTAMENTE! :D')

                elif op == '3':
                    print('---------------INGRESE LOS SIGUIENTES DATOS DE BUSQUEDA-------------')
                    titulo = input('TITULO: ')
                    hora = input('HORA: ')
                    fecha = input('FECHA: ')
                    busqueda = lista_peliculas.buscar_pelicula(titulo, hora, fecha)
                    if busqueda:
                        print('SE ENCONTRARON LOS DATOS DE FORMA CORRECTA')
                    else:
                        print('NO SE ENCONTRARON PELICULAS CON LOS DATOS ESPECIFICADOS')
                elif op == '4':
                    print('----------------INGRESE LOS SIGUIENTES DATOS DE BUSQUEDA------------')
                    titulo = input('Titulo: ')
                    hora = input('Hora: ')
                    fecha = input('Fecha: ')
                    busqueda = lista_peliculas.actualizar_pelicula(titulo, hora, fecha)
                    if busqueda:
                        print('Se ACTUALIZARON LOS DATO CORRECTAMENTE')
                    else:
                        print('NO SE ENCONTRARON PELICULAS CON LOS DATOS ESPECIFICADOS')

                elif op == '5':
                    print('---------------INGRESE LOS SIGUIENTES DATOS DE BUSQUEDA-------------')
                    titulo = input('Titulo: ')
                    hora = input('Hora: ')
                    fecha = input('Fecha: ')
                    eliminar = lista_peliculas.eliminar_pelicula(titulo, hora, fecha)
                    if eliminar:
                        print('SE ELIMINARON LOS DATOS CORRECTAMENTE')
                    else: 
                        print('NO SE ENCONTRARON PELICULAS CON LOS DATOS ESPECIFICADOS')
                elif op == '6':
                    lista_peliculas.imprimir_pelicula()
                elif op == '7':
                    sal = False
                else:
                    print('Opción inválida. Por favor, seleccione una opción válida.')


            #------------------------------- FINALIZA LA GESTION DE PELICULAS MODO USUARIO 
        elif opcion == '3':
            sal = True
            while sal:
                print('1-Ingresar XML\n2-Ingresar Sala\n3-Buscar Sala\n4-Actualizar Sala\n5-Eliminar Sala\n6-Ver Salas\n7-Salir')

                opcion = input('Ingrese la opcion: ')
                if opcion=='1':
                    rut = filedialog.askopenfilename(title='Abrir')
                    leerXML_cines(rut)
                elif opcion=='2':
                    print("------------Ingrese los datos de la sala a modificar-----------")
                    cine = input('Cine: ')
                    noSala = input('No. Salas: ')
                    asientos = input('Asientos: ')
                    lista_cines.add_cine(cine, noSala, asientos)
                    print('Se ingresaron los datos Correctamente')

                elif opcion=='3':
                    print("------------Ingrese los datos de la sala a modificar-----------")
                    cine = input('Cine: ')
                    salaNo = input('No. Sala: ')
                    busqueda = lista_cines.buscar_cine(cine, salaNo)
                    if busqueda:
                        print('SE ENCONTRARON LOS DATOS CORRECTAMENTE')
                    else:
                        print('NO SE ENCONTRARON SALAS CON LOS DATOS ESPECIFICADOS')

                elif opcion=='4':
                    print("------------Ingrese los datos de la sala a modificar-----------")
                    cine = input('Nombre: ')
                    salaNo = input('No. Sala: ')
                    modificar = lista_cines.modificar_cine(cine, salaNo)
                    if modificar:
                        print('SE MODIFICARON LOS DATOS CORRECTAMENTE')
                    else:
                        print('NO SE ENCONTRARON SALAS CON LOS DATOS ESPECIFICADOS')
                        
                elif opcion=='5':
                    print("------------Ingrese los datos de la sala a eliminar-----------")
                    nombre = input('Nombre: ')
                    salaNo = input('Sala No. : ')
                    eliminar = lista_cines.eliminar_cine(nombre, salaNo)
                    if eliminar:
                        print('SE ELIMINARON LOS DATOS CORRECTAMENTE')
                    else:
                        print('NO SE ENCONTRARON SALAS CON LOS DATOS ESPECIFICADOS')

                elif opcion=='6':
                    lista_cines.imprimir_cines()
                elif opcion=='7':
                    sal = False
                else:
                    print('Opción inválida. Por favor, seleccione una opción válida.')


        elif opcion == '4':
            salir = False
        else:
            print('Opción inválida. Por favor, seleccione una opción válida.')


#--------------------- FINALIZA LA GESTION EN MODO AMDMINISTRADOR ---------------------------

def iniciar_sesion(usuario, contrasenia):
    bandera = lista_usuarios_fin.buscar_usuario(usuario, contrasenia)
    rol = lista_usuarios_fin.rol_usuario(usuario, contrasenia)
    if bandera: 
        print('Bienvenido', usuario, '!!!')
        if rol == 'administrador':
            modo_administrador()
        elif rol == 'cliente':
            modo_cliente(usuario)
    else:
        print('Usuario o contrasenia incorrectas')



def menu():

    while True:
        print('\n--Menu--')
        print('1-Iniciar Sesion')
        print('2-Registrar Usuario')
        print('3-Ver listado de peliculas')
        print('4-salir')

        opcions = input('Ingrese la opcion: ')

        if opcions == '1':
            corre = input('Usuario: ')
            contr = input('Contrasenia: ')
            iniciar_sesion(corre, contr)
        elif opcions == '2':
            rol = 'cliente'
            print('\n--Ingrese los siguientes datos--')
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            telefono = input('Telefono: ')
            correo = input('Correo: ')
            contra = input('Contrasenia: ')

            lista_usuarios_fin.add_usuario(rol, nombre, apellido, telefono, correo, contra)

            print('Se ha cargado el usuario correctamente! :D')

        elif opcions == '3':
            lista_peliculas.imprimir_pelicula()
        elif opcions == '4':
            break
        else:
            print('Opción inválida. Por favor, seleccione una opción válida.')


#listaDos = leerXML_usuarios('prueba.xml')
#leerXML_cines('cines.xml')
#listaUno = 
#listaUno.imprimir_pelicula()
#print('----------------')
#listaDos.imprimir_usuarios()
#print('-----------------')
#listaTres = leerXML_cines('cines.xml')
#listaTres.imprimir_cines()
menu()
#modo_cliente('Jonibv')




