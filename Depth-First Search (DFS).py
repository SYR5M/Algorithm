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

# DFS Algorithm
def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    if start == goal:
        return path
    visited.add(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if result:
                return result
    return None

# Execute DFS
path = dfs(graph, 'A', 'E')

# Visualize the graph and the path
plt.figure(figsize=(8, 6))
nx.draw(graph, pos, with_labels=True, node_color='pink', node_size=1000)
nx.draw_networkx_edge_labels(graph, pos, edge_labels={(u, v): d['weight'] for u, v, d in graph.edges(data=True)})
nx.draw_networkx_edges(graph, pos, edgelist=graph.edges, edge_color='black')
if path:
    edge_path = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(graph, pos, edgelist=edge_path, edge_color='purple', width=2)
    plt.title(f"DFS Path: {' -> '.join(path)}\nReason: Explores deeply first; path may not be optimal")
    print(f"Path found by DFS: {' -> '.join(path)}")
else:
    print("No path found by DFS")
plt.show()
