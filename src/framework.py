__author__ = 'Francois Belanger 94 245 437' \
             'Genevieve Dostie 12 078 306' \
             'Jeremie Coulombe 13 061 991'

import argparse
import random
import time
import timeit

import numpy as np

from graph_generator import *
from boruvka import *
from kruskal import *
from prim import *

nb_algo = 3


def parm():
    parser = argparse.ArgumentParser(description="put someting here")
    parser.add_argument('--n_min', '-n', type=int, default=100, help="Min data size")
    parser.add_argument('--n_max', '-N', type=int, default=10000, help="Max data size")
    parser.add_argument('--nb_sample', '-s', type=int, default=100, help="Number of random samples")
    parser.add_argument('--nb_repetition', '-r', type=int, default=1000, help="Number of test at each data size")
    args = parser.parse_args()

    return args


def test(args):
    # initializing pseudo random generator
    np.random.seed(0)
    random_state = np.random.get_state()

    step_sizes = random.sample(xrange(args.n_min+1, args.n_max), args.nb_sample-2)
    step_sizes.append(args.n_min)
    step_sizes.append(args.n_max)
    step_sizes.sort()

    timed = np.zeros((nb_algo, len(step_sizes)))

    fct = [boruvka, kruskal, prim]

    for algo_idx in range(nb_algo):
        np.random.set_state(random_state)

        for sz_idx in range(len(step_sizes)):
            start_time = timeit.default_timer()
            for test_iter in xrange(0, args.nb_repetition):
                graph = generate_graph(step_sizes[sz_idx])
                #execute the algo on the graph
                fct[algo_idx](graph[algo_idx % 2])

            #timer stop
            timed[algo_idx][sz_idx] = timeit.default_timer() - start_time

    np.random.set_state(random_state)
    for sz_idx in range(len(step_sizes)):
        start_time = timeit.default_timer()

        for test_iter in xrange(0, args.nb_repetition):
                graph = generate_graph(step_sizes[sz_idx])

        delta = timeit.default_timer() - start_time

        for i in range(nb_algo):
            timed[i][sz_idx] -= delta

    timed /= args.nb_repetition

    stamp = str(time.time())

    np.save('data_'+stamp, timed)
    np.save('step_'+stamp, step_sizes)


if __name__ == "__main__":
    arg = parm()
    test(arg)