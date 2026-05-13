def dijkstra_simple(graph, start):
    n = len(graph)

    dist = [9999] * n
    visited = [False] * n

    dist[start] = 0

    for _ in range(n):
        min_dist = 9999
        u = -1

        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        visited[u] = True

        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    print("Shortest Distance from source:", dist)


# graph (adjacency matrix)
graph = [
    [0, 4, 1, 0, 0],
    [4, 0, 2, 5, 0],
    [1, 2, 0, 8, 10],
    [0, 5, 8, 0, 2],
    [0, 0, 10, 2, 0]
]

dijkstra_simple(graph, 0)