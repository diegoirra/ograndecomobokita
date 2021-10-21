from bellman_ford import bellman_ford
from dijkstra import dijkstra
from numpy import Inf
from aux import example_edges,example_vertices,print_dict

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


def johnson(vertices, edges):
    
    print("Running Johnson for below Graph:")
    print()
    print("Vertices:")
    print("    ",vertices)
    print("Edges:")
    for e in edges:
        print("    ",e)
    print()
    
        
    print("Starting Algorithm:")
    print()
    # step 1
    q = 'q'
    print("Add extra vertex:",q)
    print()
    remove_later = []
    for v in vertices:
        e = [(q, v),0] 
        edges.append(e)
        remove_later.append(e)
    vertices.append(q)
    print("New Graph:")
    print()
    print("Vertices:")
    print("    ",vertices)
    print("Edges:")
    for e in edges:
        print("    ",e)
    print()
    print("Extra edges to be removed:")
    for e in remove_later:
        print("    ",e)
    print()

    # step 2
    h = bellman_ford(vertices, edges, q)
    print()
    print("Resulting distances from Bellman-Ford")
    print_dict(h)

    # step 3
    print("Update distances from Graph:")
    for i in range(len(edges)):
        (u, v), w = edges[i]
        edges[i][1] = w + h[u] - h[v]
    print("Edges:")
    for e in edges:
        print("    ",e)
    print()
    
    
    # step 4
    print("Remove extra vertex and edges...")
    vertices.remove(q)
    for edge in remove_later:
        edges.remove(edge)
    print("Graph is now:")
    print("Vertices:")
    print("    ",vertices)
    print("Edges:")
    for e in edges:
        print("    ",e)
    print()


    shortest_dist = Inf
    shortest_path = None
    dist_table = []
    winner = ''

    for v in vertices:
        print("Applying Dijkstra for vertex:", v)
        dists, prevs = dijkstra(vertices, edges, v)
        total_dist = sum(dists.values())
        print("Sum of distances = ", total_dist)

        if total_dist <= shortest_dist:
            print("This is a better solution!")
            print("Update closest vertex")
            shortest_dist = total_dist
            shortest_path = prevs
            dist_table = dists.copy()
            winner = v
        else:
            print("Not better :/")
     
    print()
    print()
    print("Solution was found!")
    print("And the winner of Shortest Path between All Pairs Dundie is:")
    print(f"**********************      {winner}      ********************************")
    print()
    print(f"Find distances from {winner} below")

    print()
    
    for d in dist_table:
        dist_table[d] = dist_table[d] + h[winner] - h[d]
    print_dict(dist_table)
    
    print()
    print(f"Shortest paths to everywhere from {winner}")
    print_path(shortest_path)
    
    return  


if __name__ == '__main__':
    
    vertices= example_vertices
    edges = example_edges
    
    
    johnson(vertices, edges)










