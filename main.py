from ograndecomobokita.johnson import johnson

vertices = set()
edges = []

with open('depositos.txt') as f:
    lines = f.readlines()
    for line in lines:
        data = line.strip().split(',')
        vertices.add(data[0])
        vertices.add(data[1])
        newTuple = (data[0], data[1])
        edges.append([newTuple, int(data[2])])

vertices_list = list(vertices)
vertices_list.sort()
print(edges)
print(vertices_list)
print(johnson(vertices_list, edges))
