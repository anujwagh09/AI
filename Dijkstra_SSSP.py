# Dijkstra - Greedy Approach

def dijkstra(graph, start):
    n = len(graph)
    visited = [False] * n
    distance = [9999] * n
    
    distance[start] = 0

    for _ in range(n):
        min_dist = 9999
        u = -1

        # Find the vertex with minimum distance
        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                u = i

        visited[u] = True

        # Update distances of adjacent vertices
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]

    print("Shortest distances:", distance)


# Graph (Adjacency Matrix)
graph = [
    [0, 2, 0, 1],
    [2, 0, 3, 2],
    [0, 3, 0, 4],
    [1, 2, 4, 0]
]

# Function call
dijkstra(graph, 0)