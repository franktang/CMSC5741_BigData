#!/usr/bin/python

import numpy as np
import operator


node_list = {}
rank_list = {}
node_size = 875713
beta = 0.8

def load_file():
	current_node = None
	current_node_list = {};
	count = 0
	with open("web-Google.txt") as f:
		for i in xrange(4):
			f.readline()
		for line in f:
			from_node, to_node = line.split("\t", 1)
			from_node = from_node.strip()
			to_node = to_node.strip()
			if (current_node == from_node):
				current_node_list[to_node]=True
				count += 1
			else:
				if (current_node):
					for key in current_node_list.iterkeys():
						update_nodelist(key, current_node, count)
				current_node_list.clear()
				current_node = from_node
				current_node_list[to_node]=True
				count = 1
		if (current_node == from_node):
			for key in current_node_list.iterkeys():
				update_nodelist(key, current_node, count)
				
		#print(node_list)
				
def update_nodelist(key, current_node, count):
	if (not node_list.has_key(key)):
		node_list[key] = {}
		init_ranklist(key)
	node_list[key][current_node] = 1.0/count
	
	
def init_ranklist(key):
	if (not rank_list.has_key(key)):
		rank_list[key] = 1.0/node_size
		
def power_iteration():
	temp_rank_list = {}
	rank = 0.
	for key, from_node_list in node_list.iteritems():
		rank = (1-beta)*(1.0/node_size)
		for from_key, value in from_node_list.iteritems():
			if (rank_list.has_key(from_key)):
				rank += beta * rank_list[from_key] * value
		temp_rank_list[key] = rank		
	rank_list.update(temp_rank_list)
	temp_rank_list.clear()
	
				
load_file()
for i in xrange(1):
	power_iteration()
sorted_rank = sorted(rank_list.items(), key=operator.itemgetter(1), reverse=True)
f = open("result.txt", "w")
for i in xrange(100):
	f.write("\t".join(str(x) for x in sorted_rank[i]) + "\n")
f.close()