from disjoint_set import DisjointSet

# adapted from https://github.com/israelst/Algorithms-Book--Python/blob/master/5-Greedy-algorithms/kruskal.py

def kruskal(graph):
    disj_set = DisjointSet()
    min_span_tree = []

    for u in graph['vertices']:
        disj_set.make_set(u)

    edges = list(graph['edges'])
    edges.sort()

    for edge in edges:
        weight, u, v = edge
        if disj_set.find(u) != disj_set.find(v):
            disj_set.union(u, v)
            min_span_tree.append(edge)

    return min_span_tree
