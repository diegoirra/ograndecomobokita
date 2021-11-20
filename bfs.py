
def get_neighbors(graph, vertex):
    edges = graph[1]
    neighbors = set()
    for e in edges:
        u,w = e[0]
        if vertex == u:
            neighbors.add(w)
        # if vertex == w:
        #     neighbors.add(u)
            
    neighbors = list(neighbors)
    neighbors.sort()
    return neighbors

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
    
    return "Sink not found"


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























