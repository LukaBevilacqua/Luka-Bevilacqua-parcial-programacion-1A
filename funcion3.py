def ordenarCaracteres(cadena_caracteres:str)->str:
    """Ordena una cadena de caracteres de manera ascendente dentro de la cadena
    Args:
        cadena_caracteres (str): La cadena de caracteres que quiere ordenar
    Returns:
        str: La cadena de caracteres ordenada
    """
    flag_swap = True
    contador = 1
    while flag_swap:
        flag_swap = False
        for i in range(len(cadena_caracteres)-contador):
            if cadena_caracteres[i] > cadena_caracteres[i + 1]:
                aux = cadena_caracteres[i]
                cadena_caracteres[i] = cadena_caracteres[i + 1]
                cadena_caracteres[i + 1] = aux
                flag_swap = True
    return cadena_caracteres

print(ordenarCaracteres("algoritmo"))



