from numpy import Inf
from aux import print_dict,example_vertices,example_edges


def bellman_ford(vertices, edges, source):
    
    print("Running Bellman-Ford for below Graph:")
    print()
    print("Vertices:")
    print("    ",vertices)
    print("Edges:")
    for e in edges:
        print("    ",e)
    
    print()
    print("Starting algorithm from vertex =",source)
    print()
    
    print("Init distances:")
    
    dist = {v: 0 if v == source else Inf for v in vertices}
    print_dict(dist) 

    for i in range(len(vertices)):
        print(f"Loop {i+1}:")
        print()        
        for (u, v), w in edges:            
            dist[v] = min(dist[v], dist[u] + w)
        print_dict(dist)
    return dist

if __name__ == '__main__':
    
    vertices= example_vertices
    edges = example_edges
    
    
    bellman_ford(vertices, edges, "A")
    
        
    

















