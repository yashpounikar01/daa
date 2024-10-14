def is_safe(graph, color, vertex, c):
    # Check if the current color assignment is safe for vertex
    for neighbor in graph[vertex]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, vertex):
    # If all vertices are assigned a color then return true
    if vertex == len(graph):
        return True

    # Try different colors for vertex
    for c in range(1, m + 1):
        if is_safe(graph, color, vertex, c):
            color[vertex] = c  # Assign color c to vertex
            if graph_coloring_util(graph, m, color, vertex + 1):
                return True
            color[vertex] = 0  # Backtrack

    return False

def graph_coloring(graph, m):
    color = [0] * len(graph)  # Initialize color assignments
    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist")
        return False
    
    print("Solution exists: Following are the assigned colors:")
    for vertex in range(len(graph)):
        print(f"Vertex {vertex}: Color {color[vertex]}")
    return True

def main():
    n = int(input("Enter the number of vertices: "))
    graph = [[] for _ in range(n)]

    print("Enter the edges in the format 'u v' (one edge per line). Type 'done' to finish:")
    while True:
        edge = input()
        if edge.lower() == 'done':
            break
        u, v = map(int, edge.split())
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph

    m = int(input("Enter the number of colors: "))
    graph_coloring(graph, m)

if __name__ == "__main__":
    main()
