def largo_elemento (lista, contador):
    if lista == []:
        return contador
    else:
        return largo_elemento (lista [1:], contador + 1)


def sumaMatrices (matriz_1, matriz_2):
    if matriz_1 == [] and matriz_2 == []:
        return []
    elif largo_elemento(matriz_1, 0) != largo_elemento(matriz_2, 0):
        return "Error, la cantidad de los elementos debe ser igual"
    else:
        return sumaMatrices_aux(matriz_1, matriz_2, 0, [])


def sumaMatrices_aux(matriz_1, matriz_2, cont_f, resultado):
    if cont_f == largo_elemento(matriz_1, 0):
        return resultado
    else:
        suma = suma_matrices(matriz_1[cont_f], matriz_2[cont_f], 0)
        return sumaMatrices_aux(matriz_1, matriz_2, cont_f + 1, resultado + [suma])


def suma_matrices(lista_1, lista_2, cont_c):
    if cont_c == largo_elemento(lista_1, 0):
        return []
    else:
        return [lista_1 [cont_c] - lista_2 [cont_c]] + suma_matrices(lista_1, lista_2, cont_c + 1) 