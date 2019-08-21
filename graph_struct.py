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

    def compKcore(self, n, k, deg):

        if deg[n - 1] < k:
            deg[n - 1] = 0
            for i in self.graph[n]:
                if deg[i - 1]>0:
                    deg[i-1]-=1

        return deg


    def isKcores(self, k):
        deg = [0]*self.V

        for i in list(self.graph.keys()):
            deg[i-1] = len(self.graph[i])

        old_deg = deg[:]
        while True:
            for i in range(self.V):
                if not deg[i] == 0:
                    deg = self.compKcore(i+1, k, deg)
            if old_deg==deg:
                break
            else:
                old_deg = deg

        return len([x for x in deg if x>=k])
