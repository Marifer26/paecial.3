"""
Estudiante:Marifer Estrada Rubio 
Registro:21310110 
Carrera:Ingeniería Mecatrónica.
Profesor : Mauricio Alejandro Cabrera Arellano 
Materia:Inteligência Artificial 
"""
class Node:
    # Clase para crear nodos del árbol
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    # Función para insertar un nodo en el árbol
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root, sorted_list):
    # Función para realizar el recorrido en orden del árbol y obtener el arreglo ordenado
    if root:
        inorder_traversal(root.left, sorted_list)
        sorted_list.append(root.val)
        inorder_traversal(root.right, sorted_list)

def tree_sort(arr):
    # Función principal para realizar el ordenamiento de árbol
    if len(arr) == 0:
        return []
    
    root = Node(arr[0])
    
    # Inserta todos los elementos del arreglo en el árbol
    for i in range(1, len(arr)):
        insert(root, arr[i])
    
    sorted_list = []
    # Realiza el recorrido en orden para obtener el arreglo ordenado
    inorder_traversal(root, sorted_list)
    
    return sorted_list

# Ejemplo de uso del algoritmo de ordenamiento de árbol (Tree Sort)
arr = [5, 4, 7, 2, 11]
sorted_arr = tree_sort(arr)
print("El arreglo ordenado es:", sorted_arr)
