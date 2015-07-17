# Tim Wilson, 2-25-2002
# https://www.ics.uci.edu/~eppstein/161/python/prim.py

def decrease_key(Q, K):
    """
    :param Q: min queue
    :param K: vertex list
    """
    for i in range(len(Q)):
        for j in range(len(Q)):
            if K[Q[i]] < K[Q[j]]:
                s = Q[i]
                Q[i] = Q[j]
                Q[j] = s

def prim(adj_list, vertex_list, r):
    """
    :param adj_list:    adjacency list
    :param vertex_list: vertex list
    :param r:           root
    :return:            minimum spanning tree
    """
    u = 0
    v = 0

    # initialize and set each value of the array P (pi) to none
    # pi holds the parent of u, so P(v)=u means u is the parent of v
    P=[None]*len(vertex_list)

    # initialize and set each value of the array K (key) to some large number (simulate infinity)
    K = [999999]*len(vertex_list)

    # initialize the min queue and fill it with all vertices in V
    Q=[0]*len(vertex_list)
    for u in range(len(Q)):
        Q[u] = vertex_list[u]

    # set the key of the root to 0
    K[r] = 0
    decrease_key(Q, K)    # maintain the min queue

    # loop while the min queue is not empty
    while len(Q) > 0:
        # pop the first vertex off the min queue
        u = Q[0]
        Q.remove(Q[0])

        # loop through the vertices adjacent to u

        for v in adj_list[u]:
            w = adj_list[u][v]    # get the weight of the edge uv

            # proceed if v is in Q and the weight of uv is less than v's key
            if Q.count(v)>0 and w < K[v]:
                # set v's parent to u
                P[v] = u
                # v's key to the weight of uv
                K[v] = w
                # maintain the min queue
                decrease_key(Q, K)
    return P

# B = {0: {1: 4, 7: 8},
#      1: {0: 4, 2: 8, 7: 11},
#      2: {1: 8, 3: 7, 5: 4, 8: 2},
#      3: {2: 7, 4: 9, 5: 14},
#      4: {3: 9, 5: 10},
#      5: {2: 4, 3: 14, 4: 10, 6: 2},
#      6: {5: 2, 7: 1, 8: 6},
#      7: {0: 8, 1: 11, 6: 1, 8: 7},
#      8: {2: 2, 6: 6, 7: 7}}

# V = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# P = prim(B, V, 0)
# print P
