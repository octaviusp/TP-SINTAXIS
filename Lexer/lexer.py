from automatas import *
# importamos los automatas

# todas las tuplas posibles de tokens posibles.
TOKENS_POSIBLES = [("eq", a_eq), ("num", a_num),
("+", a_suma) , ("*", a_multiplicacion),
("(", a_parentesisAbierto), (")", a_parentesisCerrado),
("si", a_si), ("entonces", a_entonces), ("sino", a_sino), 
("mostrar", a_mostrar), ("aceptar", a_aceptar), ("mientras", a_mientras),
("esMenorQue", a_esMenorQue), ("hacer", a_hacer), ("op", a_op),
("clp", a_clp), ("id", a_id)]

class Lexer:

    # constructor del lexer
    # inicializamos un nuevo lexer
    # con los tokens posibles pasados por parametro al instanciar la clase
    def __init__(self, tokens_posibles) -> None:
        self.TOKENS_POSIBLES = tokens_posibles

    # ESTA FUNCION SIMPLEMENTE
    # MUESTRA MAS LINDO LOS RESULTADOS DEL LEXER
    # Y QUITA LOS LEXEMAS INVALIDOS DEL TEXTO 
    def __formatear_tuplas(self, tuplas, lexemas_invalidos):
        texto = ""

        for tupla in tuplas:
            texto += f"- AUTOMATA:  {tupla[0]}  - LEXEMA: {tupla[1]} \n"
        if len(lexemas_invalidos) > 0:
            texto += f"\nLexemas invalidos\n{lexemas_invalidos}"
        return texto

    ## ACOMODA LA LISTA DE AUTOMATAS, PARA EL QUE SEA FINAL, ESTE ADELANTE DE TODOS.
    def __acomodar_listado_automatas(self, automatas):
        nueva_lista = []
        for automata in automatas:
            if automata[1] == "FINAL":
                nueva_lista = [automata] + nueva_lista
                continue
            nueva_lista.append(automata)
        return nueva_lista

    def __alimentar_automatas(self, lexema) -> list:
        # Creo array de aceptados
        posibles = []
        # por cada TUPLA en TOKENS_POSIBLES hacer...
        for (token, automata) in self.TOKENS_POSIBLES:
            # si el automata de la tupla actual queda en estado trampa
            # con el lexema actual, continuamos al siguiente automata, ya que este no lo acepta.
            # ejemplo, pasar 34 en el automata A_sino
            resultado = automata(lexema)
            if resultado == ESTADO_TRAMPA:
                continue
            # caso contrario, agregamos a aceptados el token de la tupla actual
            elif resultado == ESTADO_NO_FINAL:
                posibles.append((token, "NO FINAL"))
            elif resultado == ESTADO_FINAL:
                posibles.append((token, "FINAL"))
        # si la longitud del array aceptados es mayor a 0
        # retornar el aceptados[0], osea el primer automata de la lista
        #caso contrario, devolver lista vacia
        # ya que si no hacemos esto, nos tira error por devolver posicion [0] en lista vacia.
        posibles = self.__acomodar_listado_automatas(posibles)
        return posibles[0] if len(posibles) > 0 else []

    def __recorriendo_lexema(self, source_code, modo_test) -> list:
        # lista de tokens
        tokens = []
        # lista de tokens invalidos , por ejemplo = & % $ · !
        tokens_invalidos = []
        # variable para comenzar el texto a probar, empieza en 0
        start = 0

        # mientras la variable start es menor al codigo fuente, realizar...
        # ya que si no, nos pasariamos del codigo fuente, sin nada para corregir sintacticamente
        while start < len(source_code):
            # para ignorar los espacios
            while source_code[start] == " ":
                start+=1
            # variable start_lexema se iguala a start, para empezar a construir un lexema
            start_lexema = start
            # todos los posibles tokens con el lexema actual
            posibles_tokens = []
            # todos los posibles tokens con el lexema actual + un caracter
            # por ejemplo => 100, luego 100h
            posibles_tokens_extra_char = []
            # lexema es = palabra, para ir probando palabras en el codigo fuente
            lexema = ""
            # ciclo infinito pero luego se rompe si no hay automatas que acepten
            # el lexema
            while True:
                # si la variable start mayor que el codigo fuente, break ciclo
                if start >= len(source_code)+1:
                    break
                # lexema es igual al codigo fuente desde start_lexema hasta start+1
                lexema = source_code[start_lexema:start+1]
                # posibles tokens se iguala a posibles tokens extra caracter
                posibles_tokens = posibles_tokens_extra_char
                # extra caracter se iguala a array vacio
                posibles_tokens_extra_char = []
                # alimentamos TODOS los automatas con el lexema actual
                # result nos devuelve un array de automatas que aceptaron el lexema
                # pero solo tomamos el primero
                # ya que sino, por ej => SINO , aceptada por Automat_sino y automata_id
                # debemos regresar el primero, el Automata_sino
                # por eso en la funcion retorna array posicion 0
                result = self.__alimentar_automatas(lexema)
                # si la longitud de la variable result es igual a 0
                # significa que el lexema NO es valido, rompemos ciclo
                if len(result) == 0:
                    break
                # si el lexema es valido, agregamos a posibles tokens extra caracter
                else:
                    posibles_tokens_extra_char.append(result[0])

                # avanzamos un caracter en el codigo fuente
                # importante esto, ya que si no, se bugea
                start += 1

            # si longitud de posibles tokens > 0, entonces agregamos a tokens con su respecitvo lexema
            if len(posibles_tokens) > 0:
                tokens.append((posibles_tokens[0], source_code[start_lexema:start]))
            else:
                # caso contrario, TOKEN INVALIDO!
                tokens_invalidos.append(lexema)
                start += 1

        if modo_test:
            return tokens, tokens_invalidos
        else:
            return self.__formatear_tuplas(tokens, tokens_invalidos)

    # funcion para testear automatas por separado
    # no se usa , es para testing nomas
    def test_automatas(self, sour) -> str:
        print( self.__alimentar_automatas(sour))

    # funcion publica para utilizar el lexer privado
    def use(self, source_code, modo_test) -> None:
        return self.__recorriendo_lexema(source_code, modo_test)

LEXER = Lexer(TOKENS_POSIBLES)
print(LEXER.use("c$$$$$$$$ont*$", False))
