# Disjoint set union
# a data structure to combine elements together into large set

'''
Naive approach: O(N) for 2 operations findSet and unionSet

# we define number of set as the root parent of that set
def findSet(parent, u):
    while u != parent[u]:
        u = parent(u)
    return u

# function unions 2 elements
def unionSet(parent, u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[up] = vp

'''

# Optimal approach: O(log(N)) for all 2 operations.
# unionSet will be operated base on node's rank (assign node with lower rank to node has higher rank).
# findSet will compress the path of found node to root parent.

import unicodedata


def findSet(parent, u):
    if parent[u] != u:
        parent[u] = findSet(parent, parent[u])
    return parent[u]


def sameSet(parent, u, v):
    return findSet(parent, u) == findSet(parent, v)


def unionSet(parent, ranks, u, v):
    up = findSet(parent, u)
    vp = findSet(parent, v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1


n = 7
parent = [i for i in range(n+1)]
ranks = [0 for _ in range(n+1)]

unionSet(parent, ranks, 1, 2)
unionSet(parent, ranks, 2, 3)
unionSet(parent, ranks, 4, 5)
unionSet(parent, ranks, 5, 6)
print(sameSet(parent, 2, 6))  # expected False
unionSet(parent, ranks, 6, 7)
unionSet(parent, ranks, 7, 3)
print(sameSet(parent, 2, 6))  # expacted True
print(sameSet(parent, 7, 1))  # expacted True
