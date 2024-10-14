import sys

def tsp(graph, start_vertex):
    n = len(graph)
    memo = {}

    def dp(mask, pos):
        if mask == (1 << n) - 1:
            return graph[pos][start_vertex]  # Return to starting point

        if (mask, pos) in memo:
            return memo[(mask, pos)]

        ans = sys.maxsize

        for city in range(n):
            if mask & (1 << city) == 0:  # If city is not visited
                new_ans = graph[pos][city] + dp(mask | (1 << city), city)
                ans = min(ans, new_ans)

        memo[(mask, pos)] = ans
        return ans

    return dp(1 << start_vertex, start_vertex)

def main():
    print("Enter the distance matrix row by row (type 'done' when finished):")
    graph = []

    while True:
        line = input().strip()
        if line.lower() == "done":
            break
        # Convert the input line into a list of integers and append to the graph
        row = list(map(int, line.split()))
        graph.append(row)

    print("Enter the start vertex (0 to {}):".format(len(graph) - 1))
    start_vertex = int(input().strip())

    result = tsp(graph, start_vertex)
    print(f"The minimum cost of visiting all cities starting from vertex {start_vertex} is: {result}")

if __name__ == "__main__":
    main()
