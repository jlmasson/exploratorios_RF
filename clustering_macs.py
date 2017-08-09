import networkx as nx
#import matplotlib.pyplot as plt
#import pandas as pd

'''data = pd.read_csv('datasets/aeropuertoPeso2.csv', index_col=False, sep=',')

real = nx.Graph()
elist = [tuple(x) for x in data.to_records(index=False)]
real.add_weighted_edges_from(elist)'''

nodes = 133518 # Numero de nodos de nuestro grafo.
posiblesArcos = 0.5 * nodes * (nodes-1)
promedio = 1048576/posiblesArcos #Probabilidad para la creacion de un arco

graph = nx.gnp_random_graph(nodes, promedio, seed=2000, directed=False)

c_aleatorio = nx.average_clustering(graph) # Calculo del coeficiente de clustering promedio
c_aleatorio

nx.write_gexf(real, "real.gexf")


#Gerardo Vera (Gerente Comercial)
#vera@compsesa.com.ec

#Claudia Franco (Business Developer)
#claudia.franco@compsesa.com.ec