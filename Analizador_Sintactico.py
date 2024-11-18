import ply.yacc as yacc
from Analizador_Lexico import tokens

def p_programa(p):
    '''programa : sentencia
                | sentencia programa'''
    
def p_sentencia(p):
    '''sentencia : asignacion
                | impresion
                | array
                | condicion'''

def p_asignacion(p):
    'asignacion : variable ASIGNACION valores'


def p_impresion(p):
    'impresion : PUTS PARENTESIS_IZQ argumentos PARENTESIS_DER'

#Cristhian Vinces - 1 estructura de datos, 1 estructura de control y 1 tipo de función.
#1 estructura de datos
def p_array(p):
    'array : CORCHETE_IZQ argumentos CORCHETE_DER'

#1 estructura de control
def p_condicion(p):
    '''condicion : if
                | if_else
                | if_elsif_else'''

def p_if(p):
    '''if : IF expresion instrucciones END_BLOCK
            | IF expresion THEN instrucciones END_BLOCK'''
    
def p_if_else(p):
    '''if_else : IF expresion instrucciones ELSE instrucciones END_BLOCK
               | IF expresion THEN instrucciones ELSE instrucciones END_BLOCK'''

def p_if_elsif_else(p):
    '''if_elsif_else : IF expresion instrucciones elsif_clauses END_BLOCK
                     | IF expresion THEN instrucciones elsif_clauses END_BLOCK
                     | IF expresion instrucciones elsif_clauses ELSE instrucciones END_BLOCK
                     | IF expresion THEN instrucciones elsif_clauses ELSE instrucciones END_BLOCK'''

def p_elsif_clauses(p):
    '''elsif_clauses : ELSIF expresion instrucciones
                     | ELSIF expresion THEN instrucciones
                     | ELSIF expresion instrucciones elsif_clauses
                     | ELSIF expresion THEN instrucciones elsif_clauses'''


def p_expresion(p):
    '''expresion : var_expresion
                | var_expresion comparadores var_expresion
                | expresion comparadores expresion
                | PARENTESIS_IZQ expresion PARENTESIS_DER
                | NOT_BLOCK expresion
                | expresion operador_logico expresion'''

def p_comparadores(p):
    '''comparadores : MAYOR_QUE
                    | MENOR_QUE
                    | IGUAL_IGUAL
                    | DIFERENTE
                    | MAYOR_IGUAL
                    | MENOR_IGUAL'''
    
def p_operador_logico(p):
    '''operador_logico : AND
                        | OR
                        | NOT'''
    
def p_var_expresion(p):
    '''var_expresion : valor
                    | booleano'''
    
def p_instrucciones(p):
    '''instrucciones : instruccion
                    | instruccion instrucciones
                    | instruccion PUNTO_Y_COMA instrucciones'''
    
def p_instruccion(p): 
    '''instruccion : asignacion
                    | impresion
                    | condicion
                    | llamada_funcion'''
    
def p_llamada_funcion(p):
    '''llamada_funcion : VARIABLE_LOCAL PARENTESIS_IZQ argumentos PARENTESIS_DER
                       |  VARIABLE_LOCAL PARENTESIS_IZQ PARENTESIS_DER'''
    

def p_variable(p):
    '''variable : VARIABLE_LOCAL
                | VARIABLE_GLOBAL
                | VARIABLE_INSTANCIA
                | VARIABLE_CLASE'''

def p_booleano(p):
    '''booleano : FALSE
                | TRUE '''

def p_argumentos(p):
    '''argumentos : argumento
                    | argumento COMA argumentos'''

def p_argumento(p):
    '''argumento : booleano
                | operacionAritmetica
                | array
                | empty '''

def p_empty(p):
    'empty :'

def p_valores(p): 
    '''valores : operacionAritmetica
                | SIMBOLO
                | booleano
                | array'''

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
    if p:
        print(f"Error de sintaxis en la línea {p.lineno}, cerca de '{p.value}'")
    else:
        print("Error de sintaxis: final inesperado de la entrada.")

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