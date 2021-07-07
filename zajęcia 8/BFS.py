import queue

class Node:
    def __init__(self, edges):
        self.edges = edges
        self.visited = False
        self.d = -1
        self.parent = None


def BFS(G, s):
    q = queue.Queue()
    s.d = 0
    s.visited = True
    q.put(s, )
    while not q.empty():
        u = q.get()
        for i in range(len(u.edges)):
            v = G[u.edges[i]]
            if not v.visited:
                v.visited = True
                v.d = u.d + 1
                v.parent = u
                q.put(v)


nodes = [Node([1]), Node([2, 4]), Node([4]), Node([1]), Node([3])]
BFS(nodes, nodes[0])