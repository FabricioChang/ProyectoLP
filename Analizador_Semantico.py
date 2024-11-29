import ast
import re

def extraer_asignaciones_y_funciones(archivo):
    """
    Extrae asignaciones y declaraciones de funciones desde el archivo fuente.
    """
    asignaciones = []
    funciones = []

    with open(archivo, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i, linea in enumerate(lines):
        linea = linea.strip()

        # Detectar asignaciones usando ast.literal_eval para evaluar tipos
        if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*.+', linea):
            try:
                partes = linea.split("=")
                variable = partes[0].strip()
                valor = partes[1].strip()
                tipo = type(ast.literal_eval(valor)).__name__
                asignaciones.append((variable, tipo, valor))
            except Exception:
                # Caso de error de asignación (ej: tipos incompatibles o sintaxis inválida)
                asignaciones.append((variable, "desconocido", valor))

        # Detectar funciones
        elif re.match(r'^def\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\(.*\):', linea):
            nombre_funcion = linea.split()[1].split("(")[0]
            tipo_retorno = "desconocido"
            valor_retorno = "desconocido"

            # Buscar el retorno dentro de la función
            for j in range(i+1, len(lines)):
                if "return" in lines[j]:
                    retorno = lines[j].split("return")[1].strip()
                    try:
                        valor_retorno = ast.literal_eval(retorno)
                        tipo_retorno = type(valor_retorno).__name__
                    except:
                        tipo_retorno = "desconocido"
                        valor_retorno = retorno
                    break
                elif "end" in lines[j]:  # Termina al encontrar 'end'
                    break
            funciones.append((nombre_funcion, tipo_retorno, valor_retorno))

    return asignaciones, funciones

def verificar_tipos(asignaciones):
    """
    Verifica que las asignaciones sean consistentes en términos de tipo.
    """
    errores = []
    for variable, tipo, valor in asignaciones:
        if tipo == "desconocido":
            errores.append(f"Error: No se pudo determinar el tipo de la variable '{variable}' con valor '{valor}'.")
    return errores


def verificar_funciones(funciones):
    """
    Valida que las funciones retornen el tipo esperado.
    """
    errores = []
    for funcion, tipo_retorno, valor_retorno in funciones:
        if tipo_retorno == "desconocido":
            errores.append(f"Error en la función '{funcion}': Tipo de retorno desconocido o no válido ('{valor_retorno}').")
    return errores


def analizador_semantico(archivo):
    """
    Ejecuta el análisis semántico.
    """
    asignaciones, funciones = extraer_asignaciones_y_funciones(archivo)
    errores = []
    errores.extend(verificar_tipos(asignaciones))
    errores.extend(verificar_funciones(funciones))
    
    if errores:
        return "\n".join(errores)
    else:
        return "Análisis semántico completado sin errores."