"""
Estudiante:Marifer Estrada Rubio 
Registro:21310110 
Carrera:Ingeniería Mecatrónica.
Profesor : Mauricio Alejandro Cabrera Arellano 
Materia:Inteligência Artificial 
"""
def quick_sort(arr):
    # Función auxiliar para realizar el ordenamiento
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Ejemplo de uso del algoritmo de QuickSort
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("El arreglo ordenado es:", sorted_arr)
