__author__ = 'Francois Belanger 94 245 437' \
             'Genevieve Dostie 12 078 306' \
             'Jeremie Coulombe 13 061 991'

import numpy as np
import matplotlib.pyplot as plt

nb_algo = 3
algo = ['Boruvka', 'Kruskal', 'Prim']

def plot_graph(x1, y1, x2, y2, idx):
    plt.plot(y1, x1[idx])
    plt.plot(y1, x1[idx])
    plt.title("Temps d'execution de " + algo[idx] + " en fonction de la taille des donnee")
    plt.ylabel("Temp (sec.)")
    plt.xlabel("Nombre de noeud dans le graph")

def plot_bo(x1, y1, x2, y2):
    plot_graph(x1, y1, x2, y2, 0)
    plt.show()


def plot_kr(x1, y1, x2, y2):
    plot_graph(x1, y1, x2, y2, 1)
    plt.show()

def plot_pr(x1, y1, x2, y2):
    plot_graph(x1, y1, x2, y2, 3)
    plt.show()


def plot_group_graph(timed, step_sizes):
    color = ['r', 'g', 'b']
    for i in range(nb_algo):
        plt.plot(step_sizes, timed[i], color[i])

    plt.title("Temps d'execution en fonction de la taille des donnee")
    plt.ylabel("Temp (sec.)")
    plt.xlabel("Nombre de noeud dans le graph")
    plt.legend(['Boruvka', 'Kruskal', 'Prim'], loc='upper left')


def plot_total(x1, y1, x2, y2):
    plot_group_graph(x1, y1)
    plot_group_graph(x2, y2)
    plt.show()

if __name__ == '__main__':
    x1 = np.load('data_100_20000_20_100.npy')
    y1 = np.load('step_100_20000_20_100.npy')
    x2 = np.load('data_100_30000_25_100.npy')
    y2 = np.load('step_100_30000_25_100.npy')

    plot_total(x1, y1, x2, y2)

    plot_bo(x1, y1, x2, y1)
    plot_kr(x1, y1, x2, y1)
    plot_pr(x1, y1, x2, y1)
