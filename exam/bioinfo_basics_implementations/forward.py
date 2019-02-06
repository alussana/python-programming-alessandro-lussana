## pseudo code Forward algorithm
## =================================================================================
## setup:
##      store the model's parameters:
##          states: list of state names, order is consistent with t,e,startp,endp
##          t: matrix of transition prob (K states) 
##          e: dictionary of emission prob
##          startp: list of starting prob
##          endp: list of ending prob
##      data:
##          seq: a string, the sequence of N symbols
##      build the forward matrix B with
##          N columns (from position 1 to position N) 
##          K rows
## initialization step:
##      for each k:
##          F(k,0) = startp(k -> BEGIN) * e(k : character at first position)
## recurrence:
##      for n in range(1, N - 1):
##          for each state k:
##              total_score = 0
##              for each state l:
##                  score = F(l,n - 1) * t(l-->k) * e(k : character at position n)
##                  total_score += score
##              F(k,n) = total_score
## termination:
##      initialize total_score = 0
##      for each state k:
##          score = F(k,N - 1) * endp(k --> END)
##          total_score += score
## output:
##      total_score
## =================================================================================
##
## Visual Description, e.g.
##
## K == 4       "number of state"
## N == 10      "length of the sequence"
##
## Matrix F:
##
##      -   A   T   C   G   C   G   A   A   -       
##   
##      |   1   2   3   4   5   6   7   8   |
##  k1  |                                   |
##  k2  |                                   |
##  k3  |                                   |
##  k4  |                                   |
##
## ===============================================================================  
## implementation

def compute_matrix(t, e, startp, endp, seq):
    ## initialize empty forward matrix
    N = len(seq)    ## number of positions in the list
    K = len(t)      ## number of different states
    F = [[0] * N for i in range(K)]

    ## initialization:
    for k in range(K):
        F[k][0] = startp[k] * e[k][seq[0]]

    ## recurrence step:
    for i in range(1, N):
        for k in range(K):
            total_score = 0
            for l in range(K):
                score = F[l][i - 1] * t[l][k] * e[k][seq[i]]
                total_score += score
            F[k][i] = total_score

    ## termination:
    total_score = 0
    for k in range(K):
        score = F[k][N - 1] * endp[k]
        total_score += score

    return(F, total_score)

if __name__ == '__main__':
    ## dummy data:
    ## dummy sequence
    seq = "ATCGCGAA"    ## length is 8
    ## dummy parameters
    ## states and symbols order are consistent with t and e
    states = ["Y","N"]
    t = [[0.7,0.3],[0.3,0.7]]                       ## transition probabilities
    e = [{"A":0.1,"T":0.1,"C":0.4,"G":0.4},\
        {"A":0.25,"T":0.25,"C":0.25,"G":0.25}]      ## emission probabilities
    startp = [0.2,0.8]                              ## starting probabilities
    endp = [0.0,1.0]                                ## ending probabilities
    F, total_score = compute_matrix(t, e, startp, endp, seq)
    ## display result
    print("forward matrix")
    for row in F:
        print(row)
    print("total score = %f" %(total_score))