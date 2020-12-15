import pandas as pd
import matplotlib.pyplot as plt 
import networkx as nx
import numpy as np

file = pd.read_csv('graph_pandas_weighted.csv')
data = file[['first', 'second', 'distance']]


bb = nx.from_pandas_edgelist(data, 'first', 'second', 'distance', nx.Graph())


dgree = []
for i in bb.nodes():
	k = bb.degree(i)
	dgree.append(k)

nx.draw_kamada_kawai(bb, dist = data['distance'], weight=dgree, with_labels=True,
	node_size=dgree, node_color='blue',
	edge_color='gray', font_size=8)

#plt.show()



def getDistance(graph, country):
	li = []
	for j in graph[country].values():
		li.append(j['distance'])
	return li

#usa_ave = getAveDistance(bb, 'USA')


def getDistanceFrame(graph, country):
	dist = getDistance(graph, country)
	nodes = [f for f in graph[country]]

	data = {
		'country': nodes,
		'distance_km': dist}
	return pd.DataFrame(data)

#print('USA', usa1)
#print('\n', 'JPN', jpn1)
#print('\n', 'DEU', deu1)

usa1 = getDistanceFrame(bb, 'USA')
jpn1 = getDistanceFrame(bb, 'JPN')
deu1 = getDistanceFrame(bb, 'DEU')

for nation in bb['JPN']:
	countries = getDistanceFrame(bb, nation)
	print('\n', nation, countries)

