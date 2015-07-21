import random

# Maximum weight of an edge
MAX_WEIGHT = 100

# Average degree of vertices
AVG_DEG = 10


def generate_graph(n):
    # Graph structures that must be generated in parallel
    adj_list = {}
    edges = []

    # Initialize adjacency lists for each vertex
    for u in xrange(0, n):
        adj_list[u] = {}

    # Connect each vertex to its "next" vertex to make the graph connected
    for u in xrange(0, n-1):
        weight = random.randint(1, MAX_WEIGHT)
        adj_list[u][u+1] = adj_list[u+1][u] = weight
        edges.append((weight, u, u+1))

    # Add random edges until graph is of correct size
    num_edges = n * min(0.2*(n-1), AVG_DEG)
    while len(edges) < num_edges:
        # Generate a random edge
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)

        # Skip edge for any of these conditions:
        #   - It is linking a vertex with itself
        #   - It is linking a vertex with a vertex that has a "lower" value (to keep the graph undirected)
        #   - It is linking a vertex with the "next" one
        #   - It was already added
        if u > v - 2 or v in adj_list[u]:
            continue

        # Add edge
        weight = random.randint(1, MAX_WEIGHT)
        adj_list[u][v] = adj_list[v][u] = weight
        edges.append((weight, u, v))

    return adj_list, (range(0, n), edges)
