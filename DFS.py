
def dfs(matrix, vertex, visited):
    print(vertex, end=' ')
    visited[vertex] = True

    for i in range(len(matrix)):
        if matrix[vertex][i] == 1 and not visited[i]:
            dfs(matrix, i, visited)

n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

start = int(input("Enter starting vertex (0 to {}): ".format(n-1)))

visited = [False] * n

print("\nDFS Traversal:")
dfs(matrix, start, visited)