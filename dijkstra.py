from numpy import Inf
import heapq
from aux import print_dict,example_vertices,example_edges2

def print_path(p):
    print(p)

def dijkstra(vertices, edges, source):
    
    print("Running Dijkstra for below Graph:")
    print()
    print("Vertices:")
    print("    ",vertices)
    print("Edges:")
    for e in edges:
        print("    ",e)
    
    print()
    print("Starting algorithm from vertex =", source)
    print()
        
    dist = {}
    prev = {}
    heap = []
    print("Init distances:")
    for v in vertices:
        if v == source:
            dist[v] = 0
            prev[v] = 'Source'
        else:
            dist[v] = Inf
            prev[v] = ''    
        heapq.heappush(heap, (v, dist[v]))
    print_dict(dist)  
    print("El Camino hacia El Dorado:")
    print_path(prev)
    print()  

    print("Get neighbors:")
    neighbors = {v: [] for v in vertices}
    for (v,u), w in edges:
        neighbors[v].append((u, w))
    print_dict(neighbors)
    
    while len(heap) > 0:
        print("Not visited:")
        print(heap)
        print()
        u = heapq.heappop(heap)
        
        print("Moving to vertex:",u)
        print(f"{u[0]}'s neighbors: {neighbors[u[0]]}")
        print()
        for v, w in neighbors[u[0]]:
            print("daneigh",v,w)
            alt = w if dist[u[0]] == Inf else dist[u[0]]+ w
            print(f"new dist? {alt} vs idst[v] {dist[v]}")
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u[0]
                print("Updated El Camino")
                print("Updated distances")
        print()
        print("El Camino hacia El Dorado:")
        print_path(prev)
        print()
        print("Shortest distances from",source)
        print_dict(dist)
            
    return dist, prev


if __name__ == '__main__':
    
    vertices= example_vertices
    edges = example_edges2
    
    
    dijkstra(vertices, edges, "A")






















