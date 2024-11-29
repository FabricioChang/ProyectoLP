import os

def verificar_tipos(asignaciones):
    """
    Verifica que las asignaciones sean consistentes en términos de tipo.
    Ejemplo: No permitir sumar enteros con cadenas sin conversión explícita.
    """
    errores = []
    for variable, tipo, valor in asignaciones:
        if tipo == "int" and not isinstance(valor, int):
            errores.append(f"Error: La variable {variable} esperaba un entero, pero se le asignó {valor}.")
        elif tipo == "float" and not isinstance(valor, float):
            errores.append(f"Error: La variable {variable} esperaba un flotante, pero se le asignó {valor}.")
        elif tipo == "str" and not isinstance(valor, str):
            errores.append(f"Error: La variable {variable} esperaba una cadena, pero se le asignó {valor}.")
    return errores

def verificar_funciones(funciones):
    """
    Valida que las funciones retornen el tipo esperado.
    """
    errores = []
    for funcion, tipo_retorno, valor_retorno in funciones:
        if tipo_retorno == "int" and not isinstance(valor_retorno, int):
            errores.append(f"Error en la función {funcion}: Se esperaba retornar un entero, pero se retornó {valor_retorno}.")
    return errores

def analizador_semantico(asignaciones, funciones):
    """
    Ejecuta todas las verificaciones semánticas en asignaciones y funciones.
    """
    errores = []
    errores.extend(verificar_tipos(asignaciones))
    errores.extend(verificar_funciones(funciones))
    return "\n".join(errores) if errores else "Análisis semántico completado sin errores."
