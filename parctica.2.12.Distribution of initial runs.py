"""
Estudiante:Marifer Estrada Rubio 
Registro:21310110 
Carrera:Ingeniería Mecatrónica.
Profesor : Mauricio Alejandro Cabrera Arellano 
Materia:Inteligência Artificial 
"""
def distribution_of_initial_runs(arr):
    # Función para distribuir las secuencias iniciales (runs) de un arreglo
    runs = []
    new_run = [arr[0]]
    
    # Iterar sobre el arreglo para construir las secuencias
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            # Si el elemento actual es mayor o igual al anterior, sigue la secuencia
            new_run.append(arr[i])
        else:
            # Si no, empieza una nueva secuencia
            runs.append(new_run)
            new_run = [arr[i]]
    
    # Añadir la última secuencia si existe
    if new_run:
        runs.append(new_run)
    
    return runs

# Ejemplo de uso de la función
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
initial_runs = distribution_of_initial_runs(arr)
print("Las secuencias iniciales son:", initial_runs)
