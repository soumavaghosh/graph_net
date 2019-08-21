from collections import defaultdict
  
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices 
        self.graph= defaultdict(list)
        for i in range(self.V):
            self.graph[i+1] = []
  
    def addEdge(self,u,v): 
        self.graph[u].append(v)
        self.graph[v].append(u)

    def getMindeg(self):
        min = 9999999
        for i in list(self.graph.keys()):
            if len(self.graph[i]) < min:
                min = len(self.graph[i])

        return min

    def getMaxdeg(self):
        max = 0
        for i in list(self.graph.keys()):
            if len(self.graph[i]) > max:
                max = len(self.graph[i])

        return max

    def getAvgdeg(self):
        num = 0
        for i in list(self.graph.keys()):
            num += len(self.graph[i])

        return num/self.V

    def compKcore(self, n, k, deg, visited):

        visited[n-1] = True

        for i in self.graph[n]:
            if deg[n-1]<k:
                deg[i-1]-=1

            if not visited[n-1]:
                if self.compKcore(i, k, deg, visited):
                    deg[n-1]-=1

        return deg[n-1] < k


    def isKcores(self, k):
        deg = [0]*self.V
        for i in list(self.graph.keys()):
            deg[i-1] = len(self.graph[i])

        visited = [False]*self.V

        for i in range(self.V):
            if visited[i] == False:
                self.compKcore(i+1, k, deg, visited)

        for v in range(self.V):

            # Only considering those vertices which have
            # vDegree >= K after DFS
            if deg[v] >= k:
                print (str("\n [ ") + str(v+1) + "  " + str(deg[v]) + str(" ]"))

                # Traverse adjacency list of v and print only
                # those adjacent which have vvDegree >= k
                # after DFS
                for i in self.graph[v+1]:
                    if deg[i-1] >= k:
                        print("-> " + str(i))

        return
