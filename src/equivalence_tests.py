# -*- coding: utf-8 -*-

from boruvka import boruvka
from kruskal import kruskal
from prim import prim
from graph_generator import generate_graph

def normalize_edge_list(edges):
    """
    Alter an edge list so that edges always goes from a vertex to a vertex with a greater value
    :param edge list:
    """
    for edge in edges:
        if edge[1] > edge[2]:
            edges.remove(edge)
            edges.add((edge[0], edge[2], edge[1]))

def build_mst_edge_list(tree, adj_list):
    edges = set()
    for i in range(1, len(tree)):
        parent = tree[i]
        edges.add((adj_list[i][parent], i, parent))
    normalize_edge_list(edges)
    return edges


def run_equivalence_test(n, trace=False):
    """
    Compare all algorithms for the same input graph
    :param n:       size of the test graph
    :param trace:   print debug info is test failed
    :return True if test succeeds
    """
    adj_list, vertex_list, edge_list = generate_graph(n)

    min_span_tree_boruvka = set(boruvka(adj_list))
    normalize_edge_list(min_span_tree_boruvka)
    min_span_tree_kruskal = set(kruskal(vertex_list, edge_list))
    min_span_tree_prim = build_mst_edge_list(prim(adj_list, vertex_list, 0), adj_list)

    success = min_span_tree_boruvka == min_span_tree_kruskal == min_span_tree_prim

    if not success and trace:
        print 'TEST FAILED:'
        print 'Adjacency list: {}'.format(adj_list)
        print 'Edge and vertex list: {}'.format(edge_list)
        print 'Minimum spanning tree with Boruvka: {}'.format(min_span_tree_boruvka)
        print 'Minimum spanning tree with Kruskal: {}'.format(min_span_tree_kruskal)
        print 'Minimum spanning tree with Prim:    {}'.format(min_span_tree_prim)
        print '----------------------------------'

    return success

def run_equivalence_test_suite(max_graph_size, perc_increm=5):
    """
    Run a series of algorithm equivalence tests and prints an ugly chart depicting results
    :param max_graph_size: maximum input graph size
    :param perc_increm:    percentages increments in the result chart
\    """
    # Prepare result chart
    result_chart = []
    for j in range(100/perc_increm + 1):
        result_chart.append([])

    # Run equivalence tests
    for size in range(1, max_graph_size + 1):
        success_count = 0
        for i in range(100):
            if run_equivalence_test(size):
                success_count += 1
        result_chart[(100-success_count)/perc_increm].append(size)
        print 'Success rate for n={}: {}%'.format(size, success_count)

    # Print result chart
    perc = 100
    for line in result_chart:
        print '%3d%%' % perc,
        for i in range(max_graph_size + 1):
            print('·' if i in line else ' '),
        print
        perc -= perc_increm

run_equivalence_test_suite(50)
