"""
Estudiante:Marifer Estrada Rubio 
Registro:21310110 
Carrera:Ingeniería Mecatrónica.
Profesor : Mauricio Alejandro Cabrera Arellano 
Materia:Inteligência Artificial 
"""
import heapq
from itertools import cycle

def distribute_data(data, num_files):
    """
    Distribuye los datos en num_files archivos (listas en este caso).
    """
    files = [[] for _ in range(num_files)]  # Crear listas vacías para cada archivo
    data.sort()  # Primero ordenamos los datos para simplificar la distribución inicial
    for idx, value in enumerate(data):
        files[idx % num_files].append(value)  # Distribuir datos en las listas de manera equitativa
    return files

def merge_files(files):
    """
    Mezcla las listas (archivos) utilizando un heap para obtener una única lista ordenada.
    """
    min_heap = []
    # Insertar el primer elemento de cada archivo en el heap
    for file_idx, file in enumerate(files):
        if file:
            heapq.heappush(min_heap, (file[0], file_idx, 0))
    
    result = []
    while min_heap:
        value, file_idx, item_idx = heapq.heappop(min_heap)  # Obtener el elemento más pequeño
        result.append(value)  # Añadirlo a la lista resultado
        if item_idx + 1 < len(files[file_idx]):  # Si hay más elementos en el archivo actual
            next_item = files[file_idx][item_idx + 1]  # Obtener el siguiente elemento
            heapq.heappush(min_heap, (next_item, file_idx, item_idx + 1))  # Insertar en el heap
    
    return result

def polyphase_sort(data, num_files=3):
    """
    Realiza el ordenamiento polifase en los datos proporcionados.
    """
    # Paso 1: Distribuir los datos en num_files archivos
    files = distribute_data(data, num_files)
    print("Distribución inicial de datos en archivos:", files)

    # Paso 2: Intercalar los archivos hasta obtener un único archivo ordenado
    while len(files) > 1:
        # Intercalamos los archivos en pares
        next_files = []
        for i in range(0, len(files), 2):
            if i + 1 < len(files):  # Si hay un par para mezclar
                merged_file = merge_files([files[i], files[i + 1]])  # Mezclar los dos archivos
            else:  # Si hay un archivo sin par, se pasa tal cual
                merged_file = files[i]
            next_files.append(merged_file)
        files = next_files  # Actualizar la lista de archivos con los archivos mezclados
        print("Archivos después de una fase de intercalado:", files)
    
    # El resultado final es el archivo ordenado
    return files[0] if files else []

# Ejemplo de uso
data = [7, 5, 2, 8, 4, 1, 3, 6, 9, 0]  # Datos desordenados
sorted_data = polyphase_sort(data)  # Ordenar los datos
print("Datos ordenados:", sorted_data)  # Imprimir los datos ordenados