from collections import defaultdict
from numpy import Inf
import heapq

def bellman_ford(vertices, edges, source):

    dist = {v: 0 if v == source else Inf for v in vertices}

    for _ in range(len(vertices)):
        for (u, v), w in edges:
            dist[v] = min(dist[v], dist[u] + w)
    return dist

def dijkstra(vertices, edges, source):

    dist = {}
    prev = {}
    heap = []
    for v in vertices:
        if v == source:
            dist[v] = 0
        else:
            dist[v] = Inf
            heapq.heappush(heap, (v, dist[v]))
        prev[v] = None

    neighbors = defaultdict(set)
    for (u, v), w in edges:
        neighbors[u].add((v, w))

    while len(heap) > 0:
        u = heapq.heappop(heap)

        for v, w in neighbors[u]:
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev

def johnson(vertices, edges):

    # step 1
    q = 'q'
    vertices.append(q)
    remove_later = []
    for v in vertices:
        edges[(q, v)] = 0
        remove_later.append((q, v))

    # step 2
    h = bellman_ford(vertices, edges, q)

    # step 3
    for (u, v), w in edges:
        edges[(u, v)] = w + h[u] - h[v]

    # step 4
    vertices.remove(q)
    for edge in remove_later:
        del edges[edge]

    shortest_dist = Inf
    shortest_path = None

    for v in vertices:
        dists, prevs = dijkstra(vertices, edges, v)
        total_dist = sum(dists.values())

        if total_dist <= shortest_dist:
            shortest_dist = total_dist
            shortest_path = prevs
            
    # aca faltaria aplicarle w = w - (h[u] - h[v]) a cada arista
    return shortest_path 
