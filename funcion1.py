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