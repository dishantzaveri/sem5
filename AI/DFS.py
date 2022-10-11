from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self,s):
        g.visited.add(s)
        print (s, end = " ")

        for i in self.graph[s]:
            if i not in self.visited:
                self.dfs(i)

g = Graph()
n=int(input('enter number of edges:\n'))
for i in range(n):
    print('enter v1 v2:')
    a,b=input().split()
    g.addEdge(int(a), int(b))  
g.dfs(min(g.graph))
