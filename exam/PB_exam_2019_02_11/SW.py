def find_max(scores):
    max_score = max(scores)
    max_paths = []
    for i in range(len(scores)):
        if scores[i] == max_score:
            max_paths.append(i)
    return(max_score, max_paths)

def SW(s, d, A, B):
    # initialization
    nA = len(A)
    nB = len(B)
    M = [[0 for col in range(nB)] for row in range(nA)]
    BT = [[0 for col in range(nB)] for row in range(nA)]

    # iteration
    for row in range(1, nA):
        for col in range(1, nB):
            gapA = M[row][col - 1] - d
            gapB = M[row - 1][col] - d
            match = M[row - 1][col - 1] + s[A[row]][B[col]]
            scores = [gapA, gapB, match, 0]
            max_score, max_paths = find_max(scores)
            M[row][col] = max_score
            BT[row][col] = max_paths

    # find highest score in M
    best_score = 0
    for row in range(1, nA):
        for col in range(1, nB):
            if M[row][col] >= best_score:
                best_score = M[row][col]
                row_pointer = row
                col_pointer = col

    return(M, BT, [row_pointer, col_pointer])

if __name__ == '__main__':
    A = "-ACCA"
    B = "-ATCGG"
    d = 2
    s = {   "A":{"A": 2, "T": -1, "C": -1, "G": 0},\
            "T":{"A": -1, "T": 2, "C": 0, "G": -1},\
            "C":{"A": -1, "T": 0, "C": 2, "G": -1},\
            "G":{"A": 0, "T": -1, "C": -1, "G": 2}}
    
    scores, backtrace, pointer = SW(s, d, A, B)
    
    print("matrix M")
    for row in scores:
        print(row)
    print()

    print("backtrace")
    for row in backtrace:
        print(row)
    print()

    print("pointer to the max scoring cell in M", "\n", pointer)
