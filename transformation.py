import pandas as pd
import csv
from collections import Counter
import math
import itertools 
import networkx as nx 

# option to view max columns and rows
#
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)


lines = []
with open('book2.csv', encoding='utf-8-sig') as file:
    csvReader = csv.reader(file, delimiter=';')
    for row in csvReader:
        lines.append(row)

signatories ={}

for i in range(len(lines)):
    signatories[i]=lines[i]


def ttlCount(dictionary):
	
	count = 0
	ttl_elements = 0

	while ttl_elements < len(list(dictionary)):
		for index, list_of_country in dictionary.items():
			each_count = len(list_of_country)
			ttl_elements += each_count
			count += 1
	return ttl_elements


def stripTextSpace(dictionary):
	ref = {}
	for i, j in dictionary.items():
		d1 = []
		for k in j:
			d1.append(k.strip())
		ref[i] = d1
	return ref


def replaceEachItem(dic1, dic2):
	ref = {}
	
	for i, j in dic1.items():
		d = []
		for k in j:
			for i1, j1 in dic2.items():
				if k == j1:
					x = j1.replace(k, i1)
					d.append(x)
		ref[i] = d
	return ref

def create_edges(iterable_dict, r=2):
	"""
	Creates edges.
	
	:param      iterable_dict:  The iterable dictionary
	:type       iterable_dict:  { type_description }
	:param      r:              { number of elements in a tuple }
	:type       r:              number
	
	:returns:   { description_of_the_return_value }
	:rtype:     { return_type_description }
	"""
	possible_variation = []

	permut = itertools.combinations(iterable_dict, r)
	
	for i in permut:
		possible_variation.append(i)
	return possible_variation


def distance(origin, destination):
    """
    Calculate the Haversine distance.

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6378.137  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d

# stripping the whitespace in a string 
stripped = stripTextSpace(signatories)
ttl_stripped = [len(f) for f in stripped.values()]
#print('sum of ttl_stripped:', sum(ttl_stripped))
#for i in range(len(stripped)):
#	print(i, stripped[i])


# loading the country, alpha3 code to convert my stripped  
frames = pd.read_csv('country_alpha.csv')
#print('\n frames', frames)
frames_dict = dict(zip(frames.alpha3, frames.country))
ttl_frames = [len(f) for f in frames_dict.values()]
#print('\n', sum(ttl_frames))


# replacing the country with alpha3 code 
converted = replaceEachItem(stripped, frames_dict)

ttl_converted = [len(f) for f in converted.values()]

#for i in range(len(converted)):
#	print('\n', i, len(converted[i]), converted[i])

#print('sum of ttl converted:', sum(ttl_converted))
"""
print('looking for CAM ...')
for i, j in converted.items():
	for each in j:
		if each == 'CAM':
			print(i, j)
"""


# creating a number of edges for a networkx
ref1 = {}
for i in range(len(converted)):
	combi = create_edges(converted[i])
	ref1[i] = combi

#for i in range(len(ref1)):
#	print('\n', i, len(ref1[i]), ref1[i])

first = []
second = []
for key, list_of_edges in ref1.items():
	for each_edge in list_of_edges:
		first.append(each_edge[0])
		second.append(each_edge[1])

# to save in csv format 
converted_to_frame = {
	'first': first,
	'second': second
}

#pd.DataFrame(converted_to_frame).to_csv('total_edges.csv')


graph_pandas = pd.DataFrame(converted_to_frame)


# loading geolocation including alpha3, latitude, longitude
country_alpha3 = pd.read_csv('world.csv')

def createAlphaLatLon_dict(dataframe, col1, col2, col3):
	lat_lon = list(zip(dataframe[col2].to_list(), dataframe[col3].to_list()))
	ref1 = dict(zip(dataframe[col1].to_list(), lat_lon))
	return ref1



geo_dict = createAlphaLatLon_dict(country_alpha3, col1='alpha3', col2='latitude', col3='longitude')

#first = frames['first'].to_list()
#second = frames['second'].to_list()

edge_list = list(zip(first, second))

dstnce = []
for ind, edge in enumerate(edge_list):

	loc1 = geo_dict[edge[0]]
	loc2 = geo_dict[edge[1]]
	calculated = round(distance(loc1, loc2), 1)
	dstnce.append(calculated)

graph_pandas['distance'] = dstnce

#graph_pandas.to_csv('graph_pandas_weighted.csv')
#print(graph_pandas.head())
#print(len(graph_pandas))
#
#
# Total countries in the RTAs
#urt = []
#for each in stripped.values():
#	for el in each:
#		urt.append(el)


geo_lo = pd.read_csv('geo_location.csv')
print(geo_lo.info())

