
def get_neighbors(graph, vertex):
    edges = graph[1]
    neighbors = set()
    for e in edges:
        (u,w),weight = e
        if vertex == u and weight>0:
            neighbors.add(w)
            
    neighbors = list(neighbors)
    neighbors.sort()
    return neighbors

def get_neighbors_and_cut(graph, vertex, possible_cuts):
    edges = graph[1]
    neighbors = set()
    cut = []
    for e in edges:
        (u,w),weight = e
        if vertex == u:
            if e in possible_cuts:
                print(f"Found flow cut: {e}")
                cut.append(e) 
            elif weight>0:
                neighbors.add(w)
            
    neighbors = list(neighbors)
    neighbors.sort()
    return neighbors,cut

def get_path(parents,source,sink):
    print()
    path = [sink]
    current = sink
    
    while current != source:
        parent = parents[current]
        path.insert(0,parent)                
        current = parent
        
    for v in path:
        if v == sink:
            print(f"{v}",end='')
            continue
        print(f"{v} -> ",end='')
    print()
    print()
    return path
       
    
def bfs(graph, source, sink):
    print()
    print("Starting Bread First Search in Graph: ")
    print(f"Vertices: {graph[0]}")
    print(f"Edges: ")
    for e in graph[1]:
        print(f"\t {e}")
    print()
    print(f"With root={source} and goal={sink}")
    queue = []
    queue.append(source)
    parents = {}
    parents[source] = "Source"
    
    while queue:
        print()
        print("Queue:", queue)
        print("Parents:", parents)        
        print()
        v = queue.pop(0)        
        if v == sink:
            print()
            print("BFS complete!")
            print(f"Goal ({sink}) was found!!")
            print("By the following path:")
            return get_path(parents,source,sink)
        print("Searching node:",v)
        
        v_neighbors = get_neighbors(graph, v)
        print(f"Neighbours of {v}: {v_neighbors}")
        for n in v_neighbors:
            if n not in parents:
                print(f"{n} was not visited! Updating..")
                parents[n] = v
                queue.append(n)
    
    return []

def bfs_cut(graph, source, sink, possible_cuts):
    queue = []
    queue.append(source)
    parents = {}
    parents[source] = "Source"
    
    min_cuts = []
    while queue:
        print(f"BFS queue: {queue}")        
        v = queue.pop(0)        
        if v == sink:
            print("Sink was found, no cut")
            return []
        
        print(f"Current node: {v}")
        v_neighbors,cuts = get_neighbors_and_cut(graph, v, possible_cuts)
        for edge in cuts:
            if edge not in min_cuts:
                min_cuts.append(edge)
        
        for n in v_neighbors:
            if n not in parents:
                parents[n] = v
                queue.append(n)
    
    return min_cuts


if __name__ == "__main__":
    example_vertices = ["A","B","C","D","E", "F","G"]
    example_edges = [
        [("A","B"),1],
        [("A","D"),1],
        [("B","C"),1],
        [("B","F"),1],
        [("C","E"),1],
        [("C","G"),1],
        [("D","F"),1],
        [("E","B"),1],
        [("E","F"),1],
        [("F","A"),1],
        [("G","E"),1]
        ]
    
    graph = (example_vertices, example_edges)
    bfs(graph, "A", "G")























