"""
2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro, 
un carácter como segundo y otro carácter como tercero, la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero 
y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena
"""

def reemplazarCaracteres(cadena_caracteres:str, caracter_a_reemplazar:str, reemplazo_caracter:str) -> str:
    """Reemplaza caracteres de una cadena de strings
    Args:
        cadena_caracteres (str): la cadena a la cual le queremos reemplazar un caracter
        caracter_a_reemplazar (str): el caracter que queremos reemplazar
        reemplazo_caracter (str): el caracter que va a reemplazar al anterior
    Returns:
        str: la cadena con el o los caracteres cambiados
    """
    cantidad_reemplazos = cadena_caracteres.count(caracter_a_reemplazar)
    cadena_modificada = cadena_caracteres.replace(caracter_a_reemplazar, reemplazo_caracter)
    return cadena_modificada, cantidad_reemplazos

print(reemplazarCaracteres())