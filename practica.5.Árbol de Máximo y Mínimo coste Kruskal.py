import matplotlib.pyplot as plt
import networkx as nx

# Clase para representar una estructura de unión-búsqueda
class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

# Función para aplicar el algoritmo de Kruskal
def kruskal(graph):
    # Ordena las aristas por su peso
    edges_sorted = sorted(graph['edges'], key=lambda edge: edge[2])
    uf = UnionFind(graph['vertices'])
    mst = []

    # Itera sobre las aristas ordenadas
    for edge in edges_sorted:
        u, v, weight = edge
        # Si u y v no están conectados, añade la arista al árbol de expansión mínimo
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append(edge)

    return mst

# Ejemplo de uso del algoritmo de Kruskal
graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
    'edges': [
        ('A', 'B', 4),
        ('A', 'F', 2),
        ('B', 'C', 6),
        ('B', 'F', 5),
        ('C', 'D', 3),
        ('C', 'E', 1),
        ('D', 'E', 8),
        ('E', 'F', 7),
    ]
}

mst = kruskal(graph)

# Crear un gráfico con NetworkX y dibujar el árbol de expansión mínimo
G = nx.Graph()
for edge in graph['edges']:
    G.add_edge(edge[0], edge[1], weight=edge[2])

pos = nx.spring_layout(G)  # Posicionamiento de los nodos del gráfico
nx.draw(G, pos, with_labels=True)  # Dibuja los nodos y las etiquetas

# Dibuja las aristas del árbol de expansión mínimo con un color diferente
mst_edges = [(u, v) for u, v, _ in mst]
nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='r')

plt.show()  # Muestra el gráfico

# Para obtener el árbol de expansión de costo máximo,
# simplemente cambia la línea que ordena las aristas a:
# edges_sorted = sorted(graph['edges'], key=lambda edge: edge[2], reverse=True)


