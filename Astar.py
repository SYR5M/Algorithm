import networkx as nx
import matplotlib.pyplot as plt
import heapq

def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph.nodes}
    f_score[start] = heuristic(start, goal)

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], g_score[goal]

        for neighbor in graph.neighbors(current):
            tentative_g_score = g_score[current] + graph[current][neighbor]['weight']
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None, None

# Define the graph
graph = nx.Graph()
edges = [
    ('A', 'B', 1), ('A', 'C', 3), ('B', 'D', 4),
    ('C', 'D', 2), ('C', 'E', 6), ('D', 'E', 1)
]
graph.add_weighted_edges_from(edges)

# Heuristic function (here, all are zero for simplicity)
heuristic = lambda x, y: 0

# Run A*
path, cost = a_star(graph, 'A', 'E', heuristic)

# Visualize the graph and path
pos = nx.spring_layout(graph)
plt.figure(figsize=(8, 6))
nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=1000)
nx.draw_networkx_edge_labels(graph, pos, edge_labels={(u, v): d['weight'] for u, v, d in graph.edges(data=True)})
nx.draw_networkx_edges(graph, pos, edgelist=graph.edges, edge_color='black')
if path:
    edge_path = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(graph, pos, edgelist=edge_path, edge_color='red', width=2)
    plt.title(f"A* Path: {' -> '.join(path)}\nCost: {cost}\nReason: The path minimizes total cost (g + h)")
    print(f"Path found by A*: {' -> '.join(path)}")
    print(f"Total cost: {cost}")
else:
    print("No path found by A*")
plt.show()
