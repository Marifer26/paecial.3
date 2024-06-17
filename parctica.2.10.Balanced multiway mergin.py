"""
Estudiante:Marifer Estrada Rubio 
Registro:21310110 
Carrera:Ingeniería Mecatrónica.
Profesor : Mauricio Alejandro Cabrera Arellano 
Materia:Inteligência Artificial 
"""
import heapq

def balanced_multiway_merge(*sequences):
    # Función para realizar la mezcla equilibrada de múltiples secuencias
    # Utiliza una cola de prioridad (heap) para mantener el orden mientras se fusionan las secuencias
    min_heap = []
    for index, seq in enumerate(sequences):
        iterator = iter(seq)
        first_element = next(iterator, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, index, iterator))

    result = []
    while min_heap:
        value, index, iterator = heapq.heappop(min_heap)
        result.append(value)
        next_element = next(iterator, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, index, iterator))

    return result

# Ejemplo de uso del algoritmo de mezcla equilibrada de múltiples vías
seq1 = [1, 4, 7]
seq2 = [2, 5, 8]
seq3 = [3, 6, 9]
sorted_arr = balanced_multiway_merge(seq1, seq2, seq3)
print("El arreglo ordenado es:", sorted_arr)
