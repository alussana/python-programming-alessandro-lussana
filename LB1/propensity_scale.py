#!/usr/local/bin/python3

def pretty_dictionary(D):
    print()
    for element in D:
        print(element, D[element][0:3])
    print()

def propensity(filename):
    FILE_IN = open(filename)
    RESIDUES = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
    STRUCTURES = ['B', 'C', 'E', 'G', 'I', 'H', 'S', 'T' ]
   
    RES_DICT = dict([(res, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) for res in RESIDUES]) ## [num_res, H, E, C]
    STRUCT_DICT = dict([(struct, 0.0) for struct in STRUCTURES])
    
    for line in FILE_IN:
        sequence = line.split()[0]
        structure = line.split()[1]

        for character in range(len(structure)):
            
            if sequence[character] not in RES_DICT: continue ## just for working with the traditional 20 aa
            RES_DICT[sequence[character]][0] += 1

            if structure[character] == 'H':
                RES_DICT[sequence[character]][1] += 1
                STRUCT_DICT['H'] += 1
            
            elif structure[character] == 'E':
                RES_DICT[sequence[character]][2] += 1
                STRUCT_DICT['E'] += 1
            
            elif structure[character] == 'C':
                RES_DICT[sequence[character]][3] += 1
                STRUCT_DICT['C'] += 1
   
    ###########################################################
    ###             PROPENSITY definition                   ###
    ### P(residue, sec_struct) / P(residue) * P(sec_struct) ###
    ###########################################################
    
    LEN_SEQ = 0.0
    for key in RES_DICT:
        LEN_SEQ += RES_DICT[key][0]
    
    HELIX_DICT = dict((res, [0.0, 0.0, 0.0]) for res in RESIDUES)
    STRAND_DICT = dict((res, [0.0, 0.0, 0.0]) for res in RESIDUES)
    COIL_DICT = dict((res, [0.0, 0.0, 0.0]) for res in RESIDUES)

    for residue in RESIDUES:
        HELIX_DICT[residue][0:2] = RES_DICT[residue][0:2]
        
        STRAND_DICT[residue][0] = RES_DICT[residue][0]
        STRAND_DICT[residue][1] = RES_DICT[residue][2]

        COIL_DICT[residue][0] = RES_DICT[residue][0]
        COIL_DICT[residue][1] = RES_DICT[residue][3]

        RES_DICT[residue][4] = HELIX_DICT[residue][2] = round((RES_DICT[residue][1] / LEN_SEQ) / ((RES_DICT[residue][0] / LEN_SEQ)*(STRUCT_DICT['H'] / LEN_SEQ)), 2)
        RES_DICT[residue][5] = STRAND_DICT[residue][2] = round((RES_DICT[residue][2] / LEN_SEQ) / ((RES_DICT[residue][0] / LEN_SEQ)*(STRUCT_DICT['E'] / LEN_SEQ)), 2)
        RES_DICT[residue][6] = COIL_DICT[residue][2] = round((RES_DICT[residue][3] / LEN_SEQ) / ((RES_DICT[residue][0] / LEN_SEQ)*(STRUCT_DICT['C'] / LEN_SEQ)), 2)

    '''
    If propensity has to be shown as a logarithmic function of frequency

    for residue in RESIDUES:
        RES_DICT[residue][4] = round(log2((RES_DICT[residue][1] / LEN_SEQ) / ((RES_DICT[residue][0] / LEN_SEQ)*(STRUCT_DICT['H'] / LEN_SEQ))), 2)
        RES_DICT[residue][5] = round(log2((RES_DICT[residue][2] / LEN_SEQ) / ((RES_DICT[residue][0] / LEN_SEQ)*(STRUCT_DICT['E'] / LEN_SEQ))), 2)
        RES_DICT[residue][6] = round(log2((RES_DICT[residue][3] / LEN_SEQ) / ((RES_DICT[residue][0] / LEN_SEQ)*(STRUCT_DICT['C'] / LEN_SEQ))), 2)
    '''
    print(LEN_SEQ)
    return(RES_DICT, HELIX_DICT, STRAND_DICT, COIL_DICT)


## Professor function
def something(filename):
    f = open(filename)
    d_seq = {}
    d_ss = {}
    d_pair = {}
    for line in f:
        v = line.rstrip().split()
        if len(v)<2:
            print >> sys.stderr, line
            continue
        n = len(v[0])
        for i in range(n):
            d_seq[v[0][i]] = d_seq.get(v[0][i], 0) + 1
            d_ss[v[1][i]] = d_seq.get(v[1][i], 0) + 1
            k = v(v[0][i], v[1][i])
            d_pair[k] = d_pair.get(k, 0) + 1
    return(d_seq, d_ss, d_pair)

def something_continue(d_seq, d_ss, d_pair, ss):
    ks = d_pair.keys()
    tot = float(sum(d_pair.values()))
    for k in ks:
        if k[1] == ss:
            prop = (d_pair[k]/tot)/(((d_seq[k[0]])/tot)*(d_ss[k[1]]/tot))
        print(k, prop)


if __name__ == '__main__':
    import sys
    import pandas as pd
    from math import log2
    try:
        FILE_IN = sys.argv[1]
    except:
        print('Program Usage: script.py <PREDICTION_FILE.TXT> <THRESHOLD_VALUE>')
        raise SystemExit
    else:
        RES_DICT, HELIX_DICT, STRAND_DICT, COIL_DICT = propensity(FILE_IN)
        #pretty_dictionary(RES_DICT)
        #d_seq, d_ss, d_pair = something(FILE_IN)
        #something_continue(d_seq, d_ss, d_pair, 'H')
        #something_continue(d_seq, d_ss, d_pair, 'E')
        #something_continue(d_seq, d_ss, d_pair, 'C')

        print('\n\n', pd.DataFrame.from_dict(RES_DICT, orient='index', \
            columns = ['# Residue', '# Helix', '# Extended', '# Coil', \
            'Helix propensity', 'Extended propensity', 'Coil propensity']), '\n\n')
        
        print('\n\n', pd.DataFrame.from_dict(HELIX_DICT, orient='index', \
            columns = ['# of residue', '# of helix', 'Helix propensity']), '\n\n')
        
        print('\n\n', pd.DataFrame.from_dict(STRAND_DICT, orient='index', \
            columns = ['# of residue', '# of strand', 'Srand propensity']), '\n\n')
        
        print('\n\n', pd.DataFrame.from_dict(COIL_DICT, orient='index', \
            columns = ['# of residue', '# of coil', 'Coil propensity']), '\n\n')