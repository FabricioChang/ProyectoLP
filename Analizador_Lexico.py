import ply.lex as lex
import os
import datetime

# Fabricio Chang - Inicio
path = r"C:\Users\fabri\OneDrive\Documents\GitHub\ProyectoLP"
# Palabras reservadas
reservadas = {
    'begin': 'BEGIN',
    'END': 'END',
    'alias': 'ALIAS', 
    'and': 'AND_BLOCK',
    'begin': 'BEGIN_BLOCK',
    'break': 'BREAK',
    'puts': 'PUTS',
    'if': 'IF',
    'else': 'ELSE',
    'begin': 'BEGIN_BLOCK',
    'end': 'END_BLOCK',
    'length': 'LENGTH',
    #Cristhian Vinces
    'elsif': 'ELSIF',
    'case': 'CASE',
    'false': 'FALSE',
    'do': 'DO',
    'then': 'THEN',
    'while': 'WHILE',
    'self': 'SELF',
    'true': 'TRUE',
    'def': 'DEF',
    'defined?': 'DEFINED',
    'return': 'RETURN',
    'unless': 'UNLESS',
    'super': 'SUPER',
    'until': 'UNTIL',
    'when': 'WHEN',
    'class': 'CLASS',
    'module': 'MODULE',
    'next': 'NEXT',
    'in': 'IN',
    'not': 'NOT_BLOCK',
    'redo': 'REDO',
    'retry': 'RETRY',
    'ensure': 'ENSURE'
    }

# Tokens para el lenguaje Ruby
#Fabricio Chang
tokens = (
    'VARIABLE_LOCAL',
    'VARIABLE_GLOBAL',
    'VARIABLE_INSTANCIA',
    'VARIABLE_CLASE',
    'NUMERO',
    'FLOTANTE',
    'CADENA',
    'MAS',
    'MENOS',
    'MULTIPLICAR',
    'DIVIDIR',
    'MODULO', 
    'EXPONENCIACION',
    'ASIGNACION',
    'AND',
    'OR',
    'NOT',
    'COMENTARIO',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'CORCHETE_IZQ',
    'CORCHETE_DER',
    'LLAVE_IZQ',
    'LLAVE_DER', 
    'RESERVADA',
    'MENOR_QUE',
    'MAYOR_QUE',
    'PUNTO',
    'GETS',
    #Cristhian Vinces
    'IGUAL_IGUAL',
    'DIFERENTE',
    'MAYOR_IGUAL',
    'MENOR_IGUAL',
    'FLECHA_HASH',
    'DOSPUNTOS',
    'PUNTO_Y_COMA',
    'COMA',
    'DOSPUNTOS_IGUAL',
    'INTERROGACION',
    'SIMBOLO'
)

tokens += tuple(reservadas.values())

# Expresiones regulares para tokens
#Fabricio Chang
t_CADENA = r'"([^"\\]|\\.)*"'
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'/'
t_MODULO = r'%'
t_EXPONENCIACION = r'\*\*'
t_ASIGNACION = r'='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_COMENTARIO = r'\#.*'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'
t_PUNTO =r'\.'
t_GETS = r'gets'
#Cristhian Vinces
t_IGUAL_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_FLECHA_HASH = r'=>'
t_DOSPUNTOS = r':'
t_PUNTO_Y_COMA = r';'
t_COMA = r','
t_DOSPUNTOS_IGUAL = r':='
t_SIMBOLO = r':[a-zA-Z_][a-zA-Z_0-9]*'
t_INTERROGACION = r'\?'


#Fabricio Chang
def t_FLOTANTE(t):
    r'(\d?|\d+)\.\d+'
    t.value = float(t.value)
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE_LOCAL(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'VARIABLE_LOCAL')
    return t

def t_VARIABLE_GLOBAL(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'VARIABLE_GLOBAL')
    return t

def t_VARIABLE_INSTANCIA(t):
    r'@[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'VARIABLE_INSTANCIA')
    return t

def t_VARIABLE_CLASE(t):
    r'@@[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'VARIABLE_CLASE')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignora espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores léxicos
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en línea {t.lineno}")
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()

# Función para generar un log con el nombre del archivo según la convención
def generar_log(nombre_usuario, contenido):
    fecha_hora = datetime.datetime.now().strftime("%d%m%Y-%Hh%M")
    nombre_archivo = os.path.join(path, f"lexico-{nombre_usuario}-{fecha_hora}.txt")
    
    try:
        os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)  # Verifica que el directorio exista
        with open(nombre_archivo, 'w') as log:
            log.write(contenido)
        print(f"Archivo de log '{nombre_archivo}' creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el archivo de log: {e}")
    

# Función para procesar un archivo de prueba y crear el log
def analizar_archivo(nombre_usuario, archivo_prueba):
    with open(archivo_prueba, 'r') as archivo:
        data = archivo.read()
        lexer.input(data)
        resultado = ""
        for token in lexer:
            resultado += f"{token.type}: {token.value}\n"
    generar_log(nombre_usuario, resultado)

def analizador_lexico(archivo):
    with open(archivo, 'r') as archivo:
        data = archivo.read()
        lexer.input(data)
        resultado = ""
        for token in lexer:
            resultado += f"{token.type}: {token.value}\n"
    return resultado