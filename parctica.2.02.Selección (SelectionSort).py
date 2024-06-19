"""
Estudiante:Marifer Estrada Rubio 
Registro:21310110 
Carrera:Ingeniería Mecatrónica.
Profesor : Mauricio Alejandro Cabrera Arellano 
Materia:Inteligência Artificial 
"""
def selection_sort(arr):
    # Recorre todos los elementos del arreglo
    for i in range(len(arr)):
        # Encuentra el mínimo en el resto del arreglo
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        # Intercambia el mínimo encontrado con el primer elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Ejemplo de uso del algoritmo de ordenamiento por selección
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("El arreglo ordenado es:", arr)
