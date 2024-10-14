import sys

def floyd_warshall(graph, n):
    # Initialize the distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Set the distance from each node to itself to 0
    for i in range(n):
        dist[i][i] = 0
    
    # Set initial distances based on the input graph
    for u in range(n):
        for v in range(n):
            if graph[u][v] != float('inf'):
                dist[u][v] = graph[u][v]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def print_solution(dist):
    n = len(dist)
    print("Shortest distances between every pair of vertices:")
    for i in range(n):
        for j in range(n):
            if dist[i][j] == float('inf'):
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
        print()

if __name__ == "__main__":
    # Input number of vertices
    n = int(input("Enter the number of vertices: "))
    
    # Initialize graph with infinities
    graph = [[float('inf')] * n for _ in range(n)]
    
    print("Enter the adjacency matrix (use space-separated values):")
    
    # Input adjacency matrix
    for i in range(n):
        row = input(f"Enter the row {i + 1}: ").split()
        for j in range(n):
            value = row[j]
            if value.lower() == 'inf':
                graph[i][j] = float('inf')
            else:
                graph[i][j] = int(value)
    
    # Run Floyd-Warshall algorithm
    dist = floyd_warshall(graph, n)
    
    # Print the result
    print_solution(dist)
