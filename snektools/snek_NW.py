import numpy as np
import sys
import math

class snek_matrix(object):
    def __init__(self, A, A_path, seq1, seq2):
        self.A = A
        self.path = A_path
        self.seq1 = seq1
        self.seq2 = seq2

class alignment(object):
    def __init__(self, seqA_header, seqB_header, seqA, seqB, score):
        self.seqA_header = seqA_header
        self.seqB_header = seqB_header
        self.seqA = seqA
        self.seqB = seqB
        self.score = score
    ## TODO def a method to display every optimal alignment
    #def print_alignment(self):
    #    print("%s\n%s" %(self.seqA_header, self.seqA))
    #    print("%s\n%s" %(self.seqB_header, self.seqB))
    def score(self):
        return(self.score)

def print_help_page():
    ## TODO make this shit readable with some smart lib
    print("\n=== Snek Tools ===\n\nSYNOPSIS:\
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

    return(snek_matrix(A, A_path, seq1, seq2))

def store_alignment(snek_matrix):

    seqA = ""
    seqB = ""
    
    all_paths_resolved = 1
    pointer = [len(snek_matrix.path) - 1, len(snek_matrix.path[0]) - 1]

    while pointer[0] > 0 and pointer[1] > 0:
        
        directions = list(str(int(snek_matrix.path[pointer[0]][pointer[1]])))
        
        ## pop the first direction if there are multiple equivalent directions
        if len(directions) > 1:
            direction = int(directions.pop(0))
            snek_matrix.path[pointer[0]][pointer[1]] = float("".join(directions))
            all_paths_resolved = 0
        else:
            direction = int("".join(directions))

        if direction == 1:
            seqA = seqA + snek_matrix.seq1[pointer[0]]
            seqB = seqB + snek_matrix.seq2[pointer[1]]
            pointer[0] = pointer[0] - 1
            pointer[1] = pointer[1] - 1
        
        elif direction == 2:
            pointer[0] = pointer[0] - 1
            seqA = seqA + snek_matrix.seq1[pointer[0]]
            seqB = seqB + "-"

        elif direction == 3:
            seqA = seqA + "-"
            seqB = seqB + snek_matrix.seq2[pointer[1]]
            pointer[1] = pointer[1] - 1

    return([seqA, seqB, all_paths_resolved])

def snek_backtrace(snek_matrix, seqA_header, seqB_header):
    ## memo
    ## seq1 must refer to the rows of snek_matrix.A
    ## seq2 must refer to the cols of snek_matrix.A

    score = snek_matrix.A[len(snek_matrix.A) - 1][len(snek_matrix.A[0]) - 1]

    stored_seqA = []
    stored_seqB = []
    
    all_path_resolved = 0

    while all_path_resolved == 0:
        
        aligned = store_alignment(snek_matrix)
        stored_seqA.append(aligned[0][::-1])
        stored_seqB.append(aligned[1][::-1])
        all_path_resolved = aligned[2]

    ## TODO reverse the aligned sequences in seqA and seqB lists
    return(alignment(seqA_header, seqB_header, stored_seqA, stored_seqB, score))

def snek_setup(type_of_alignment, score_matrix_file, seq1_file, seq2_file, d): 

    ## check type of alignment
    if type_of_alignment != "AA" and type_of_alignment != "NT":
        sys.exit("Type of alignment must be \"NT\" or \"AA\"\n\n")

    ## read, check and pre-process sequences
    file_seq1 = open(seq1_file)
    file_seq2 = open(seq2_file)

    seq1_header = file_seq1.readline()
    seq1_header = seq1_header.strip()
    seq1 = file_seq1.read()
    seq1 = seq1.replace("\n","")
    seq1 = "0" + seq1

    seq2_header = file_seq2.readline()
    seq2_header = seq2_header.strip()
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
    score_matrix = np.loadtxt(score_matrix_file)
    ## TODO check the score_matrix

    ## read and check the gap penalty
    d = int(d)
    ## TODO check the gap penalty for being a positive int
    
    return([seq1,seq2,score_matrix,d,symbol_dict,seq1_header,seq2_header])

def start_snek(type_of_alignment,score_matrix_file,seq1_file,seq2_file,d):
    snek_input = snek_setup(type_of_alignment,score_matrix_file,seq1_file,seq2_file,d)
    matrix = compute_matrix(snek_input[0],snek_input[1],snek_input[2],snek_input[3],snek_input[4])
    backtrace = snek_backtrace(matrix, snek_input[5], snek_input[6])
    return(backtrace)

def initiate_snek(args):
    
    ## check number of arguments
    if len(sys.argv) != 6 and len(sys.argv) != 1:
        print_help_page()
        sys.exit("E: wrong number of arguments\n\n")
    
    elif len(sys.argv) == 1:
        print_help_page()
        sys.exit()

    type_of_alignment = sys.argv[1]
    score_matrix_file = sys.argv[2]

## start the snek from command line
#initiate_snek(sys.argv)

## or

## test that importing snek module:
'''
import snek_NW as snek
type = "NT"
score_matrix = "scores.txt"
sequence1 = "tardigradum.aquaporin10.fa"
sequence2 = "tardigradum.aquaporin4.fa"
gap = 2
alignment = snek.start_snek(type, score_matrix, sequence1, sequence2, gap)

import snek_NW as snek
type = "NT"
score_matrix = "scores.txt"
sequence1 = "seqA.fa"
sequence2 = "seqB.fa"
gap = 2
alignment = snek.start_snek(type, score_matrix, sequence1, sequence2, gap)

single functions:
snek_input = snek.snek_setup(type,score_matrix,sequence1,sequence2,gap)
matrix = snek.compute_matrix(snek_input[0],snek_input[1],snek_input[2],snek_input[3],snek_input[4])
'''
