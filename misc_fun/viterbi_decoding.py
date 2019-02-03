#################################
## dummy transition probabilities
## MEMO: to ... from ...
t = {   "Y": {"Y":0.7, "N":0.1, "B":0.2, "E":0.0}, \
        "N": {"N":0.8, "Y":0.2, "B":0.8, "E":0.0}, \
        "E": {"Y":0.1, "N":0.1, "B":0.0, "E":0.0},
        "B": {"Y": 0.0, "N":0.0, "B":0.0, "E":0.0}}
#print("dictionary t, key Y is: "t["Y"])

###############################
## dummy emission probabilities
e = {   "Y": {"A":0.1, "C":0.4, "G":0.4, "T":0.1}, \
        "N": {"A":0.25, "C":0.25, "G":0.25, "T":0.25}}
#print(e["Y"])

#################
## dummy sequence
s = "AGCGCGAA"

#################
## list of states
## order of states is meaningful
## order of states is the same as in the viterbi matrix
states = ["B", "Y", "N", "E"]
#print(len(s))

###################
## viterbi decoding
## V is the viterbi matrix
def viterbi(s, t, e, states):
    n = len(s) + 1 ## number of cols of V
    m = len(states) ## number of rows of V
    V = [[0 for col in range(n + 1)] for row in range(m)]

    ## Initialization
    for i in range(m):
        V[i][0] = 1.0

    ## Iteration
    for j in range(1, n):
        #print(j)
        for i in range(1, m - 1):
            #print(i)
            scores = []
            ## for each cell i,j of the matrix V
            ## I need to iterate on the previous states
            ## retrieving the score of i-1,*state*:
            for state in range(0,len(states)):
                score = V[state][j-1] * t[states[i]][states[state]] 
                #print(states[i],states[state],round(score,2),t[states[i]][states[state]])
                scores.append(score)
            
            max_score,max_state = find_max(scores,states)
            V[i][j] = max_score * e[max_state][s[j - 1]] 
    
    return(V)

def find_max(scores,states):
    ## TODO define this function
    for i in scores:
    ## use index i to retrieve max_score and max_state
    ## the order in scores and states is consistent

M = viterbi(s, t, e, states)
def prettyMatrix(M):
    for i in M:
        print(i)


## testThis
prettyMatrix(M)
