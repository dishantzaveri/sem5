from collections import defaultdict
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)


	def addEdge(self,u,v):
		self.graph[u].append(v)

	def BFS(self, s):

		visited = [False] * (max(self.graph) + 1)
		queue = []

		queue.append(s)
		visited[s] = True

		while queue:

			s = queue.pop(0)
			print (s, end = " ")

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

g = Graph()
n=int(input('enter number of edges:\n'))
for i in range(n):
    print('enter v1 v2:')
    g.addEdge(int(input()), int(input()))  

g.BFS(2)
