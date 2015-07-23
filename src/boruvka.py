__author__ = 'Francois Belanger 94 245 437' \
             'Genevieve Dostie 12 078 306' \
             'Jeremie Coulombe 13 061 991'

from disjoint_set import DisjointSet

# adapted from https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm)


def boruvka(adj_list):
    disj_set = DisjointSet()

    for u in adj_list.keys():
        disj_set.make_set(u)

    min_span_tree = []
    while True:
        minima = {}
        for u in adj_list.keys():
            root = disj_set.find(u)
            for v in adj_list[u]:
                if disj_set.find(v) != root and (root not in minima or adj_list[u][v] < minima[root][0]):
                    minima[root] = (adj_list[u][v], u, v)

        if len(minima) == 0:
            break

        for edge in minima.items():
            if disj_set.union(edge[0], edge[1][2]):
                min_span_tree.append(edge[1])

    return min_span_tree
