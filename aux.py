
example_vertices = ["A","B","C","D","E"]
example_edges = [
        [("A","B"),-1],
        [("A","D"),-2],
        [("B","C"),-6],
        [("D","C"),-3],
        [("D","E"), 4],
        [("E","C"), 5]
        ]

def print_dict(dic):
    for k in dic: print(k,dic[k])
    print()
    return