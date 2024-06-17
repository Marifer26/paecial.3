"""
Estudiante:Marifer Estrada Rubio 
Registro:21310110 
Carrera:Ingeniería Mecatrónica.
Profesor : Mauricio Alejandro Cabrera Arellano 
Materia:Inteligência Artificial 
"""
# Función auxiliar para hacer el conteo de los elementos según el dígito representado por exp
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Almacena el conteo de ocurrencias en count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Cambia count[i] para que contenga la posición actual de este dígito en output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construye el arreglo de salida
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copia los elementos de output[] a arr[], para que arr[] ahora contenga números ordenados según el dígito actual
    for i in range(n):
        arr[i] = output[i]

# Función principal para realizar el Radix Sort
def radix_sort(arr):
    # Encuentra el número máximo para saber la cantidad de dígitos
    max1 = max(arr)

    # Hace un counting sort para cada dígito. En lugar de pasar el dígito número, exp es pasado. exp es 10^i donde i es el número de dígito actual
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Ejemplo de uso del algoritmo Radix Sort
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("El arreglo ordenado es:", arr)
