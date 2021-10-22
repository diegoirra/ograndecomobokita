from numpy import Inf

example_vertices = ["A","B","C","D","E"]
example_edges = [
        [("A","B"),-1],
        [("A","D"),-2],
        [("B","C"),-6],
        [("D","C"),-3],
        [("D","E"), 4],
        [("E","C"), 5]
        ]

example_edges2 = [
        [("A","B"),10],
        [("A","C"),2],
        [("C","A"),3],
        [("B","D"),4],
        [("C","D"),2],        
        [("D","B"),4],
        [("D","E"),7],
        [("E","A"),1],
        [("E","C"),5]
        ]


def print_dict(dic):
    for k in dic: print(f"{k}    {dic[k]}")
    print()
    return


def print_matr(dic):
    print()
    print("************************** Distance Matrix **************************")
    print()
    print('        ' + '\t'.join([str(k) for k in dic.keys()]) + "    Total")
    for k in dic:
        total = sum(dic[k].values())
        print(k + '\t' + '\t'.join([str(value) if value != Inf else '-' for value in list(dic[k].values())])+ f"    {'N/A' if total == Inf else total}")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        