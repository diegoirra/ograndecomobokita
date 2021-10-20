vertices = set()
edges = []

with open('depositos.txt') as f:
    lines = f.readlines()
    for line in lines:
        data = line.strip().split(',')
        vertices.add(data[0])
        vertices.add(data[1])
        newTuple = (data[0], data[1])
        edges.append([newTuple, data[2]])

print(edges)
print(vertices)

