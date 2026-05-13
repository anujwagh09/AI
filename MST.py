def mst(graph):
    n = len(graph)
    visited = [False] * n

    visited[0] = True  # start from node 0
    print("Edge : Weight")

    for _ in range(n - 1):
        min_weight = 9999
        x = 0
        y = 0

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j] != 0:
                        if graph[i][j] < min_weight:
                            min_weight = graph[i][j]
                            x = i
                            y = j

        print(x, "-", y, ":", graph[x][y])
        visited[y] = True


# graph (adjacency matrix)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

mst(graph)