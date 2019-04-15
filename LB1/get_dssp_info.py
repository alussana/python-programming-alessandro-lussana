import sys

# hard coded maximum theoretical solvent accessibility
Norm_Acc={"A" :106.0, "B" :160.0,\
         "C" :135.0, "D" :163.0, "E" :194.0,\
         "F" :197.0, "G" : 84.0, "H" :184.0,\
         "I" :169.0, "K" :205.0, "L" :164.0,\
         "M" :188.0, "N" :157.0, "P" :136.0,\
         "Q" :198.0, "R" :248.0, "S" :130.0,\
         "T" :142.0, "V" :142.0, "W" :227.0,\
         "X" :180.0, "Y" :222.0, "Z" :196.0}

def get_dssp_info(dsspfile, ch):
    c = 0 # state variable to assess 'you are in a chain, so do parsing' status
    with open(dsspfile) as f:
        dssp = []
        for line in f:
            
            if line.find('  #  RESIDUE') == 0:
                c = 1
                continue
            
            if c == 0:
                continue

            if line[11] == ch or ch == ' ':
                r = line[13]
                pos = line[5:10].strip()
                ss = line[16]
                if ss == ' ':
                    ss = 'C'
                acc = float(line[35:38])
                phi = float(line[103:109])
                psi = float(line[109:115])
                racc = acc / Norm_Acc[r]
                if racc > 1:
                    racc = 1.0
                v = [pos, r, ss, racc, phi, psi]
                dssp.append(v)

    return(dssp)

if __name__ == '__main__':
    dsspfile = sys.argv[1]
    ch = sys.argv[2]
    dssp = get_dssp_info(dsspfile, ch)
    for i in dssp:
        print(i)
