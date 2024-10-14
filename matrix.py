def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]  # s[i][j] stores the index of the split
    
    for length in range(2, n + 1):  # Length of the chain
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k  # Record the index of the split

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i + 1}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

def main():
    print("Enter the number of matrices:")
    n = int(input().strip())
    
    print("Enter the dimensions of matrices (as a space-separated list):")
    dimensions = list(map(int, input().strip().split()))
    
    if len(dimensions) != n + 1:
        print("Error: Number of dimensions should be one more than the number of matrices.")
        return
    
    m, s = matrix_chain_order(dimensions)
    
    print(f"The minimum number of multiplications is: {m[0][n - 1]}")
    print("Optimal parenthesization is: ", end="")
    print_optimal_parens(s, 0, n - 1)
    print()  # For a new line

if __name__ == "__main__":
    main()
