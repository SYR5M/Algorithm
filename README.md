Pathfinding Algorithms: A*, BFS, and DFS
This project explores three fundamental pathfinding algorithms—A*, Breadth-First Search (BFS), and Depth-First Search (DFS)—by applying them to the same graph and analyzing their behavior, results, and use cases.

Features
A*:

Finds the optimal path based on actual and estimated costs.
Uses 
𝑓
(
𝑛
)
=
𝑔
(
𝑛
)
+
ℎ
(
𝑛
)
f(n)=g(n)+h(n), balancing path cost and heuristic.
Guarantees the shortest path for weighted graphs.
BFS:

Explores the graph level by level to find the shortest path by the number of edges.
Ignores edge weights, making it ideal for unweighted graphs.
DFS:

Dives deep into one path before backtracking, exploring all possibilities.
Does not guarantee the shortest path but is great for exhaustive searches.
How It Works
Each algorithm is applied to the same graph.
The graph is visualized using Python libraries NetworkX and Matplotlib.
Results are displayed both as terminal outputs (paths and costs) and visually on a graph.

Requirements
Python 3.x

Libraries:

networkx

matplotlib

Install required libraries using:

bash
Copy code

pip install networkx matplotlib

Usage
Run the script to see the algorithms in action:

bash
Copy code

python pathfinding_algorithms.py

Outputs include:

The path found by each algorithm.
Graph visualizations with highlighted paths, edge weights, and reasoning.
Use Cases

A*: GPS navigation, logistics, and weighted graphs.
BFS: Social networks, unweighted mazes, and shortest path by edges.
DFS: Puzzle-solving, cycle detection, and graph traversal.

Example Outputs

A*:
Path: A -> B -> D -> E
Total Cost: 6

BFS:
Path: A -> C -> E

DFS:
Path: A -> B -> D -> C -> E

![BFS](https://github.com/user-attachments/assets/a60bed08-4aff-452e-88df-88e1b116cc9e)
![Astar](https://github.com/user-attachments/assets/16cf6a9d-6811-4d74-817c-b3a2d5bdcfce)
![DFS](https://github.com/user-attachments/assets/d6222d4f-dff7-4396-a016-ad0e95aa8821)
