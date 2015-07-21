__author__ = 'Francois Belanger 94 245 437' \
             'Genevieve Dostie 12 078 306' \
             'Jeremie Coulombe 13 061 991'

import argparse
# import random
import timeit

import numpy as np
import matplotlib.pyplot as plt

from graph_generator import *
from boruvka import *
from kruskal import *
from prim import *

nb_algo = 3


def save_graph(timed, step_sizes):
    # plt.plot(step_sizes, timed[0])
    # plt.plot(step_sizes, timed[1])
    for i in range(nb_algo):
        plt.plot(step_sizes, timed[i])

    plt.title(u"Temps d'execution en  fonction de la taille des donnee")
    plt.ylabel("temp (sec.)")
    print "step_sizes", step_sizes
    print "timed", timed
    plt.show()


def parm():
    parser = argparse.ArgumentParser(description="put someting here")
    parser.add_argument('n', type=int, default=10000, help="Max data size")
    parser.add_argument('--step_size', '-s', type=int, default=100, help="Data size step increment")
    parser.add_argument('--nb_test', '-t', type=int, default=1000, help="Number of test at each data size")
    parser.add_argument('--step_number', '-sn', type=int, help="Number of step to go from 1 to n" +
                                                               " in each batch of test. Override data step size")
    args = parser.parse_args()

    return args


def test(args):
    # initializing pseudo random generator
    random.seed(0)
    random_state = random.getstate()

    s_size = args.step_size

    if args.step_number is not None:
        s_size = args.n / args.step_number

    step_sizes = range(s_size, args.n+s_size, s_size)
    timed = np.zeros((nb_algo, len(step_sizes)))

    fct = [boruvka, kruskal, prim]
    # TODO: iterate on the algo
    for algo_idx in range(nb_algo):
        random.setstate(random_state)

      # TODO: iterate on the step_size
        for sz_idx in range(len(step_sizes)):
            start_time = timeit.default_timer()
            for test_iter in xrange(0, args.nb_test):
                graph = generate_graph(step_sizes[sz_idx])
                #execute the algo on the graph
                fct[algo_idx](graph[algo_idx % 2])

            #timer stop
            timed[algo_idx][sz_idx] = timeit.default_timer() - start_time

    random.setstate(random_state)
    for sz_idx in range(len(step_sizes)):
        start_time = timeit.default_timer()

        for test_iter in xrange(0, args.nb_test):
                graph = generate_graph(step_sizes[sz_idx])

        delta = timeit.default_timer() - start_time

        for i in range(nb_algo):
            timed[i][sz_idx] -= delta

    timed /= step_sizes

    save_graph(timed, step_sizes)

if __name__ == "__main__":
    arg = parm()
    test(arg)