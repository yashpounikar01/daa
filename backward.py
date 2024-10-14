class MultistageGraph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, cost):
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append((u, cost))  # Reverse the direction for backward approach

    def find_shortest_path(self, start, end):
        # Initialize the distance dictionary
        dist = {node: float('inf') for node in self.graph}
        dist[end] = 0  # Start from the end vertex

        # Using dynamic programming to find the shortest path
        for i in range(len(self.graph)):
            for u in self.graph:
                if dist[u] != float('inf'):
                    for v, cost in self.graph[u]:
                        if dist.get(v, float('inf')) > dist[u] + cost:
                            dist[v] = dist[u] + cost

        # Check if the start vertex is reachable
        return dist.get(start, float('inf'))

def main():
    graph = MultistageGraph()

    print("Enter edges in the format 'start_vertex end_vertex cost'. Type 'done' to finish:")
    
    while True:
        user_input = input()
        if user_input.lower() == 'done':
            break
        try:
            u, v, cost = user_input.split()
            cost = int(cost)
            graph.add_edge(u, v, cost)
        except ValueError:
            print("Invalid input. Please enter in the correct format.")

    start = input("Enter the start vertex: ")
    end = input("Enter the end vertex: ")
    
    shortest_path_cost = graph.find_shortest_path(start, end)

    if shortest_path_cost == float('inf'):
        print(f"No path found from {start} to {end}.")
    else:
        print(f"The shortest path cost from {start} to {end} is: {shortest_path_cost}")

if __name__ == "__main__":
    main()
