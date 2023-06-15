def ingresar_operacion():
    operacion = input("Ingrese la operación matemática: ")
    return operacion

def evaluar_operacion(operacion):
    operandos = []
    operadores = []
    
    for token in operacion:
        if token.isdigit():
            operandos.append(int(token))
        elif token == '(':
            operadores.append(token)
        elif token == ')':
            while operadores and operadores[-1] != '(':
                realizar_operacion(operandos, operadores)
            operadores.pop()  # Eliminar el paréntesis de apertura
        elif token in ['+', '-', '*', '/']:
            while operadores and obtener_prioridad(token) <= obtener_prioridad(operadores[-1]):
                realizar_operacion(operandos, operadores)
            operadores.append(token)
    
    while operadores:
        realizar_operacion(operandos, operadores)
    
    return operandos[0]

def realizar_operacion(operandos, operadores):
    operador = operadores.pop()
    segundo_operando = operandos.pop()
    primer_operando = operandos.pop()
    
    if operador == '+':
        resultado = primer_operando + segundo_operando
    elif operador == '-':
        resultado = primer_operando - segundo_operando
    elif operador == '*':
        resultado = primer_operando * segundo_operando
    elif operador == '/':
        resultado = primer_operando / segundo_operando
    
    operandos.append(resultado)

def obtener_prioridad(operador):
    if operador in ['+', '-']:
        return 1
    elif operador in ['*', '/']:
        return 2
    elif operador == '(':
        return 0

def ver_resultado(resultado):
    print("El resultado de la operación es:", resultado)

def menu():
    operacion = ''
    resultado = None
    
    while True:
        print("\n-- Menú --")
        print("1) Ingresar operación matemática")
        print("2) Ver resultado")
        print("3) Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            operacion = ingresar_operacion()
            resultado = None
        elif opcion == '2':
            if operacion:
                if resultado is None:
                    resultado = evaluar_operacion(operacion)
                ver_resultado(resultado)
            else:
                print("Debe ingresar una operación matemática primero.")
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()