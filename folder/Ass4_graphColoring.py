def isSafe(Graph, n, v, colour, c):
        for i in range(n):
            if Graph[v][i] == 1 and colour[i] == c:
                return False
        return True

def graphColourUtil(Graph, n, m, colour, v):
    if v == n:
        return True
    for c in range(1, m + 1):
        if isSafe(Graph,n,v, colour, c) == True:
            colour[v] = c
            if graphColourUtil(Graph,n,m, colour, v + 1) == True:
               return True
            colour[v] = 0
 
def graphColouring(Graph,n, m):
    colour = [0] * n
    if graphColourUtil(Graph,n,m, colour, 0) == None:
        return False
 
    print ("Solution exist and Following are the assigned colours:")
    for c in colour:
        print (c,end=' ')
    return True
 

n=int(input("Enter no. of vertices : "))
graph=[]
print("Enter Adjacancy matrix for graph")
for i in range(n):
    tmp=list(map(int,input().split()))
    graph.append(tmp)
print(graph)    


#graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3
graphColouring(graph,n,m)

