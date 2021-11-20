import sys


vertices = set()
edges = []
source = "" 
sink = ""

if len(sys.argv) != 2:
    print()
    print("ERROR: you need to pass a file as an argument")
    exit(-1)

file = sys.argv[1]

print("        START")
print()
print("Reading VUELOS from file:", file)
print()

with open(file) as f:
    lines = f.readlines()
    source = lines.pop(0)
    sink   = lines.pop(0)
    for line in lines:
        v,u,w = line.strip().split(',')
        vertices.add(v)
        vertices.add(u)
        if v == sink or u == source:
            continue
        edge = (v,u)
        edges.append([edge, int(w)])

vertices_list = list(vertices)
vertices_list.sort()
print("Source:",source)
print("Sink:",sink)
print("Edges:",edges)
print("Vertices:", vertices_list)
print()
print("File is good. Continuing...")
print()


## do stuff




if __name__ == '__main__':
    
    
    
    pass










