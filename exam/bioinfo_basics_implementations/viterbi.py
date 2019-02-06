def prettyMatrix(M):
    for row in M:
        print(row)

def find_max(scores):
    max_score = max(scores)
    max_states = []
    for i in range(len(scores)):
        if scores[i] == max_score:
            max_score = scores[i]
            max_states.append(i)
    return(max_score, max_states)

if __name__ == '__main__':
    # dummy sequence
    seq = "ATCGCGAA"
    ## dummy parameters
    ## states and symbols order are consistent with t and e
    states = ["Y","N"]
    t = [[0.7,0.3],[0.3,0.7]]                       ## transition probabilities
    e = [{"A":0.1,"T":0.1,"C":0.4,"G":0.4},\
        {"A":0.25,"T":0.25,"C":0.25,"G":0.25}]      ## emission probabilities
    startp = [0.2,0.8]                              ## starting probabilities
    endp = [0.0,1.0]                                ## ending probabilities

    # inizialize matrix V with
    V = [[0 for i in range(len(seq) + 1)] for y in range(len(states))]
    B = [[0 for i in range(len(seq) + 1)] for y in range(len(states))]

    # fill the first col in V
    for i in range(len(states)):
        V[i][0] = startp[i] * e[i][seq[0]]

    # fill the first col in B
    for i in range(len(states)):
        B[i][0] = "BEGIN"

    # recurrence
    for pos in range(1, len(seq)):
        for k in range(len(states)):
            scores = []
            for l in range(len(states)):
                score = V[l][pos - 1] * t[l][k] * e[k][seq[pos]]
                scores.append(score)
            max_score, max_states = find_max(scores)
            V[k][pos] = max_score
            B[k][pos] = max_states

    # termination
    for k in range(len(states)):
        scores = []
        for l in range(len(states)):
            score = V[l][len(seq) - 1] * endp[k]
            scores.append(score) 
        max_score, max_states = find_max(scores)
        V[k][len(seq)] = max_score
        B[k][len(seq)] = max_states

    prettyMatrix(V)
    print()
    prettyMatrix(B)