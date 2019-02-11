''' pseudo code
    input:
        scoring matrix is a dictionary of dictionaries
        seq1 is a string of character starting with "-"
        seq2 is a string of character starting with "-"
        d is gap penalty
    initialization:
        n1 is length seq1
        n2 is length seq2
        initialize the matrix M(n2 x n1)
        initialize the matrix B(n2-1 x n1-1)
    recurrence:
        for each row in M
            for each col in M
                gap1 = M[row][col - 1] - d
                gap2 = M[row - 1][col] - d
                match = M[row - 1][col - 1] + scoring[seq1[row]][seq2[col]]
                return the index of the max score between gap1, gap2, match, 0
                
'''

def find_max(scores):
    max_score = max(scores)
    max_path = []
    for i in range(len(scores)):
        if scores[i] == max_score:
            max_score = scores[i]
            max_path.append(i)
    return(max_score, max_path)

def prettyMatrix(M):
    for row in M:
        print(row)
    print()

if __name__ == '__main__':
    # imported params
    scoring = { "A":{"A":2, "C":-1, "T":-1, "G":0},\
                "C":{"A":-1, "C":2, "T":0, "G":-1},\
                "T":{"A":-1, "C":0, "T":2, "G":-1},\
                "G":{"A":0, "C":-1, "T":-1, "G":2}}
    d = 2
    seq1 = "-ACCA"
    seq2 = "-ACTGG"
    n1 = len(seq1)
    n2 = len(seq2)

    # initialization
    M = [[0 for i in range(n2)] for y in range(n1)]
    B = [[0 for i in range(n2)] for y in range(n1)]

    # iteration to fill the matrix M and B
    for row in range(1, n1):
        for col in range(1, n2):
            gap1 = M[row][col - 1] - d
            gap2 = M[row - 1][col] - d
            match = M[row - 1][col - 1] + scoring[seq1[row]][seq2[col]]
            max_score, max_path = find_max([gap1, gap2, match, 0])
            M[row][col] = max_score
            B[row][col] = max_path

    # find alignment last position in M
    max_score = -1
    max_row = 0
    max_col = 0
    for pointer_row in range(len(M)):
        for pointer_col in range(len(M[0])):
            if M[pointer_row][pointer_col] >= max_score:
                max_score = M[pointer_row][pointer_col]
                max_row = pointer_row
                max_col = pointer_col

    # backtrace, only one optimal path is printed
    pointer_row = max_row
    pointer_col = max_col
    score = M[pointer_row][pointer_col]
    alignment = {"seq1":"", "seq2":""}
    while score != 0:
        backtrace = B[pointer_row][pointer_col]
        trace = backtrace[len(backtrace) - 1]
        if trace == 0:
            alignment["seq1"] = alignment["seq1"] + "-"
            alignment["seq2"] = alignment["seq2"] + seq2[pointer_col]
            pointer_col += -1
        elif trace == 1:
            alignment["seq1"] = alignment["seq1"] + seq1[pointer_row]
            alignment["seq2"] = alignment["seq2"] + "-"
            pointer_row += -1
        elif trace == 2:
            alignment["seq1"] = alignment["seq1"] + seq1[pointer_row]
            alignment["seq2"] = alignment["seq2"] + seq2[pointer_col]
            pointer_col += -1
            pointer_row += -1
        score = M[pointer_row][pointer_col]
        #print(score)

    alignment["seq1"] = alignment["seq1"][::-1]
    alignment["seq2"] = alignment["seq2"][::-1]

    # print matrices
    prettyMatrix(M)
    prettyMatrix(B)

    # print results
    print(alignment["seq1"])
    print(alignment["seq2"])