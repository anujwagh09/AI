# Kruskal's Algorithm (Greedy)

def kruskal(vertices, edges):
    # Sort edges based on weight
    edges.sort(key=lambda x: x[2])

    # Initialize parent dictionary
    parent = {v: v for v in vertices}

    # Find function (with recursion)
    def find(v):
        if parent[v] == v:
            return v
        return find(parent[v])

    # Union function
    def union(u, v):
        parent[find(u)] = find(v)

    cost = 0

    print("Edge : Weight")

    # Process edges
    for u, v, w in edges:
        if find(u) != find(v):
            print(u, "-", v, ":", w)
            cost += w
            union(u, v)

    print("Total Cost:", cost)


# Vertices
vertices = ['A', 'B', 'C', 'D']

# Edges (u, v, weight)
edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 5)
]

# Function call
kruskal(vertices, edges)