## pseudo code Backward algorithm
## ================================================================================
## setup:
## -   read the model's parameters from a file
## -   store the model's parameters in two matrices:
## -   -   t: one for the transition prob (K states) 
## -   -   e: one for the emission prob (A characters)
## -   read the sequence of N symbols
## -   store the sequence of symbols in a string
## -   build the backward matrix B with
## -   -   N columns (from position 1 to position N) 
## -   -   K rows
## initialization step:
## -   for each k:
## -   -   M(k,N) = t(k -> E)
## recurrence:
## -   for n in range(N-1,-1,-1):
## -   -   for each state k:
## -   -   -   total_score = 0
## -   -   -   for each state l:
## -   -   -   -   score = B(l,n + 1) * t(k-->l) * e(l : character at position n+1)
## -   -   -   -   total_score += score
## -   -   -   M(k,n) = total_score
## termination:
## -   initialize total_score = 0
## -   for each state k:
## -   -   score = B(k,1) * e(k : character at position 1) * t(BEGIN --> k)
## -   -   total_score += score
## return(total_score)
## ================================================================================
##
## Visual Description
##
## K == 4       "number of state"
## N == 10      "length of the sequence"
##
## Matrix B:
##
##      -   A   T   C   G   C   G   G   A   A   T   -          
##      |   1   2   3   4   5   6   7   8   9   10  |
##  k1  |                                           |
##  k2  |                                           |
##  k3  |                                           |
##  k4  |                                           |
## ===============================================================================  
## implementation

## dummy data:
## dummy sequence
seq = "ATCGCGAA"    ## length is 8
## dummy parameters
## states and symbols order are consistent with t and e
states = ["Y","N"]
t = [[0.7,0.3],[0.3,0.7]]                       ## transition probabilities
e = [{"A":0.1,"T":0.1,"C":0.4,"T":0.4},\
    {"A":0.25,"T":0.25,"C":0.25,"T":0.25}]   ## emission probabilities
startp = [0.2,0.8]                              ## starting probabilities
endp = [0.0,1.0]                                ## ending probabilities

## initialize empty backward matrix
N = len(seq)    ## number of positions in the list
K = len(t)      ## number of different states
B = [[0] * N for i in range(K)]

## initialization:
position = K - 1 ## matrix col pointer
for k in range(K):
    B[k][position] = endp[k]

## recurrence step:
for i in range(position - 1, -1, -1):
    for k in range(K):
        total_score = 0
        for l in range(K):
            score = B[l][i + 1] * t[k][l] * e[l][seq[i]]
            total_score += score
        B[k][i] = total_score

## termination:
total_score = 0
for k in range(K):
    score = B[k][0] * e[k][seq[i]] * startp[k]
    total_score += score

## return value
print(total_score)