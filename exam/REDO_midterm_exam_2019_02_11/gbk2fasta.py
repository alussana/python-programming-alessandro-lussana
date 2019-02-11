def gbk2fasta(in_path, out_path):
    fasta = open(out_path, "w")
    
    # search for header info
    with open(in_path) as gbk:
        id = False
        specie = False
        for line in gbk:
            line = line.strip()
            line = line.split()
            if line[0] == "ACCESSION":
                info = line[1].split("|")
                id = info[0]
            elif line[0] == "ORGANISM":
                specie = line[1] + " " + line[2]
            if id != False and specie != False:
                print(">%s|%s" %(id, specie), file=fasta)
                break
    
    # search for sequence info
    with open(in_path) as gbk:
        origin = False
        for line in gbk:
            line = line.strip()
            line = line.split()
            if origin == False:
                if len(line) >= 1:
                    if line[0] == "ORIGIN":
                        origin = True
            elif line[0] == "//":
                break
            else:
                line.pop(0)
                seq = ''.join(line)
                print(seq.upper(), file=fasta)
            
# command line interface
if __name__ == '__main__':
    print("=== gtk to fasta ===")
    in_path = input("Input file name: ")
    out_path = input("Output file name: ")
    gbk2fasta(in_path, out_path)
