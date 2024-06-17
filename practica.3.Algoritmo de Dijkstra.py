"""
Estudiante:Marifer Estrada Rubio 
Registro:21310110 
Carrera:Ingeniería Mecatrónica.
Profesor : Mauricio Alejandro Cabrera Arellano 
Materia:Inteligência Artificial 
"""
import matplotlib.pyplot as plt
import networkx as nx

# Definimos una función para el algoritmo de Dijkstra
def dijkstra(graph, start):
    # Inicializamos las distancias con infinito y el camino con el nodo de inicio
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    previous_vertices = {vertex: None for vertex in graph}
    vertices = graph.copy()

    while vertices:
        # Seleccionamos el vértice con la distancia más corta no visitado
        current_vertex = min(vertices, key=lambda vertex: shortest_paths[vertex])
        vertices.pop(current_vertex)

        # Revisamos los vecinos del vértice actual
        for neighbour, weight in graph[current_vertex].items():
            alternate_route = shortest_paths[current_vertex] + weight
            # Si encontramos una ruta más corta, actualizamos la distancia y el camino
            if alternate_route < shortest_paths[neighbour]:
                shortest_paths[neighbour] = alternate_route
                previous_vertices[neighbour] = current_vertex

    return previous_vertices, shortest_paths

# Creamos un grafo de ejemplo
graph_example = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Aplicamos Dijkstra al grafo desde el nodo 'A'
previous_vertices, shortest_paths = dijkstra(graph_example, 'A')

# Creamos un grafo dirigido con NetworkX para visualizarlo
G = nx.DiGraph()
for vertex, edges in graph_example.items():
    for neighbour, weight in edges.items():
        G.add_edge(vertex, neighbour, weight=weight)

# Dibujamos el grafo con NetworkX y Matplotlib
pos = nx.spring_layout(G) # Posicionamiento automático de los nodos
nx.draw(G, pos, with_labels=True) # Dibujamos los nodos y etiquetas
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels) # Mostramos los pesos

# Mostramos el gráfico
plt.show()

