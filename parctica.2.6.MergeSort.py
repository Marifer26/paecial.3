"""
Estudiante:Marifer Estrada Rubio 
Registro:21310110 
Carrera:Ingeniería Mecatrónica.
Profesor : Mauricio Alejandro Cabrera Arellano 
Materia:Inteligência Artificial 
"""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encuentra el punto medio del arreglo
        L = arr[:mid]  # Divide los elementos en dos mitades
        R = arr[mid:]

        merge_sort(L)  # Ordena la primera mitad
        merge_sort(R)  # Ordena la segunda mitad

        i = j = k = 0

        # Copia los datos a los arreglos temporales L[] y R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Verifica si quedan elementos en L[]
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Verifica si quedan elementos en R[]
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Ejemplo de uso del algoritmo de MergeSort
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("El arreglo ordenado es:", arr)
