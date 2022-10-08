from lexer import *

class Tests:
    def integrated_test(self):
        LEXER = Lexer(TOKENS_POSIBLES)

        resultado_1 = LEXER.use("si 20 &&&&&&&  5 && 4 & 2")
        assert resultado_1 == ([(['si'], 'si '), (['num'], '20 '), (['num'], '5 '), (['num'], '4 '), (['num'], '2')], ['&', '&', '&', '&', '&', '&', '&', '&', '&', '&'])

        resultado_2 = LEXER.use("cont*")
        assert resultado_2 == ([(['id'], 'cont*'), (['*'], '*')], [])

        resultado_3 = LEXER.use("333vaux")
        assert resultado_3 == ([(['num'], '333v'), (['id'], 'vaux')], [])

        resultado_4 = LEXER.use("si 10 esMenorQue 20 entonces mostrar 21")
        assert resultado_4 == ([(['si'], 'si '), (['num'], '10 '), (['esMenorQue'], 'esMenorQue '), (['num'], '20 '), (['entonces'], 'entonces '), (['mostrar'], 'mostrar '), (['num'], '21')], [])
        
        resultado_5 = LEXER.use("mostrar 80 sino 21 21 + 55")
        assert resultado_5 == ([(['mostrar'], 'mostrar '), (['num'], '80 '), (['sino'], 'sino '), (['num'], 
'21 '), (['num'], '21 '), (['+'], '+ '), (['num'], '55')], [])

        resultado_6 = LEXER.use("mientras 0 esMenorQue 1 hacer mostrar 55 sino hacer mostrar -1")
        assert resultado_6 == ([(['mientras'], 'mientras '), (['num'], '0 '), (['esMenorQue'], 'esMenorQue '), (['num'], '1 '), (['hacer'], 'hacer '), (['mostrar'], 'mostrar '), (['num'], '55 '), (['sino'], 'sino '), (['hacer'], 'hacer '), (['mostrar'], 'mostrar '), (['num'], '1')], ['-'])
        
        resultado_7 = LEXER.use("si 40 entonces (contador eq 21) entonces 10 mientras 0 eq 20")
        assert resultado_7 == ([(['si'], 'si '), (['num'], '40 '), (['entonces'], 'entonces '), (['('], '(c'), (['id'], 'contador '), (['eq'], 'eq '), (['num'], '21)'), ([')'], ') '), (['entonces'], 'entonces '), (['num'], '10 '), (['mientras'], 'mientras '), (['num'], '0 '), (['eq'], 'eq '), (['num'], '20')], [])
        
        resultado_8 = LEXER.use("&&/$$$···### 2 + 2 ··$")
        assert resultado_8 == ([(['num'], '2 '), (['+'], '+ '), (['num'], '2 ')], ['&', '&', '/', '$', '$', 
'$', '·', '·', '·', '#', '#', '#', '·', '·', '$'])
        
        resultado_9 = LEXER.use("((((((((((( )))))))))))")
        assert resultado_9 == ([(['('], '((((((((((( '), ([')'], ')))))))))))')], [])
        
        resultado_10 = LEXER.use("contador eq 20 si ( 2 * 10 ) eq contador mostrar esNumeroPar")
        assert resultado_10 == ([(['id'], 'contador '), (['eq'], 'eq '), (['num'], '20 '), (['si'], 'si '), (['('], '( '), (['num'], '2 '), (['*'], '* '), (['num'], '10 '), ([')'], ') '), (['eq'], 'eq '), (['id'], 'contador '), (['mostrar'], 'mostrar '), (['id'], 'esNumeroPar')], [])

if __name__ == "__main__":
    test_parte_1 = Tests()
    test_parte_1.integrated_test()






