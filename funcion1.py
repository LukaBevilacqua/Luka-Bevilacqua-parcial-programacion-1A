"""
1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto 
y devuelva el valor del producto con un aumento del 5%. 
Realizar la llamada desde el main.
"""

def aplicarAumento(valor_producto:float)->float:
    """ Aplica un aumento al valor de un producto
    Args:
        valor_producto (float): El valor del producto al que desea aplicar el aumento
    Returns:
        float: El valor con el aumento aplicado
    """
    porcentaje = 5
    valor_aumento = (valor_producto * porcentaje)/100
    valor_producto_aumentado = valor_producto + valor_aumento
    return valor_producto_aumentado

print(aplicarAumento())