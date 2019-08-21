from graph_struct import Graph
import pandas as pd

with open('socfb-Haverford76.mtx', 'rb') as f:
    d = f.readlines()[1:]

d = [x.decode('utf-8').strip() for x in d]

g = Graph(int(d[0].split(' ')[0]))
for e in d[1:]:
    g.addEdge(int(e.split(' ')[0]), int(e.split(' ')[1]))

num_edges = len(d[1:])
num_nodes = int(d[0].split(' ')[0])
print('num_nodes - '+ str(num_nodes))
print('num_edges - '+ str(num_edges))
print('density - '+ str(num_edges*2/(num_nodes*(num_nodes-1))))
print('min_deg - '+ str(g.getMindeg()))
print('max_deg - '+ str(g.getMaxdeg()))
print('avg_deg - '+ str(g.getAvgdeg()))

k = 1
while(True):
    l = g.isKcores(k)
    if l==0:
        break
    else:
        k+=1

print('k_core - '+ str(k))

ct = 0
for i in range(num_nodes):
    ct+=g.getClustercoeff(i+1)
ct/=num_nodes

print('avg_clustering_coeff - '+ str(ct))
print('num_triangle - '+ str(g.getNumtri()))
