def addEdge(graph,u, v, w):
    graph.append([u, v, w])

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])
 

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    else:
        parent[yroot] = xroot
        rank[xroot] += 1
        
def KruskalMST(graph,n):
 
    result = []  # This will store the resultant MST
         
    i = 0
         
    e = 0

    graph = sorted(graph,key=lambda item: item[2])
 
    parent = []
    rank = []
 
    for node in range(n):
        parent.append(node)
        rank.append(0)
 
    while e < n - 1:
 
        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)
 
    minimumCost = 0
    print ("Edges in the constructed MST")
    for u, v, weight in result:
        minimumCost += weight
        print("%d -- %d == %d" % (u, v, weight))
    print("Minimum Spanning Tree" , minimumCost)

#g = Graph(4)
n=4
graph=[]
addEdge(graph,0, 1, 10)
addEdge(graph,0, 2, 6)
addEdge(graph,0, 3, 5)
addEdge(graph,1, 3, 15)
addEdge(graph,2, 3, 4)
 
KruskalMST(graph,n)
