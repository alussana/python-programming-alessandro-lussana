# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght 
# Use separate functions for the input and the output 


'''
Pseudo-code:
    
    function A:
    -) open the fasta file for reading
    -) initialize the list headers
    -) initialize the list sequences
    -) initialize the string seq
    -) for each line of the fasta file:
    -)      if the line starts with ">":
    -)          strip the line
    -)          append the line as an item of headers
    -)          append seq as an item of sequences
    -)          reinitialize seq as an empty string
    -)      else:
    -)          append the line to seq
    -) append seq as an item of sequences
    -) remove the first item of sequences
    -) return headers and sequences

    function B:
    -) take headers and sequences from function A in input
    -) open a file out_file for writing
    -) for each element of headers:
    -)      split element on "OS=" and store the resulting list in head_items
    -)      split the second item of head_items on " " and store the
            resulting list in head_info
    -)      if in head_info the first item != "Homo" and the second item
            != "sapiens":
    -)          print the first and the second items of head_info on STDIN
    -)          print the length of the sequences' item whose index corresponds
                to the index of element, minus the count of "\n" in that string
    -)          print element on out_file
    -)          print the sequences' item whose index corresponds to the index
                of element on out_file

'''

def store_seq(fasta_file):
    with open(fasta_file) as fasta:
        heads = []
        seqs = []
        seq = ""
        for line in fasta:
            if line[0] == ">":
                line = line.strip()
                heads.append(line)
                seqs.append(seq)
                seq = ""
            else:
                seq = seq + line
        seqs.append(seq)
        seqs.pop(0)
    return([heads, seqs])

def analyze(heads, seqs):
    out_file = open("out_file.fa", "w")
    for i in range(len(heads)):
        head_items = heads[i].split("OS=")
        head_info = head_items[1].split(" ")
        if head_info[0] != "Homo" and head_info[1] != "sapiens":
            print("%s %s" %(head_info[0], head_info[1]))
            print(len(seqs[i]) - seqs[i].count("\n"))
            print(heads[i], file = out_file)
            print(seqs[i], file = out_file)

storing = store_seq("sprot_prot.fasta")
analyze(storing[0], storing[1])
