import ply.yacc as yacc
import datetime
import os
from Analizador_Lexico import tokens

path = r"C:\Users\fabri\Desktop"
def p_programa(p):
    '''programa : sentencia
                | sentencia programa'''
    
def p_sentencia(p):
    '''sentencia : asignacion
                | impresion
                | array
                | condicion
                | funcion
                | comentario'''

def p_asignacion(p):
    'asignacion : variable ASIGNACION valores'

def p_solicitud_datos(p):
    '''solicitud_datos : VARIABLE_LOCAL ASIGNACION GETS PARENTESIS_IZQ PARENTESIS_DER'''
    
def p_impresion(p):
    'impresion : PUTS PARENTESIS_IZQ argumentos PARENTESIS_DER'

def p_impresion_sin_argumentos(p):
    '''impresion : PUTS'''

def p_comentario(p):
    '''comentario : COMENTARIO argumento'''

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

# 1 Tipo de funcion 
def p_funcion(p):
    '''funcion : DEF VARIABLE_LOCAL PARENTESIS_IZQ parametros PARENTESIS_DER instrucciones END_BLOCK'''

def p_parametros(p):
    '''parametros : parametro
                  | parametro COMA parametros'''

def p_parametro(p):
    '''parametro : VARIABLE_LOCAL
                | empty'''


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
                    | llamada_funcion
                    | funcion'''
    
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
    
#Fabricio Chang - 1 estructura de datos, 1 estructura de control y 1 tipo de función.
#1 estructura de datos
def p_hash(p):
    '''hash : LLAVE_IZQ pares LLAVE_DER'''

def p_pares(p):
    '''pares : par
             | par COMA pares'''

def p_par(p):
    '''par : valor FLECHA_HASH valor'''

#1 estructura de control
def p_until(p):
    '''until : UNTIL expresion DO instrucciones END_BLOCK
             | UNTIL expresion instrucciones END_BLOCK'''

# 1 Tipo de funcion 
def p_funcion_parametros_defecto(p):
    '''funcion : DEF VARIABLE_LOCAL PARENTESIS_IZQ parametros_defecto PARENTESIS_DER instrucciones END_BLOCK'''

def p_parametros_defecto(p):
    '''parametros_defecto : parametro_defecto
                          | parametro_defecto COMA parametros_defecto'''

def p_parametro_defecto(p):
    '''parametro_defecto : VARIABLE_LOCAL
                         | VARIABLE_LOCAL ASIGNACION valor'''


def p_cadena_interpolacion(p):
    '''cadena_interpolacion : CADENA LLAVE_IZQ variable LLAVE_DER'''

def p_incremento(p):
    '''incremento : VARIABLE_LOCAL MAS ASIGNACION expresion'''


def find_column(input_data, token):
    """
    Encuentra la columna donde ocurrió el error basado en la posición del token.
    """
    last_newline = input_data.rfind('\n', 0, token.lexpos)
    if last_newline < 0:
        last_newline = -1
    return token.lexpos - last_newline

# Regla de error para errores sintácticos
def p_error(p):
    """
    Función que se activa cuando hay un error en el análisis sintáctico.
    """
    global input_data
    if p:
        col = find_column(input_data, p)
        raise SyntaxError(f"Error de sintaxis en la línea actual, columna {col}, cerca de '{p.value}'.")
    else:
        raise SyntaxError("Error de sintaxis: final inesperado de la entrada.")

# Construir el parser
parser = yacc.yacc()

def analizador_sintactico(file_path):
    """
    Analiza un archivo línea por línea y devuelve el resultado del análisis.
    """
    resultados = []
    try:
        with open(file_path, 'r') as archivo:
            for i, linea in enumerate(archivo, start=1):
                linea = linea.strip()  # Elimina espacios en blanco al inicio y final de la línea
                if not linea:  # Ignorar líneas vacías
                    continue

                global input_data
                input_data = linea

                # Asignar manualmente el número de línea
                parser.lineno = i
                
                try:
                    parser.parse(linea)
                    resultados.append(f"Línea {i}: Análisis sintáctico completado con éxito.")
                except SyntaxError as e:
                    resultados.append(f"Línea {i}: {e}")
        
        return resultados
    except FileNotFoundError:
        return [f"Error: No se pudo encontrar el archivo en la ruta '{file_path}'."]
    except Exception as e:
        return [f"Error al procesar el archivo: {e}."]