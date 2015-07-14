from boruvka import boruvka
from kruskal import kruskal

# connected oriented graph adjacency list
cogal = {
    'A': {'B': 1, 'C': 5, 'D': 3},
    'B': {'A': 1, 'C': 4, 'D': 2},
    'C': {'A': 5, 'B': 4, 'D': 1},
    'D': {'A': 3, 'B': 2, 'C': 1}
}

# connected oriented graph edge list
cogel = {
    'vertices': ['A', 'B', 'C', 'D'],
    'edges': {(1, 'A', 'B'),
              (5, 'A', 'C'),
              (3, 'A', 'D'),
              (4, 'B', 'C'),
              (2, 'B', 'D'),
              (1, 'C', 'D')}
}

# solution
minimum_spanning_tree = {(1, 'A', 'B'),
                         (2, 'B', 'D'),
                         (1, 'C', 'D')}

assert boruvka(cogal) == kruskal(cogel) == minimum_spanning_tree
