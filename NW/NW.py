import numpy as np
import sys
import math

## TODO take fasta in input

class NW_matrix(object):
    def __init__(self, A, A_path, seq1, seq2):
        self.A = A
        self.path = A_path
        self.seq1 = seq1
        self.seq2 = seq2

class alignment(object):
    def __init__(self, seqA, seqB, score):
        self.seqA = seqA
        self.seqB = seqB
        self.score = score
    def display(self):
        print("Score: %f" %(self.score))
        print("A: %s" %(self.seqA))
        print("B: %s" %(self.seqB))

def print_help_page():
    ## TODO make this shit readable with some smart lib
    print("\n=== Needleman-Wunsch Algorithm ===\n\nSYNOPSIS:\
            \n\npython3 NW.py <TYPE> <SCORE_MATRIX> <SEQUENCE1> <SEQUENCE2> <GAP>\
            \n\ntype                    \"NT\" or \"AA\" \
            \nscore_matrix            symmetrical matrix, order of col and rows is A,C,T,G\
            \nsequence1               fasta file\
            \nsequence2               fasta file\
            \ngap                     gap linear score (must be positive)\n\n")

def compute_matrix(seq1, seq2, score_matrix, d, symbol_dict):
    
    ## initialize A and A_path
    n_seq1 = len(seq1)
    n_seq2 = len(seq2)

    A = np.zeros((n_seq1, n_seq2))
    A_path = np.zeros((n_seq1, n_seq2))

    ## initialize pointer
    pointer = [-1,-1]

    ### Iteration ###
    for symbol1 in seq1:
        pointer[0] = pointer[0] + 1
        pointer[1] = -1
    
        for symbol2 in seq2:
            pointer[1] = pointer[1] + 1
            
            if pointer[0] == 0 and pointer[1] == 0:
            
                A[pointer[0]][pointer[1]] = 0
                A_path[pointer[0]][pointer[1]] = 0
        
            else:
            
                score = [-math.inf] * 3

                if pointer[0] > 0 and pointer[1] > 0:
                    score[0] = A[pointer[0] - 1][pointer[1] - 1] + score_matrix[symbol_dict.get(symbol1)][symbol_dict.get(symbol2)]
            
                if pointer[0] > 0: 
                    score[1] = A[pointer[0] - 1][pointer[1]] - d
            
                if pointer[1] > 0:
                    score[2] = A[pointer[0]][pointer[1] - 1] - d

                A[pointer[0]][pointer[1]] = max(score)
            
                ## memo path_notation
                ## 0 : nothing
                ## 1 : match
                ## 2 : insertion in seq1
                ## 3 : insertion in seq2
                path_notation = "" 
            
                for i in range(len(score)):

                    if max(score) == score[i]:
                        path_notation = path_notation + str(i + 1)

                A_path[pointer[0]][pointer[1]] = path_notation

    return(NW_matrix(A, A_path, seq1, seq2))

def backtrace(NW_matrix):
    ## memo
    ## seq1 must refer to the rows of NW_matrix.A
    ## seq2 must refer to the cols of NW_matrix.A

    pointer = [len(NW_matrix.A) - 1, len(NW_matrix.A[0]) - 1]
    score = NW_matrix.A[pointer[0]][pointer[1]]

    seqA = ""
    seqB = ""

    while pointer[0] > 0 and pointer[1] > 0:
        directions = NW_matrix.path[pointer[0]][pointer[1]]
        
        ## TODO: store also equivalent alignments
        directions = int(str(directions)[0])

        if directions == 1:
            seqA = seqA + NW_matrix.seq1[pointer[0]]
            seqB = seqB + NW_matrix.seq2[pointer[1]]
            pointer[0] = pointer[0] - 1
            pointer[1] = pointer[1] - 1
        
        elif directions == 2:
            pointer[0] = pointer[0] - 1
            seqA = seqA + NW_matrix.seq1[pointer[0]]
            seqB = seqB + "-"

        elif directions == 3:
            seqA = seqA + "-"
            seqB = seqB + NW_matrix.seq2[pointer[1]]
            pointer[1] = pointer[1] - 1

    return(alignment(seqA[::-1], seqB[::-1], score))

def NW_setup(type_of_alignment, score_matrix_name, seq1_name, seq2_name, d): 

    ## check type of alignment
    if type_of_alignment != "AA" and type_of_alignment != "NT":
        sys.exit("Type of alignment must be \"NT\" or \"AA\"\n\n")

    ## read, check and pre-process sequences
    file_seq1 = open(seq1_name)
    file_seq2 = open(seq2_name)

    seq1 = file_seq1.read()
    seq1 = seq1.replace("\n","")
    seq1 = "0" + seq1

    seq2 = file_seq2.read()
    seq2 = seq2.replace("\n","")
    seq2 = "0" + seq2

    ## TODO check the presence of non legal characters using regular expressions
    ## sys.exit("Sequences contain at least one illegal character\n\n")

    ## set the symbol_dictionary between indeces and symbols
    if type_of_alignment == "NT":
        symbol_dict = {"A": 0, "C": 1, "T": 2, "G": 3}
    
    ## TODO add AA symbol_dict

    ## read and check score_matrix
    score_matrix = np.loadtxt(score_matrix_name)

    ## TODO check the score_matrix

    ## read and check the gap penalty
    d = int(d)
    ## TODO check the gap penalty for being a positive int
    
    return([seq1,seq2,score_matrix,d,symbol_dict])

################
### tmp test ###

## check number of arguments
if len(sys.argv) != 6 and len(sys.argv) != 1:
    sys.exit(
            "E: wrong number of arguments\n\n")
elif len(sys.argv) == 1:
    print_help_page()
    sys.exit()

type_of_alignment = sys.argv[1]
score_matrix_name = sys.argv[2]
seq1_name = sys.argv[3] 
seq2_name = sys.argv[4]
d = sys.argv[5]

NW_input = NW_setup(type_of_alignment,score_matrix_name,seq1_name,seq2_name,d)
## test
#print(NW_input)
my_NW = compute_matrix(NW_input[0],NW_input[1],NW_input[2],NW_input[3],NW_input[4])
print(my_NW.A)
print(my_NW.path)

my_backtrace = backtrace(my_NW)
my_backtrace.display()
