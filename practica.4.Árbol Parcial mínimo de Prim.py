"""
Estudiante:Marifer Estrada Rubio 
Registro:21310110 
Carrera:Ingeniería Mecatrónica.
Profesor : Mauricio Alejandro Cabrera Arellano 
Materia:Inteligência Artificial 
"""
import networkx as nx
import matplotlib.pyplot as plt
import heapq

def prim_mst(graph):
    """
    Implementación del algoritmo de Prim para encontrar el Árbol Parcial Mínimo (MST) de un grafo.
    
    Args:
    - graph: Grafo representado como un objeto networkx.Graph
    
    Returns:
    - min_spanning_tree: Árbol parcial mínimo como un objeto networkx.Graph
    """
    min_spanning_tree = nx.Graph()  # Creamos un nuevo grafo para almacenar el MST
    start_node = list(graph.nodes())[0]  # Elegimos un nodo inicial arbitrario (en este caso el primero)
    heap = [(0, start_node, start_node)]  # Utilizamos un heap para manejar los bordes candidatos
    visited = set()  # Conjunto para mantener los nodos visitados

    while heap:
        weight, u, v = heapq.heappop(heap)  # Obtenemos el borde de peso mínimo del heap
        if v not in visited:
            visited.add(v)  # Añadimos el nodo v a los nodos visitados
            min_spanning_tree.add_edge(u, v, weight=weight)  # Añadimos el borde al MST
            # Iteramos sobre los vecinos de v
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (weight['weight'], v, neighbor))  # Añadimos los bordes candidatos al heap

    return min_spanning_tree

# Crear un grafo de ejemplo (puedes modificar este grafo para probar diferentes configuraciones)
G = nx.Graph()
G.add_edges_from([(0, 1, {'weight': 4}), (0, 7, {'weight': 8}), (1, 2, {'weight': 8}),
                  (1, 7, {'weight': 11}), (2, 3, {'weight': 7}), (2, 8, {'weight': 2}),
                  (2, 5, {'weight': 4}), (3, 4, {'weight': 9}), (3, 5, {'weight': 14}),
                  (4, 5, {'weight': 10}), (5, 6, {'weight': 2}), (6, 7, {'weight': 1}),
                  (6, 8, {'weight': 6}), (7, 8, {'weight': 7})])

# Obtener el MST utilizando el algoritmo de Prim
min_spanning_tree = prim_mst(G)

# Dibujar el grafo original y el MST resultante
plt.figure(figsize=(12, 6))

# Dibujar el grafo original
plt.subplot(121)
pos = nx.spring_layout(G)  # Calcular la posición de los nodos usando un layout de spring
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.title('Grafo Original')

# Dibujar el MST resultante
plt.subplot(122)
pos = nx.spring_layout(min_spanning_tree)  # Calcular la posición de los nodos usando un layout de spring
nx.draw(min_spanning_tree, pos, with_labels=True, node_color='lightgreen', edge_color='green', font_weight='bold')
nx.draw_networkx_edge_labels(min_spanning_tree, pos, edge_labels={(u, v): d['weight'] for u, v, d in min_spanning_tree.edges(data=True)})
plt.title('Árbol Parcial Mínimo (MST)')

plt.tight_layout()  # Ajustar el diseño de los subplots para que no se solapen
plt.show()  # Mostrar el gráfico


