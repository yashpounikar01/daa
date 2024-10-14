import sys

def prims_algorithm(graph):
    num_vertices = len(graph)
    selected = [False] * num_vertices
    key = [sys.maxsize] * num_vertices
    parent = [-1] * num_vertices

    key[0] = 0
    parent[0] = -1

    for _ in range(num_vertices):
        min_key = sys.maxsize
        u = 0

        # Find the vertex with the minimum key value
        for v in range(num_vertices):
            if not selected[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        selected[u] = True

        # Update key values of adjacent vertices
        for v in range(num_vertices):
            if graph[u][v] and not selected[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    return parent, key

def print_mst(parent, key):
    print("Edge \tWeight")
    for i in range(1, len(parent)):
        print(f"{parent[i]} - {i} \t{key[i]}")

# Example input graph as an adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

parent, key = prims_algorithm(graph)
print_mst(parent, key)
