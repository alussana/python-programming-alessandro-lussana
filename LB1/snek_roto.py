class Xstructure(object):
    def __init__(self, num, res_pos, res_name, chains, atm, occupancy, b_factor, coords):
        self.num = num
        self.res_pos = res_pos
        self.res_name = res_name
        self.chain = chains
        self.atm = atm
        self.occupancy = occupancy
        self.b_factor = b_factor
        self.coords = coords
    def coordsFromChain(self, ch):
        ch = list(ch)
        indexes = [i for i,e in enumerate(self.chain) if e in ch]
        filtered_coords = [i for i in self.coords if self.coords.index(i) in indexes]
        return(filtered_coords)

def get_Xstructure(filename, ch_id=['A'], atom="CA"):
    num = []
    coords = []
    res_name = []
    res_pos = []
    chains = []
    occupancy = []
    b_factor = []
    atm = []
    with open(filename) as pdb:
        for line in pdb:
            line = line.strip()
            line = line.split()
            line = list(filter(None, line))
            if line[0] == 'ATOM' and line[2] == atom and line[4] in ch_id:
                coords.append({'x':line[6], 'y':line[7], 'z':line[8]})
                res_name.append(line[3])
                res_pos.append(line[5])
                chains.append(line[4])
                atm.append(line[2])
                occupancy.append(line[9])
                b_factor.append(line[10])
                num.append(line[1])
    xstructure = Xstructure(num, res_pos, res_name, chains, atm, occupancy, b_factor, coords)
    return(xstructure)

if __name__ == '__main__':
    print("\n\t\t\t=== snek_roto ===\n")
    print("\tThe ROtation TOol for structural alignment of pdb files\n")
    print("\t\t\t\t-\n")
    print("You can align two structures from the command line")
    print("or import this module in Python to use all the functionalities\n")
    ## insert PDB files and chains
    #filename_1 = input("PBD file 1 path: ")
    #chain_1 = input("Chain identifier for file 1: ")
    #filename_2 = input("PBD file 2 path: ")
    #chain_2 = input("Chain identifier for file 2: ")
    
    ## hard coded some vars to test
    ## note that 5a22.pdb is strangely formatted, str.splice() will not work properly
    xstructure1 = get_Xstructure("5e4v.pdb")
    for i in xstructure1.coords:
        print(i)