#!usr/bin/python
import sys

def parse_aln(alnfile):
	'''merge togheter the aligned sequences that have the same identifier'''
	d = {}
	f = open(alnfile)
	for line in f:
		line = line.strip()
		v = line.split()
		d[v[0]] = d.get(v[0], '')
		d[v[0]] = d[v[0]] + v[1]
		return(d)

if __name__ == '__main__':
	alnfile = sys.argv[1]
	d = parse_aln(alnfile)
	for key in d.keys():
		print(key,d[key])