# Prim's algorithm for finding minimum spanning tree

import queue

INF = 10e9


class Node:
    def __init__(self, id, cost):
        self.id = id
        self.cost = cost

    def __lt__(self, other):
        return self.cost <= other.cost

    def __repr__(self):
        return f"({self.id}, {self.cost})"


def prims(graph, path, visited, dist, src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0

    while pq.empty() == False:
        top = pq.get()
        u = top.id
        visited[u] = True

        if top.cost != dist[u]:
            continue

        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.cost
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u


def printMST(dist, path, n):
    ans = 0
    for i in range(n + 1):
        if path[i] == -1:
            continue
        ans += dist[i]
    return ans


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))
    dist = [INF for _ in range(n + 1)]
    path = [-1 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    prims(graph, path, visited, dist, 1)
    print(printMST(dist, path, n))
