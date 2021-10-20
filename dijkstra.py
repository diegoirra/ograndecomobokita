from numpy import Inf
from aux import print_dict,example_vertices,example_edges2

SOURCE = 'Source'

def print_neighbors(vertex, path):
    neighbors=path[vertex]
    for n in neighbors:
        print(f"{vertex} -> {n}")
    for n in neighbors:
        if n in path:
            print_neighbors(n, path)    
    return

def print_path(p):
    
    inverted={} 
    for k,v in p.items():
        if v:
            inverted[v]= inverted.get(v, [] ) + [k]
    print_neighbors(SOURCE, inverted)

def get_neighbors(visited,edges):
    print("Get unvisited neighbors:")
    neighbors = {v: [] for v in visited}
    for (v,u), w in edges:
        if v in visited and u not in visited:
            neighbors[v].append((u, w))
    print_dict(neighbors)
    print()
    return neighbors
    
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
    if source not in vertices:
        print()
        print("ERROR: Source not in Graph!!")
        return 
        
    dist = {}
    prev = {}
    not_visited = vertices
    visited = []
    print("Init distances:")
    for v in vertices:
        if v == source:
            dist[v] = 0
            prev[v] = SOURCE
        else:
            dist[v] = Inf
            prev[v] = ''    
    print_dict(dist)  
    print("El Camino hacia El Dorado:")
    print_path(prev)
    print()  

    current_node = source
    while len(not_visited) > 0:
        print("Not visited:")
        print(not_visited)
        print()
        
        print("Moving to vertex:",current_node)
        if current_node in not_visited:
            not_visited.remove(current_node)
            visited.append(current_node)
        
        neighbors = get_neighbors(visited, edges)
        closest_node = ''
        closest_dist = Inf
        for v in visited:
            for u,w in neighbors[v]:
                alt = w if dist[current_node] == Inf else dist[current_node]+ w             
                if alt < closest_dist:
                    closest_node = u
                    closest_dist = alt
        
        if closest_node:
            next_node = closest_node
            print()
            print("Move to", next_node)
    
            dist[next_node] = closest_dist
            print("Updated distances")
            prev[next_node]=current_node
            current_node=next_node
            print("Updated El Camino")
            
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






















