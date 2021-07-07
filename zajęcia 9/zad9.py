from copy import deepcopy
from queue import PriorityQueue

def relax(u, v, w, dist, parent, q):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        parent[v] = u
        q.put((dist[v], v))


def dijkstra(G, i, j, visited, parent, dist, q):
    n = len(G)

    dist[i] = 0
    q.put((G[i], i))

    while not q.empty():
        weight, u = q.get()
        if u == j:
            break
        visited[u] = True
        for e in range(n):
            w = G[u][e]
            if w != -1 and not visited[e]:
                relax(u, e, G[u][e], dist, parent, q)

    return dist[j]


def min_cycle( G ):

  n = len(G)

  edges = []

  for i in range(n):
      for j in range(i + 1, n):
          if G[i][j] != -1:
              edges.append((i, j, G[i][j]))

  minDistance = float('inf')
  minParent = []
  minI = 0
  minJ = 0

  for edge in edges:

      visited = [False] * n
      parent = [None] * n
      dist = [float('inf')] * n

      i, j, weight = edge
      q = PriorityQueue()
      G[i][j] = -1
      G[j][i] = -1

      distance = dijkstra(G, i, j, visited, parent, dist, q)
      distance += weight

      if distance < minDistance:
          minDistance = distance
          minParent = parent
          minI = i
          minJ = j

      G[i][j] = weight
      G[j][i] = weight

  result = [minI]
  while minJ != minI:
      result.append(minJ)
      minJ = minParent[minJ]

  return result
  

### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
G = [[-1, 2,-1,-1, 1],
     [ 2,-1, 4, 1,-1],
     [-1, 4,-1, 5,-1],
     [-1, 1, 5,-1, 3],
     [ 1,-1,-1, 3,-1]]  
LEN = 7


GG = deepcopy( G )
cycle = min_cycle( GG )

print("Cykl :", cycle)


if cycle == []: 
  print("Błąd (1): Spodziewano się cyklu!")
  exit(0)
  
L = 0
u = cycle[0]
for v in cycle[1:]+[u]:
  if G[u][v] == -1:
    print("Błąd (2): To nie cykl! Brak krawędzi ", (u,v))
    exit(0)
  L += G[u][v]
  u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
  print("Błąd (3): Niezgodna długość")
else:
  print("OK")