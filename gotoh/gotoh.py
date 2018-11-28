import numpy as np
import sys

#############################
### setup and input check ###

if len(sys.argv) != 3:
    sys.exit("Wrong number of arguments: two sequences must be provided")

file_seq1 = open(sys.argv[1])
file_seq2 = open(sys.argv[2])

seq1 = read(file_seq1)
seq1 = seq1.replace("\n","")
seq2 = read(file_seq2)
seq2 = seq2.replace("\n","")

## Check the presence of non legal characters using regular expression
## [...]

######################
### Initialization ###

#################
### Iteration ###

###################
### Termination ###
