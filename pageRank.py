#!/usr/bin/python

import numpy as np




def load_file():
  with open("web-Google.txt") as f:
    for i in xrange(3):
      f.readline()
    for line in f:
  	  
X = np.zeros(875713, 875713)
