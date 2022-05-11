import sys

def printMST(graph, parent, n):
        print ("Edge \tWeight")
        for i in range(1, n):
            print (parent[i], "-", i, "\t", graph[i][parent[i]])
 
# A utility function to find the vertex with
# minimum distance value, from the set of vertices
# not yet included in shortest path tree
def minKey(n, key, mstSet):
 
    # Initialize min value
    min = sys.maxsize
 
    for v in range(n):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v
    return min_index
 
# Function to construct and print MST for a graph
# represented using adjacency matrix representation
def primMST(graph,n):
 
    # Key values used to pick minimum weight edge in cut
    key = [sys.maxsize] * n
    parent = [None] * n # Array to store constructed MST
    # Make key 0 so that this vertex is picked as first vertex
    key[0] = 0
    mstSet = [False] * n
 
    parent[0] = -1 # First node is always the root of
 
    for cout in range(n):
 
        # Pick the minimum distance vertex from the set of vertices not yet processed.
        # u is always equal to src in first iteration
        
        u = minKey(n, key, mstSet)

        # Put the minimum distance vertex in the shortest path tree
        
        mstSet[u] = True
 
        # Update dist value of the adjacent vertices of the picked vertex only if the current
        # distance is greater than new distance and the vertex in not in the shortest path tree
        
        for v in range(n):
 
            # graph[u][v] is non zero only for adjacent vertices of m
            # mstSet[v] is false for vertices not yet included in MST
            # Update the key only if graph[u][v] is smaller than key[v]
            
            if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u
 
    printMST(graph,parent,n)

n=int(input("Enter no. of vertices : "))  
graph = []
for i in range(n):
    tmp=list(map(int,input().split()))
    graph.append(tmp)
'''
graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
''' 
primMST(graph,n)
