# Dijkstra algorithm O(Elog(V)) for finding shortest paths from one node to all other nodes in a
# weighted and non-negative weight graph.

import queue

MAX = 100

INF = 10**9


class Node(object):
    def __init__(self, id, cost):
        self.id = id
        self.cost = cost

    def __lt__(self, other):
        return self.cost <= other.cost

    def __repr__(self) -> str:
        return f'({self.id}, {self.cost})'


def Dijkstra(graph, dist, path, s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.cost

        if dist[u] != w:
            continue

        for v in graph[u]:
            if w + v.cost < dist[v.id]:
                dist[v.id] = w + v.cost
                pq.put(Node(v.id, dist[v.id]))
                path[v.id] = u


if __name__ == '__main__':
    n = 6
    s = 0
    graph = [[] for _ in range(n)]
    dist = [INF for _ in range(n)]
    path = [-1 for _ in range(n)]

    graph[0].append(Node(1, 1))
    graph[1].append(Node(2, 5))
    graph[1].append(Node(3, 2))
    graph[1].append(Node(5, 7))
    graph[2].append(Node(5, 1))
    graph[3].append(Node(0, 2))
    graph[3].append(Node(2, 1))
    graph[3].append(Node(4, 4))
    graph[4].append(Node(3, 3))
    graph[5].append(Node(4, 1))

    Dijkstra(graph, dist, path, s)

    print(dist)
    print(path)
