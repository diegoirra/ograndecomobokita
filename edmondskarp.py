from bfs import bfs

def get_flow(flows,u,v):
    key = f"{u}-{v}"
    return flows[key] 

def update_flows(flows,u,v,i):
    key = f"{u}-{v}"
    flows[key] = flows.get(key,0) + i
       
def build_residual_graph(graph,flows):
    vertices,edges = graph
    residual_edges = []
    for (u,v),w in edges:
        flow = get_flow(flows, u,v)
        if flow < w:
            residual_edges.append([(u,v), w - flow])
        if flow > 0:
            residual_edges.append([(v,u), flow])
    return (vertices,edges) 

def get_aug_flow(graph, path):
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
    
    print("Initialising flows...")
    max_flow = 0
    flows = {}
    for e in edges:
        u,v = e[0]
        update_flows(flows,u,v,0)
    print(f"Max flow: {max_flow}")
    print("Flows per edge:")
    for f in flows:
        print(f"\t{f}: {flows[f]}")
    print()
            
        
    while True:
        print("Building Residual Graph:")
        residual_graph = build_residual_graph(graph, flows)
        print(f"Vertices: {residual_graph[0]}")
        print(f"Edges: {residual_graph[1]}")
        print()
        print("Searching minimal path Source-Sink")
        aug_path = bfs(residual_graph, source, sink)
        if not aug_path:
            print("No more augmeting paths. Max flow found!")
            break

        aug_flow = get_aug_flow(residual_graph, aug_path)
        print(f"Augmenting flow: {aug_flow}")
        print(f"Updating flows...")
        
        max_flow += aug_flow
        for i in range(len(aug_path)-2):
            u = aug_path[i]
            v = aug_path[i+1]
            update_flows(flows, u,v, -aug_flow)
            update_flows(flows, v,u,  aug_flow)
        print()
        print(f"New Max flow: {max_flow}")
        print(f"Flows per edge:")
        for f in flows:
            print(f"\t{f}: {flows[f]}")
        print()
        return
    print()
    
    maxxed_edges = []
    for uv,w in residual_graph[1]:
        if w == 0:
            maxxed_edges.append(uv)
    
    possible_cuts = []
    for e in edges:
        if e[0] in maxxed_edges:
            possible_cuts.append(e)
    
    possible_cuts.sort(key=lambda x: x[1])
    print(f"Max flow: {max_flow}")
    print(f"Edges with maxxed out flow")
    for e in possible_cuts:
        print(f"\t",e)
    print()
    
    current_sum = 0
    min_cut = []
    for i in range(len(possible_cuts)):
        for j in range(i+1,len(possible_cuts)):
            for k in range(i,j):
                uv,w = possible_cuts[k]
                current_sum += w
                min_cut.append([uv,w])
            if current_sum==max_flow:
                break
            min_cut = []
            current_sum = 0
        if current_sum==max_flow:
            break
        min_cut = []
        current_sum = 0
        
    print()
    print(f"Minimum cut set:")
    for e in min_cut:
        print("\t",e)
    
    return max_flow,min_cut




if __name__ == '__main__':
    example_vertices = ["S","A","B","C","D","E", "F","G","T"]
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
    
    
    
    
    
    
    
    
    
    