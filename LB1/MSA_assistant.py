#!usr/bin/python
import sys
import numpy as np

def parse_aln(alnfile):
	'''merge together the aligned sequences that have the same identifier'''
	d = {}
	f = open(alnfile)
	for line in f:
		line = line.strip()
		v = line.split()
		if len(v) == 2:
			d[v[0]] = d.get(v[0], '')
			d[v[0]] = d[v[0]] + v[1]
	return(d)

def get_profile(d_aln, pos):
	'''compute the profile of the position pos from an alignment stored in a dictionary'''
	lr = 'ACDEFGHIKLMNPQRSTVWY' # initialize the AA string
	prof = np.zeros(20) # initialize the inner list of the profile, for 20 AA
	ks = d_aln.keys() # sequences
	for k in ks:
		res = d_aln[k][pos]
		i = lr.find(res) # if no residue is found in that position, it returns -1
		if i > -1:
			prof[i] += 1
	return(prof / float(np.sum(prof)))

if __name__ == '__main__':
	# vars and tests are temporarily hard coded

	# usage: MSA_assistant.py alnfile.aln

	# test this: python MSA_assistant.py uniprot2clustalw/all_seqs.aln
	alnfile = sys.argv[1]
	d = parse_aln(alnfile)
	
	#for key in d.keys():
	#	print(key,d[key])
	
	prof = get_profile(d,36)

	aa = list('ACDEFGHIKLMNPQRSTVWY')
	for i in range(0,len(aa)):
		print(aa[i], prof[i])