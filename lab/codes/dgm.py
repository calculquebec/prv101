import networkx as nx
from writeNodesEdges import writeObjects
import sys

if len(sys.argv) == 1:
    print("Usage: python dgm.py <generationNumber>")
    sys.exit(1)

generation = int(sys.argv[1])
H = nx.dorogovtsev_goltsev_mendes_graph(generation)
pos = nx.spring_layout(H, dim=3)
xyz = [list(pos[i]) for i in pos] # list of [x,y,z]

print(nx.number_of_nodes(H), 'nodes and',
      nx.number_of_edges(H), 'edges')
degree = [d for i,d in H.degree(H.nodes())]
writeObjects(xyz, edges=H.edges(), scalar=degree,
        name='degree', power=0.333, fileout='network')
