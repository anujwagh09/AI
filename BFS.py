from collections import deque

def bfs(matrix, start):
    visited = [False] * len(matrix)
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for i in range(len(matrix)):
            if matrix[vertex][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)


n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

start = int(input("Enter starting vertex (0 to {}): ".format(n-1)))

print("\nBFS Traversal:")
bfs(matrix, start)