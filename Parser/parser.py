class Parser:

    # creamos una clase Parser donde va a contener como atributos
    # donde Hernán tiene el diccionario de parser
    def __init__(self, producciones, tokens_posibles, terminales, noTerminales):
        self.producciones = producciones
        self.tokens = tokens_posibles
        self.posicion_indice = 0
        self.error = False
        self.Terminales = terminales
        self.noTerminales = noTerminales

    def parsear(lista_tokens) -> bool:
        return True

    def cambiarError(self):
        self.error = True if not self.error else False

    def tokenActual(self):
        return self.tokens[self.posicion_indice][0]

    def principal(self) -> bool:
        # Si esta funcion devuelve False
        # significa que la cadena NO pertenece
        # si es TRUE , SI pertenece
        self.pni('PROGRAM')
        return not ((self.tokenActual != 'eof') or self.error)
    
    def pni(self, no_terminal):
        for ladoDerecho in PRODUCCIONES[no_terminal]:
            # snapshoteamos la posicion para guardarla
            # por si algo sale mal
            pos_a_retroceder = self.posicion_indice
            # procesamos el lado derecho ed las producciones
            self.procesar(ladoDerecho)
            # si sale mal, volvemos al snapshop
            if self.error:
                self.posicion_indice = pos_a_retroceder
            else:
                # caso contrario nada salio mal, salimos del ciclo
                break
    
    def procesar(self, ladoDerecho):
        for simbolo in ladoDerecho:
            self.error = False
            if simbolo in self.Terminales:
                if simbolo == self.tokenActual:
                    self.posicion_indice += 1
                else:
                    self.cambiarError()
                    break
            
            elif simbolo in self.noTerminales:
                self.pni(simbolo)
                if self.error:
                    break
