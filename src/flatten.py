def flatten(lista):
    resultado = []

    for i in range():
        if isinstance(i, list): #isinstance(i, list) es una función que verifica si i es una lista
            resultado.extend(lista(i))
        else:
            resultado.append(i)
    return resultado
