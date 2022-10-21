import lexer

TABLA_PREDICTIVA = {
    'PROGRAM':{
        'mientras': ['ESTRUCTURA', 'PROGRAM'], 
        'id':       ['ESTRUCTURA', 'PROGRAM'], 
        'clp':      [], # ponemos nada ya que CLP finaliza un cierre de program
        'eof':        [], # lo mismo eof
        'si':       ['ESTRUCTURA', 'PROGRAM'], 
        'mostrar':  ['ESTRUCTURA', 'PROGRAM'], 
        'aceptar':  ['ESTRUCTURA', 'PROGRAM'], 
    },
    'ESTRUCTURA':{
        'aceptar': ['aceptar', 'id'], 
        'id': ['id', 'eq', 'EXPRESION'],
        'mientras': ['mientras', 'id', 'esMenorQue', 'VALOR', 'hacer', 'op', 'PROGRAM', 'clp'], 
        'si': ['si', 'EXPRESION', 'entonces', 'op', 'PROGRAM', 'clp', 'sino', 'op', 'PROGRAM', 'clp'], 
        'mostrar': ['mostrar', 'EXPRESION'], 
    },
    'EXPRESION':{
        '(':  ['TERMINO', 'EXPRESION2'], 
        'num': ['TERMINO', 'EXPRESION2'],
        'id':  ['TERMINO', 'EXPRESION2'],
    },
    'EXPRESION2':{
        '+':        ['+', 'TERMINO', "EXPRESION2"], 
        'eof':        [],
        ')':[],
         'mientras': [], 
        'id':       [], 
        'clp':      [], # ponemos nada ya que CLP finaliza un cierre de program
        'eof':        [], # lo mismo eof
        'si':       [], 
        'mostrar':  [], 
        'aceptar':  [], 
    },
    'FACTOR':{
        '(':        ['(', 'EXPRESION', ')'], 
        'id':       ['VALOR'], 
        'num':      ['VALOR']
    },
    'TERMINO':{
        '(':        ['FACTOR', 'TERMINO2'], 
        'id':       ['FACTOR', 'TERMINO2'], 
        'num':      ['FACTOR', 'TERMINO2'],
        ')': [],
        'mientras': [], 
        'id':       [], 
        'clp':      [], # ponemos nada ya que CLP finaliza un cierre de program
        'eof':        [], # lo mismo eof
        'si':       [], 
        'mostrar':  [], 
        'aceptar':  [], 
    },
    'TERMINO2':{
        '*':        ['*', 'FACTOR', 'TERMINO2'], 
        '+': [],
        'eof':        [],
        ')': [],
        'mientras': [], 
        'id':       [], 
        'clp':      [], # ponemos nada ya que CLP finaliza un cierre de program
        'eof':        [], # lo mismo eof
        'si':       [], 
        'mostrar':  [], 
        'aceptar':  [], 
    },
    'VALOR':{
        'num':['num'],
        'id': ['id'],
    },
}

# list comprehensions
terminales = [tokens[0] for tokens in lexer.TOKENS_POSIBLES]
noTerminales = [keys for keys in TABLA_PREDICTIVA.keys()]

def parser(lista_tokens):
    # inicializamos la PILA como nos piden
    pila = ['eof', 'PROGRAM']
    # a la lista de tokens pasado por el lexer le añadimos el EOF
    lista_tokens.append(('eof', 'eof'))
    # creamos un indice inicializado en 0
    index = 0
    # para sacar el TOPE de la lista en pytohn es poniendo lista[-1]
    tope = pila[-1] # ESTRUCTURA
    # creamos una lista de cadena final para mostrarla al final
    cadena_final = []

    # contador simplemente para imprimir los estaods de la pila 
    times = 0

    # Algoritmo de análisis sintáctico descendente predictivo con TABLA_PREDICTIVA.
    # mientras tope NO sea "eof" o T NO sea "eof", hacer ...
    while (tope  != "eof" or t != "eof"):
        # vamos mostrando la pila

        # si el index es menor a la lista de tokens, para que no se pase
        if index <= len(lista_tokens):
            # sacamos el tope de la pila
            tope = pila[-1] # la primera vez siempre será PROGRAM
            # creamos un T, osea un puntero para el terminar de la tupla de tokens ('eq','eq') 
            t = lista_tokens[index][0] 
            # si el tope está en terminales
            if tope in terminales:
                # si el tope es igual a lo contenido en T
                if tope == t:
                    # sacamos el tope
                    pila.pop()
                    # agregamos T a las cadena_final
                    cadena_final.append(t)
                    # aumentamos index +1
                    index += 1
                else:
                    # caso contrario, error, no pertenece al lenguaje
                    print("ERROR")
                    break
            else:
                # si no está en terminales, significa que es un NO TERMINAL
                try:
                    # sacamos tope 
                    pila.pop()

                    # damos vuelta la lista ya que la pila es inversa, y el algorimto
                    # pide que y1,y2,y3,yk, se sume a la pila como yk,y3,y2,y1.
                    revertido = TABLA_PREDICTIVA[tope][t][::-1] 
                    pila = pila + revertido # pila -> pila + lo revertido en la TABLA_PREDICTIVA , para que se una a la pila
                    # los nuevos NO temrinales y terminales
                    print("PILA ESTADO º", times, " - > ", pila)
                    times+=1
                except:
                    # si no se llega a encontrar la intersección en la TABLA_PREDICTIVA 
                    # de Tope con T , significa que NO pertenece al lenguaje.
                    break

    # cadena final
    print("Cadenas final VÁLIDAS -> ", cadena_final)

    
parser([('id', 'id'), ('eq', 'eq'), ('(', '('), ('num', 'num'), ('+','+'), ('num', 'num'), (')', ')')])
