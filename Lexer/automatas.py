################ CONSTANTES #######################
# obtengo todas las letras mapeando los asci codes en el                  #
# rango de la A hasta la Z,                                                                      #
# luego lo convierto en lista                                                                   #  
LETRAS = list(map(chr, range(97, 123)))                                                 #
# mapeo las letras minusculas y las paso a mayus                             #
LETRAS_MAYUS = list(map(lambda letter: letter.upper(),LETRAS))       #
# mapeo todos los numeros del rango 0 a 9 y los paso a string          #
NUMEROS = list(map(lambda number: str(number), range(0,10)))     
NO_IDS = ['esMenorQue', 'hacer', 'aceptar', 'entonces', 'mientras', 
'op', 'si', 'eq', 'clp', 'mostrar', 'sino']  #

################################################ #
ESTADO_FINAL = "ESTADO FINAL"                                                        #
ESTADO_NO_FINAL = "ESTADO NO FINAL"                                           #
ESTADO_TRAMPA = "ESTADO TRAMPA"                                                #
#################################################

############# AUTOMATA PARA CADA TOKEN VALIDO PROPUESTO EN LA GRAMATICA ##############

# token ID
def a_id(cadena):
    estado_actual = 0
    first = True

    if cadena in NO_IDS:
        return ESTADO_NO_FINAL

    for letra in cadena:
        if first and letra in NUMEROS:
            return ESTADO_TRAMPA
        elif (letra in LETRAS or letra in LETRAS_MAYUS or letra in NUMEROS) and estado_actual == 0:
            first = False
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    return ESTADO_FINAL
# token MIENTRAS
def a_mientras(cadena):
    estado_actual = 0
    estados_finales = [8]
    for caracter in cadena:
        if estado_actual == 0 and caracter == 'm':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'i':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'e':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'n':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 't':
            estado_actual = 5
        elif estado_actual == 5 and caracter == 'r':
            estado_actual = 6
        elif estado_actual == 6 and caracter == 'a':
            estado_actual = 7
        elif estado_actual == 7 and caracter == 's':
            estado_actual = 8
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# token *
def a_multiplicacion(cadena):
    estado_actual = 0
    for letra in cadena:
        if estado_actual == 0 and letra == "*":
            estado_actual = 1
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    return ESTADO_FINAL
# token NUM
def a_num(cadena):
    estado_actual = 0
    for letra in cadena:
        if letra in NUMEROS and estado_actual == 0:
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    if estado_actual == 0:
        try:
            value = int(cadena)
            return ESTADO_FINAL
        except:
            return ESTADO_TRAMPA
# token )
def a_parentesisCerrado(cadena):
    estado_actual = 0
    for letra in cadena:
        if estado_actual == 0 and letra == ")":
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    return ESTADO_FINAL
# token (
def a_parentesisAbierto(cadena):
    estado_actual = 0    
    for letra in cadena:
        if estado_actual == 0 and letra == "(":
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    return ESTADO_FINAL
# token +
def a_suma(cadena):
    estado_actual = 0
    for letra in cadena:
        if estado_actual == 0 and letra == "+":
            estado_actual = 0
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    return ESTADO_FINAL
# token SI
def a_si(cadena):
    estado_actual = 0
    estados_finales = [2]
    
    for letra in cadena:
        if estado_actual == 0 and letra == 's':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'i':
            estado_actual = 2
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# token ENTONCES
def a_entonces(cadena):
    estado_actual = 0
    estados_finales = [8]
    
    for letra in cadena:
        if estado_actual == 0 and letra == 'e':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'n':
            estado_actual = 2
        elif estado_actual == 2 and letra == 't':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'o':
            estado_actual = 4
        elif estado_actual == 4 and letra == 'n':
            estado_actual = 5
        elif estado_actual == 5 and letra == 'c':
            estado_actual = 6
        elif estado_actual == 6 and letra == 'e':
            estado_actual = 7
        elif estado_actual == 7 and letra == 's':
            estado_actual = 8
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# token SINO
def a_sino(cadena):
    estado_actual = 0
    estados_finales = [4]
    
    for letra in cadena:
        if estado_actual == 0 and letra == 's':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'i':
            estado_actual = 2
        elif estado_actual == 2 and letra == 'n':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'o':
            estado_actual = 4
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# token HACER
def a_hacer(cadena):
    estado_actual = 0
    estadosFinales = [5]
    for caracter in cadena:
        if estado_actual == 0 and caracter == 'h':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'a':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'c':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'e':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'r':
            estado_actual = 5
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estadosFinales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# token MOSTRAR
def a_mostrar(cadena):
    estado_actual = 0
    estados_finales = [7]
    
    for letra in cadena:
        if estado_actual == 0 and letra == 'm':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'o':
            estado_actual = 2
        elif estado_actual == 2 and letra == 's':
            estado_actual = 3
        elif estado_actual == 3 and letra == 't':
            estado_actual = 4
        elif estado_actual == 4 and letra == 'r':
            estado_actual = 5
        elif estado_actual == 5 and letra == 'a':
            estado_actual = 6
        elif estado_actual == 6 and letra == 'r':
            estado_actual = 7
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# token ACEPTAR
def a_aceptar(cadena):
    estado_actual = 0
    estados_finales = [7]
    
    for letra in cadena:
        if estado_actual == 0 and letra == 'a':
            estado_actual = 1
        elif estado_actual == 1 and letra == 'c':
            estado_actual = 2
        elif estado_actual == 2 and letra == 'e':
            estado_actual = 3
        elif estado_actual == 3 and letra == 'p':
            estado_actual = 4
        elif estado_actual == 4 and letra == 't':
            estado_actual = 5
        elif estado_actual == 5 and letra == 'a':
            estado_actual = 6
        elif estado_actual == 6 and letra == 'r':
            estado_actual = 7
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# token EQ 
def a_eq(cadena):
    estado_actual = 0
    estados_finales = [2]
    for letra in cadena:
        if letra == 'e' and estado_actual == 0:
            estado_actual = 1
        elif letra == 'q' and estado_actual == 1:
            estado_actual = 2
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# token ESMENORQUE
def a_esMenorQue(cadena):
    cadena = cadena.lower()
    estado_actual = 0
    estadosFinales = [10]
    
    for caracter in cadena:
        if estado_actual == 0 and caracter == 'e':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 's':
            estado_actual = 2
        elif estado_actual == 2 and caracter.upper() == 'M':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'e':
            estado_actual = 4
        elif estado_actual == 4 and caracter == 'n':
            estado_actual = 5
        elif estado_actual == 5 and caracter == 'o':
            estado_actual = 6
        elif estado_actual == 6 and caracter == 'r':
            estado_actual = 7
        elif estado_actual == 7 and caracter.upper() == 'Q':
            estado_actual = 8
        elif estado_actual == 8 and caracter == 'u':
            estado_actual = 9
        elif estado_actual == 9 and caracter == 'e':
            estado_actual = 10
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estadosFinales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# token CLP
def a_clp(cadena):
    estado_actual = 0
    estadosFinales = [3]
    
    for caracter in cadena:
        if estado_actual == 0 and caracter == 'c':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'l':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 'p':
            estado_actual = 3
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estadosFinales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# token OP
def a_op(cadena):
    estado_actual = 0
    estadosFinales = [2]
    
    for caracter in cadena:
        if estado_actual == 0 and caracter == 'o':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'p':
            estado_actual = 2
        else:
            estado_actual = -1
            return ESTADO_TRAMPA
    
    if estado_actual in estadosFinales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
