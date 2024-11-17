import ply.yacc as yacc
from Analizador_Lexico import tokens

def p_asignacion(p):
    'asignacion : variable ASIGNACION valor'

def p_variable(p):
    '''variable : VARIABLE_LOCAL
                | VARIABLE_GLOBAL
                | VARIABLE_INSTANCIA
                | VARIABLE_CLASE'''

def p_valor(p):
    '''valor : NUMERO
            | FLOTANTE
            | CADENA'''

def p_valor_Operacion(p):
    'valor : valor operador valor'

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