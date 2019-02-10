def prettyMatrix(M):
    for row in M:
        print(row)
    print()

def find_max(scores):
    max_score = max(scores)
    max_states = []
    for i in range(len(scores)):
        if scores[i] == max_score:
            max_states.append(i)
    return(max_score, max_states)

if __name__ == '__main__':
    # dummy sequence
    seq = "ATCGCGAA-"
    ## dummy parameters
    ## states and symbols order are consistent with t and e
    states = ["Y","N"]
    t = [[0.7,0.3],[0.3,0.7]]                       ## transition probabilities
    e = [{"A":0.1,"T":0.1,"C":0.4,"G":0.4},\
        {"A":0.25,"T":0.25,"C":0.25,"G":0.25}]      ## emission probabilities
    startp = [0.2,0.8]                              ## starting probabilities
    endp = [0.05,0.95]                                ## ending probabilities

    # inizialize matrix V and B
    V = [[0 for i in range(len(seq))] for y in range(len(states))]
    B = [[0 for i in range(len(seq))] for y in range(len(states))]
    for row in range(0,len(states)):
        V[row][0] = round(startp[row] * e[row][seq[0]], 10)
        B[row][0] = "B"

    # recursion
    for pos in range(1, len(seq) -1):
        for k in range(len(states)):
            scores = []
            for l in range(len(states)):
                score = round(V[l][pos - 1] * t[l][k] * e[k][seq[pos]], 10)
                scores.append(score)
            max_score, max_states = find_max(scores)
            V[k][pos] = max_score
            B[k][pos] = max_states

    # termination
    pos += 1
    for k in range(len(states)):
        scores = []
        for l in range(len(states)):
            score = round(V[l][pos - 1] * endp[k], 15)
            scores.append(score)
        max_score, max_states = find_max(scores)
        V[k][pos] = max_score
        B[k][pos] = max_states

    # print matrices and sequence
    prettyMatrix(V)
    prettyMatrix(B)
    print(seq, "\n")

    # traceback one optimal hidden path
    path = ["END"]
    state = B[0][pos][len(B[0][pos]) - 1]
    path.append(state)
    pos -= 1
    for path_pos in range(pos, 0, -1):
        state = B[state][pos][len(B[state][pos]) - 1]
        path.append(state)
        pos -= 1
    path.append("BEGIN")
    path = path[::-1]

    # print path
    print(path)