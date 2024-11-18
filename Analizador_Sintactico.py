import ply.yacc as yacc
from Analizador_Lexico import tokens

def p_programa(p):
    '''programa : asignacion
                | impresion'''

def p_asignacion(p):
    'asignacion : variable ASIGNACION operacionAritmetica'

def p_impresion(p):
    'impresion : PUTS PARENTESIS_IZQ operacionAritmetica PARENTESIS_DER'

def p_variable(p):
    '''variable : VARIABLE_LOCAL
                | VARIABLE_GLOBAL
                | VARIABLE_INSTANCIA
                | VARIABLE_CLASE'''

def p_valor(p):
    '''valor : NUMERO
            | FLOTANTE
            | CADENA
            | variable'''

def p_operacionAritmetica(p):
    '''operacionAritmetica : valor 
                         | valor operador operacionAritmetica'''


def p_operador(p):
    '''operador : MAS
                | MENOS
                | MULTIPLICAR
                | DIVIDIR
                | MODULO
                | EXPONENCIACION'''

 # Error rule for syntax errors
def p_error(p):
    print("Error de sintaxis en la linea %d!" % p.lineno )

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)