def sumarFilas (matriz):
    if isinstance (matriz, list) and (matriz != []):
        return sumarFilas_aux (matriz, [])
    else:
        return "Error, el elemento de entrada no es válido"


def largo_elemento (lista, contador):
    if lista == []:
        return contador
    else:
        return largo_elemento (lista [1:], contador + 1)


def sumarFilas_aux (p_matriz, p_resultado):
    if p_matriz == []:
        return p_resultado
    else:
        sumas = suma_filas (p_matriz [0], 0)
        return sumarFilas_aux (p_matriz [1:], p_resultado + [sumas])


def suma_filas (lista, resultado):
    if lista == []:
        return resultado
    else:
        return suma_filas (lista [1:], resultado + lista [0])