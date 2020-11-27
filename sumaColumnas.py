def largo_elemento (lista, contador):
    if lista == []:
        return contador
    else:
        return largo_elemento (lista [1:], contador + 1)

        
def sumar_columnas (matriz):
    if isinstance (matriz, list) and (matriz != []):
        return sumar_columnas_aux (matriz, 0, 0, 0, [])
    else:
        return "Error, el elemento de entrada es inválido"

    
def sumar_columnas_aux (matriz, cont_f, cont_c, suma_col, resultado):
    if cont_c == largo_elemento (matriz [0], 0):
        return resultado
    if cont_f == largo_elemento (matriz, 0):
        return sumar_columnas_aux (matriz, 0, cont_c + 1, 0, resultado + [suma_col])
    else:
        suma_col += matriz[cont_f][cont_c]
        return sumar_columnas_aux (matriz, cont_f + 1, cont_c, suma_col, resultado)