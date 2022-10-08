import lexer
import parser

Terminales = [tokens[0] for tokens in lexer.TOKENS_POSIBLES]

noTerminales = [
'PROGRAM'
,'ESTRUCTURA'
,'VALOR'
,"EXPRESION"
,"EXPRESION2"
,"TERMINO"
,"TERMINO2"
,"FACTOR"
]

PRODUCCIONES = {
    
    # diccionario, mapa key:value
    # las keys son los NO TERMINALES
    # los values Minuscula son TERMINALES,
    # en Mayuscula son NO TERMINALES osea las keys!
    
    # Las producciones que tenian lambda se reemplazan como si fueran un espacio vacio
    # por lo que
    # Program -> Estructura Program | lambda
    # quedaria =>     'PROGRAM':[['ESTRUCTURA', 'Program'], ['ESTRUCTURA']]
    # es decir el segundo elemento es como ESTRUCTURA LAMBDA, pero tomamos a lambda como vacio. y queda solo ESTRUCTURA.
    
    'PROGRAM':[['ESTRUCTURA', 'Program'], ['ESTRUCTURA']],
    'ESTRUCTURA':[["mientras", "id", "esMenorQue","Valor","hacer","op", "Program", "clp"], ["si", "Expresion", "entonces", "op", "PROGRAM", "clp", "sino", "op"], ["PROGRAM", "clp"], ["mostrar", "EXPRESION"], ["aceptar", "id"], ["id", "eq", "EXPRESION"]],
    'VALOR':[["id"], ["num"]],
    "EXPRESION":[["TERMINO", "EXPRESION2"], ['TERMINO']],
    "EXPRESION2":[["+", "TERMINO", "EXPRESION2"], ["+", "TERMINO"]],
    "TERMINO":[["FACTOR", "TERMINO2"]],
    "TERMINO2":[["*", "FACTOR", "TERMINO2"], ["*", "FACTOR"]],
    "FACTOR":[["(", "EXPRESION", ")"], ["VALOR"]]
}

Parserito = parser.Parser(PRODUCCIONES, lexer.TOKENS_POSIBLES, Terminales, noTerminales)
