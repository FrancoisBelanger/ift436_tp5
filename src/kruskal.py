from disjoint_set import DisjointSet

def kruskal(graph):
    disj_set = DisjointSet()
    for vertice in graph['vertices']:
        disj_set.make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if disj_set.find(vertice1) != disj_set.find(vertice2):
            disj_set.union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree

def boruvka(graph):
    disj_set = DisjointSet()
    for vertice in graph['vertices']:
        disj_set.make_set(vertice)


# 0   Input: A connected graph G whose edges have distinct weights
# 1   Initialize a forest T to be a set of one-vertex trees, one for each vertex of the graph.
# 2   While T has more than one component:
# 3     For each component C of T:
# 4       Begin with an empty set of edges S
# 5       For each vertex v in C:
# 6         Find the cheapest edge from v to a vertex outside of C, and add it to S
# 7       Add the cheapest edge in S to T
# 8   Output: T is the minimum spanning tree of G.

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
    'edges': set([
        (1, 'A', 'B'),
        (5, 'A', 'C'),
        (3, 'A', 'D'),
        (4, 'B', 'C'),
        (2, 'B', 'D'),
        (1, 'C', 'D'),
    ])
}
minimum_spanning_tree = set([
    (1, 'A', 'B'),
    (2, 'B', 'D'),
    (1, 'C', 'D'),
])
assert kruskal(graph) == minimum_spanning_tree

