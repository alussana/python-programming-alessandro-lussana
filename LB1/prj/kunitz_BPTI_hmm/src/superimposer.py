#!/usr/bin/env python3

import sys
from Bio.SVDSuperimposer import SVDSuperimposer
import numpy as np

def get_atoms(pdbfile,chain,atm='CA'):
    with open(pdbfile) as file:
        lines = file.readlines()
        n = 0
        atoms = []
        for i in lines:
            if i[16] != ' ' and i[16] != 'A':
                i = ''
            if 'ATOM' in i[0:6] and atm in i[12:16] and chain in i[21]:
                n += 1
                atoms.append([
                    float(i[30:38]),
                    float(i[38:46]),
                    float(i[46:54])])

    return(np.array(atoms))

def super_prot(cas1,cas2):
    sup = SVDSuperimposer()
    sup.set(cas1,cas2)
    sup.run()
    return(sup.get_rms())

def dist(p1, p2):
    return(np.sqrt(np.sum((p1-p2)**2)))

if __name__ == '__main__':
    pdb1=sys.argv[1]
    ch1=sys.argv[2]
    pdb2=sys.argv[3]
    ch2=sys.argv[4]

    latm1 = get_atoms(pdb1,ch1)
    latm2 = get_atoms(pdb2,ch2)

    n = len(latm1)

    for i in range(n-1):
        d = dist(latm1[i,], latm1[i+1,])
        print(i,d)
    
    print("MEAN", np.mean(d), "STD", np.std(d))

    if len(latm1) == len(latm2):
        rmsd = super_prot(latm1, latm2)
        print(rmsd)
