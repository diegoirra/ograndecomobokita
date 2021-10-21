from johnson import johnson

vertices = set()
edges = []

with open('depositos.txt') as f:
    lines = f.readlines()
    for line in lines:
        v,u,w = line.strip().split(',')
        vertices.add(v)
        vertices.add(u)
        edge = (v,u)
        edges.append([edge, int(w)])

vertices_list = list(vertices)
vertices_list.sort()
print(edges)
print(vertices_list)

johnson(vertices_list, edges)
