def bubble_sort(arr):
    n = len(arr)
    # Recorre todos los elementos del arreglo
    for i in range(n):
        # Los últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Recorre el arreglo de 0 a n-i-1
            # Intercambia si el elemento encontrado es mayor que el siguiente
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ejemplo de uso del algoritmo de ordenamiento por intercambio (Bubble Sort)
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("El arreglo ordenado es:", arr)
