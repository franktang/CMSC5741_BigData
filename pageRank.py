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
		#Init a node dict, each element represent a node
		#and it contains another sub-dict which stores
		#all the from_nodes which link to that node
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
				
def update_nodelist(key, current_node, count):
	'''
	from_node = current_node
	to_node = key
	'''
	if (not node_list.has_key(key)):
		node_list[key] = {}
		init_ranklist(key)
	node_list[key][current_node] = 1.0/count
	
	
def init_ranklist(key):
	if (not rank_list.has_key(key)):
		rank_list[key] = 1.0/node_size
		
def power_iteration():
	temp_rank_list = {}
	rank = 0.0
	diff = 0.0
	for key, from_node_list in node_list.iteritems():
		rank = (1-beta)*(1.0/node_size)
		for from_key, value in from_node_list.iteritems():
			if (rank_list.has_key(from_key)):
				rank += beta * rank_list[from_key] * value
		temp_rank_list[key] = rank
		diff+=abs(rank_list[key] - rank)	
	rank_list.update(temp_rank_list)
	temp_rank_list.clear()
	return diff
	
				
load_file()
iter_count = 0
iter_diff = 1.0
#Assume convergence if difference less than 0.0000001
while (iter_diff > 0.0000001):
	iter_diff = power_iteration()
	iter_count+=1
	print("%d iteration: the difference is %.10f" % (iter_count, iter_diff))
	
print("iteration completed")

sorted_rank = sorted(rank_list.items(), key=operator.itemgetter(1), reverse=True)
f = open("result.txt", "w")
for i in xrange(100):
	f.write("\t".join(str(x) for x in sorted_rank[i]) + "\n")
f.close()