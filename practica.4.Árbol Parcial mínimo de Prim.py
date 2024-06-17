import networkx as nx
import matplotlib.pyplot as plt
import heapq

def prim_mst(graph):
    """
    Función que implementa el algoritmo de Prim para encontrar el MST de un grafo.
    Devuelve el árbol parcial mínimo como un grafo networkx.
    """
    min_spanning_tree = nx.Graph()
    # Seleccionamos un nodo inicial arbitrario (en este caso el primero)
    start_node = list(graph.nodes())[0]
    # Estructura para manejar los bordes candidatos (usamos un heap para obtener el mínimo rápido)
    heap = [(0, start_node, start_node)]  # (peso, nodo de origen, nodo de destino)
    visited = set()

    while heap:
        weight, u, v = heapq.heappop(heap)
        if v not in visited:
            visited.add(v)
            min_spanning_tree.add_edge(u, v, weight=weight)
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (weight['weight'], v, neighbor))

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

# Grafo original
plt.subplot(121)
pos = nx.spring_layout(G)  # Posición de los nodos
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.title('Grafo Original')

# MST resultante
plt.subplot(122)
pos = nx.spring_layout(min_spanning_tree)
nx.draw(min_spanning_tree, pos, with_labels=True, node_color='lightgreen', edge_color='green', font_weight='bold')
nx.draw_networkx_edge_labels(min_spanning_tree, pos, edge_labels={(u, v): d['weight'] for u, v, d in min_spanning_tree.edges(data=True)})
plt.title('Árbol Parcial Mínimo (MST)')

plt.tight_layout()
plt.show()

