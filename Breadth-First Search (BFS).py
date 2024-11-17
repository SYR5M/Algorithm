import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
graph = nx.Graph()
edges = [
    ('A', 'B', 1), ('A', 'C', 3), ('B', 'D', 4),
    ('C', 'D', 2), ('C', 'E', 6), ('D', 'E', 1)
]
graph.add_weighted_edges_from(edges)

# Define positions for visualization
pos = nx.spring_layout(graph)

# BFS Algorithm
def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
        current, path = queue.pop(0)
        if current == goal:
            return path
        visited.add(current)
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

# Execute BFS
path = bfs(graph, 'A', 'E')

# Visualize the graph and the path
plt.figure(figsize=(8, 6))
nx.draw(graph, pos, with_labels=True, node_color='lightgreen', node_size=1000)
nx.draw_networkx_edge_labels(graph, pos, edge_labels={(u, v): d['weight'] for u, v, d in graph.edges(data=True)})
nx.draw_networkx_edges(graph, pos, edgelist=graph.edges, edge_color='black')
if path:
    edge_path = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(graph, pos, edgelist=edge_path, edge_color='blue', width=2)
    plt.title(f"BFS Path: {' -> '.join(path)}\nReason: Explores the shortest path by the number of edges, ignoring weights")
    print(f"Path found by BFS: {' -> '.join(path)}")
else:
    print("No path found by BFS")
plt.show()
