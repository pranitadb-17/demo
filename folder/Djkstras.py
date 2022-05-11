import sys

def printSolution(v,dist):
   print("Vertex \tDistance from Source")
   for node in range(v):
      print(node, "\t", dist[node])
 
  
def minDistance(v,dist, sptSet):
 
   min = sys.maxsize
 
   for u in range(v):
      if dist[u] < min and sptSet[u] == False:
         min = dist[u]
         min_index = u
 
   return min_index
 
def dijkstra(v,src):
 
   dist = [sys.maxsize] * v
   dist[src] = 0
   sptSet = [False] * v
 
   for node in range(v):
 
      x = minDistance(v,dist, sptSet)
 
      
      sptSet[x] = True
 
      for y in range(v):
         if graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + graph[x][y]:
            dist[y] = dist[x] + graph[x][y]
 
   printSolution(v,dist)

graph = [[0, 4, 2, 0],
        [4, 0, 8, 0],
        [0, 8, 0, 7],
        [6, 3, 7, 0]]
 
dijkstra(4,0)
