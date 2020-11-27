def largo_elemento (lista, contador):
    if lista == []:
        return contador
    else:
        return largo_elemento (lista [1:], contador + 1)


def multiplicarMatrices(matriz_1, matriz_2):
    if isinstance(matriz_1, list) and (matriz_1 != []) and isinstance(matriz_2, list) and (matriz_2 != []):
        if largo_elemento(matriz_1[0], 0) != largo_elemento(matriz_2, 0):
            return "Error, orden no adecuado"
        else:
            return multiplicarMatrices_aux(matriz_1, matriz_2, 0, [])
    else:
        return "Error, los elemento de entrada deben ser listas y no deben estar vacías"


def multiplicarMatrices_aux(matriz_1, matriz_2, contador, resultado):
    if contador == largo_elemento(matriz_1, 0):
        return resultado
    else:
        resultado += [multiplicarFilaMatriz(matriz_1[contador], matriz_2)]
        return multiplicarMatrices_aux(matriz_1, matriz_2, contador + 1, resultado)


def obtenerColumna(matriz, indice, cont_f):
    if cont_f == largo_elemento(matriz, 0):
        return []
    else:
        return [matriz[cont_f][indice]] + obtenerColumna(matriz, indice, cont_f + 1)


def multiplicarFilaColumna(fila, columna, contador):
    if contador == largo_elemento(fila, 0) and contador == largo_elemento(columna, 0):
        return 0
    else:
        return fila[contador] * columna[contador] + multiplicarFilaColumna(fila, columna, contador + 1)


def multiplicarFilaMatriz(fila, matriz):
    return multiplicarFilaMatriz_aux(fila, matriz, 0, largo_elemento(matriz[0], 0), [])


def multiplicarFilaMatriz_aux(fila, matriz, columna_actual, total_columnas, resultado):
    if columna_actual == total_columnas:
        return resultado
    else:
        columna = obtenerColumna(matriz, columna_actual, 0)
        resultado += [multiplicarFilaColumna(fila, columna, 0)]
        return multiplicarFilaMatriz_aux(fila, matriz, columna_actual + 1, total_columnas, resultado)