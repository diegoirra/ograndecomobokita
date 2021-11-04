from johnson import johnson
import sys

vertices = set()
edges = []

if len(sys.argv) != 2:
    print()
    print("ERROR: you need to pass a file as an argument")
    exit(-1)

file = sys.argv[1]

print("        START")
print()
print("Reading depositos from file:", file)
print()

with open(file) as f:
    lines = f.readlines()
    for line in lines:
        v,u,w = line.strip().split(',')
        vertices.add(v)
        vertices.add(u)
        edge = (v,u)
        edges.append([edge, int(w)])

vertices_list = list(vertices)
vertices_list.sort()
print("Edges",edges)
print("Vertices", vertices_list)
print()
print("File is good. Continuing...")
print()

johnson(vertices_list, edges)
