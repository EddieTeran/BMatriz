"""Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.

Escribe un programa que incluya una matriz bidimensional
(puede ser una matriz pequeña de 3x3) con valores numéricos.

Implementa una función que realice una búsqueda en la matriz para
encontrar un valor específico que definas.

Muestra un mensaje que indique si el valor se encontró o no,
y muestra su posición en la matriz si se encontró."""
# creamos la matrix  3x3 con números enteros
arr_matriz3x3 = [
    [10, 11, 12],
    [14, 13, 12],
    [16, 15, 14]
]
# Imprimimos la matrix
for (x) in arr_matriz3x3:
    print(x)
# Búsqueda de un valor  en la matriz
valor_buscado = 15
if any(valor_buscado in fila for fila in arr_matriz3x3):
    print(f"Se encontró {valor_buscado} en la matriz.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")
fila_encontrada = -1
columna_encontrada = -1
for fila in range(len(arr_matriz3x3)):
    for columna in range(len(arr_matriz3x3[fila])):
        if arr_matriz3x3[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break  # Detener la búsqueda una vez que se encuentra el valor
    if fila_encontrada != -1:
        break  # Salir del bucle exterior si se encuentra el valor

# Verificar si se encontró el valor y mostrar la posición
if fila_encontrada != -1:
    print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")
