"""
Estudiante:Marifer Estrada Rubio 
Registro:21310110 
Carrera:Ingeniería Mecatrónica.
Profesor : Mauricio Alejandro Cabrera Arellano 
Materia:Inteligência Artificial 
"""
def natural_merge_sort(arr):
    # Función para realizar el ordenamiento por mezcla natural
    def merge(left, right):
        # Función auxiliar para fusionar dos secuencias ordenadas
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def get_runs(sequence):
        # Función auxiliar para obtener las secuencias ordenadas (runs) del arreglo
        runs = []
        run = [sequence[0]]
        for i in range(1, len(sequence)):
            if sequence[i] >= sequence[i - 1]:
                run.append(sequence[i])
            else:
                runs.append(run)
                run = [sequence[i]]
        runs.append(run)
        return runs

    # Obtener las secuencias ordenadas iniciales (runs)
    sorted_runs = get_runs(arr)
    # Fusionar las secuencias hasta obtener un solo arreglo ordenado
    while len(sorted_runs) > 1:
        next_runs = []
        for i in range(0, len(sorted_runs), 2):
            if i + 1 < len(sorted_runs):
                merged_run = merge(sorted_runs[i], sorted_runs[i + 1])
                next_runs.append(merged_run)
            else:
                next_runs.append(sorted_runs[i])
        sorted_runs = next_runs
    return sorted_runs[0]

# Ejemplo de uso del algoritmo de mezcla natural (Natural Merging)
arr = [5, 9, 3, 1, 2, 8, 7, 6]
sorted_arr = natural_merge_sort(arr)
print("El arreglo ordenado es:", sorted_arr)
