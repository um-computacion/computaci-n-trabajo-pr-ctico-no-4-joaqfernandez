def flatten(elemento):
    resultado = []
    if isinstance(elemento, dict):
        for clave, valor in elemento.items():
            resultado.extend(flatten(clave))
            resultado.extend(flatten(valor))
    elif isinstance(elemento, (list, tuple)):
        for item in elemento:
            resultado.extend(flatten(item))
    else:
        resultado.append(elemento)
    return resultado
