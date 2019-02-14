#!python3

#====================================================================================================================

# IMPORT MODULES

import numpy as np 

#---------------------------------------------------------------------------------------------------------------------

# VARIABLES

#====================================================================================================================

# FUNCTIONS

def loadCVS(filename, row_labels=False, column_labels=False):
	data = np.genfromtxt(filename, delimiter=',', dtype=np.str)

	if row_labels == True and column_labels == False:
		my_data={}
		for r in data:
			my_data[r[0]] = r[1:]
	elif row_labels == False and column_labels == True:
		my_data={}
		for c in data[0]:
			my_data[c]=[]
		for r in data[1:]:
			for c,n in zip(data[0],r):
				my_data[c].append(n)
	elif row_labels == True and column_labels == True:
		my_data={}
		for n,col in enumerate(data[0]):
			my_data[col] = {}
			for row in data[1:]:
				my_data[col][row] = 


	return data
