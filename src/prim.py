__author__ = 'Francois Belanger 94 245 437' \
             'Genevieve Dostie 12 078 306' \
             'Jeremie Coulombe 13 061 991'

import sys
from heapq import heappop, heappush

# adapted from Algorithmes et structures de donnees, IFT436, Chap. 3, page 34, Richard St-Denis


def prim(adj_list):
    queue = []
    costs = []
    parent = []

    for v in adj_list.keys():
        c = 0 if v is 0 else sys.maxint
        queue.append((c, v))
        costs.append(c)
        parent.append(None)

    while len(queue) > 0:
        best = heappop(queue)
        cost, u = best
        if cost is sys.maxint:
            break
        costs[u] = None
        for edge in adj_list[u].items():
            v, weight = edge
            if costs[v] is not None and weight < costs[v]:
                parent[v] = u
                costs[v] = weight
                heappush(queue, (weight, v))

    return parent
