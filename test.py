from graph_struct import Graph

k = 3;
g1 = Graph (9);
g1.addEdge(0+1,1+ 1)
g1.addEdge(0+1,1+ 2)
g1.addEdge(1+1,1+ 2)
g1.addEdge(1+1,1+ 5)
g1.addEdge(2+1,1+ 3)
g1.addEdge(2+1,1+ 4)
g1.addEdge(2+1,1+ 5)
g1.addEdge(2+1,1+ 6)
g1.addEdge(3+1,1+ 4)
g1.addEdge(3+1,1+ 6)
g1.addEdge(3+1,1+ 7)
g1.addEdge(4+1,1+ 6)
g1.addEdge(4+1,1+ 7)
g1.addEdge(5+1,1+ 6)
g1.addEdge(5+1,1+ 8)
g1.addEdge(6+1,1+ 7)
g1.addEdge(6+1,1+ 8)

print('k_core - '+ str(g1.isKcores(4)))
