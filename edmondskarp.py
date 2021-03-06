from bfs import bfs, bfs_cut

def get_flow(flows,u,v):
    key = f"{u}-{v}"
    return flows[key] 

def update_flows(flows,u,v,i):
    key = f"{u}-{v}"
    flows[key] = flows.get(key,0) + i
       
def get_aug_flow(graph, path):
    if not path:
        return 0
    aug_flow = 999999999999999
    for i in range(len(path)-2):
        for e in graph[1]:
            (u,w),weight = e 
            if u==path[i] and w==path[i+1]:
                aug_flow = min(aug_flow, weight)
    return aug_flow
        
def edmonds_karp(graph, source, sink):
    print()
    print("Starting Edgmonds-Karp...")
    
    vertices,edges = graph
    print("Graph:")
    print(f"Vertices: {vertices}")
    print(f"Edges: {edges}")
    
    print()
    max_flow = 0
    print(f"Max flow: {max_flow}")

    print("Initialising Residual Graph...")
    residual_edges = []
    for (u,v),w in edges:
        residual_edges.append([(u,v), w])
        residual_edges.append([(v,u), 0])
    residual_graph = (vertices,residual_edges) 
    print(f"Residual Vertices: {residual_graph[0]}")
    print(f"Residual Edges:")
    for e in edges:
        print(f"\t{e}")
    print()
            
        
    while True:
        print("Searching minimal path Source-Sink")
        aug_path = bfs(residual_graph, source, sink)
        if not aug_path:
            print("No more augmeting paths. Max flow found!")
            break

        aug_flow = get_aug_flow(residual_graph, aug_path)
        print(f"Augmenting flow: {aug_flow}")
        max_flow += aug_flow
        print(f"New max flow = {max_flow}")
        print()
        
        print(f"Updating Residual Graph...")
        
        for edge in residual_edges:
            for i in range(len(aug_path)-1):
                u = aug_path[i]
                v = aug_path[i+1]

                if edge[0] == (u,v):
                    edge[1] = edge[1] - aug_flow
                if edge[0] == (v,u):
                    edge[1] = edge[1] + aug_flow
                
        print(f"Residual Vertices: {residual_graph[0]}")
        print(f"Residual Edges:")
        for e in residual_edges:
            print(f"\t{e}")
        print()
    print()
    
    maxxed_edges = []
    for uv,w in residual_graph[1]:
        if w == 0:
            maxxed_edges.append(uv)
    
    possible_cuts = []
    for e in edges:
        if e[0] in maxxed_edges:
            possible_cuts.append(e)
    
    print(f"Max flow: {max_flow}")
    print(f"Edges with maxxed out flow")
    for e in possible_cuts:
        print(f"\t",e)
    print()
    
    print(f"BFS-ing for minimum cut...")
    min_cut = bfs_cut(graph,source,sink,possible_cuts)
        
    print()
    print(f"Minimum cut set:")
    for e in min_cut:
        print("\t",e)
    
    return max_flow,min_cut




if __name__ == '__main__':
    example_vertices = ["S","A","B","C","D","E","F","G","T"]
    example_edges = [
        [("S","A"), 5],
        [("S","C"),20],
        [("A","B"), 5],
        [("A","D"),10],
        [("B","T"), 5],
        [("C","B"), 5],
        [("C","F"), 8],
        [("D","C"), 2],
        [("D","E"),10],
        [("E","T"),10],
        [("F","G"), 9],
        [("G","T"), 8]
        ]
    
    graph = (example_vertices, example_edges)
    edmonds_karp(graph, "S", "T")
    
    
    
    
    
    
    
    
    
    