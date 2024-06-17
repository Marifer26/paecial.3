"""
Estudiante:Marifer Estrada Rubio 
Registro:21310110 
Carrera:Ingeniería Mecatrónica.
Profesor : Mauricio Alejandro Cabrera Arellano 
Materia:Inteligência Artificial 
"""
def merge(arr1, arr2):
    # Fusiona dos arreglos ordenados en un solo arreglo ordenado
    sorted_arr = []
    i = j = 0

    # Recorre ambos arreglos y agrega el menor elemento al arreglo fusionado
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    # Agrega los elementos restantes del primer arreglo si los hay
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1

    # Agrega los elementos restantes del segundo arreglo si los hay
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr

# Ejemplo de uso del algoritmo de mezcla directa (Straight Merging)
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
sorted_arr = merge(arr1, arr2)
print("El arreglo ordenado es:", sorted_arr)
