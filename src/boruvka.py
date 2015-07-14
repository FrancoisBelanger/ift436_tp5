from disjoint_set import DisjointSet

# Original (pseudo code source: https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm)
# 0   Input: A connected graph G whose edges have distinct weights
# 1   Initialize a forest T to be a set of one-vertex trees, one for each vertex of the graph.
# 2   While T has more than one component:
# 3     For each component C of T:
# 4       Begin with an empty set of edges S
# 5       For each vertex v in C:
# 6         Find the cheapest edge from v to a vertex outside of C, and add it to S
# 7       Add the cheapest edge in S to T
# 8   Output: T is the minimum spanning tree of G.

# Adaptation
# 0   Input: An connected oriented graph G whose edges have distinct weights
# 1   Initialize a forest T to be a set of one-vertex trees, one for each vertex of the graph.
# 2   While T has more than one component:
# 3     Initialize a map <vertex,edge> M
# 4     For each vertex u in G:
# 5       M[find(u)] = Cheapest edge from u to a vertex outside of the component of u
# 6     Add M.values to T
# 7   Output: T is the minimum spanning tree of G.

def boruvka(graph):
    disj_set = DisjointSet()

    for u in graph.keys():
        disj_set.make_set(u)

    min_spanning_tree = set()
    while True:
        minima = {}
        for u in graph.keys():
            root = disj_set.find(u)
            for v in graph[u]:
                if disj_set.find(v) != root and (root not in minima or graph[u][v] < minima[root][0]):
                    minima[root] = (graph[u][v], u, v)

        if len(minima) == 0:
            break

        for edge in minima.items():
            if disj_set.union(edge[0], edge[1][2]):
                min_spanning_tree.add(edge[1])

    return min_spanning_tree
