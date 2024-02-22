"""Ordenación de Arreglo Multidimensional

Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.

Escribe un programa que incluya una matriz bidimensional con valores numéricos
 (puede ser una matriz pequeña de 3x3).

Implementa una función que ordene una fila específica de la matriz en orden ascendente
 utilizando un algoritmo de ordenación de tu elección (por ejemplo, Bubble Sort o QuickSort).

Muestra la matriz original y la matriz con la fila ordenada"""

   # Matriz bidimensional
arr_matriz = [[11, 15, 22],
              [14, 35, 26],
              [70, 78, 69]
                            ]

for (x) in arr_matriz:
    print(x)
   # Fila a ordenar
fila_a_ordenar = 1

   # Función de ordenación Bubble Sort
def bubble_sort(fila):
    for i in range(len(fila) - 1):
        for j in range(len(fila) - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

# Llamada a la función de ordenación
bubble_sort(arr_matriz[fila_a_ordenar])
print("")
# Impresión de la matriz ordenada
print("Impresión de la matriz ordenada")
for fila in arr_matriz:
    print(fila)
