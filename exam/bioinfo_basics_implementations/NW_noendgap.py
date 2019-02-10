#   pseudo code for NW with end gap penalty
#   setup of parameters and data
#       scoring: a dict of dicts for the scoring matrix
#       set d: a natural integer for gap penalty
#       seq1: a string for sequence 1, first position is "-"
#       seq2: a string for sequence 2, first position is "-"
#   initialization
#       initialize a matrix M with n1 rows and n2 columns
#       initialize a matrix B with n1-1 rows and n2-1 columns
#   iteration
#       for each row of M except the first
#           for each col of M except the first
#               initialize scores, an empty list
#   [...]

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
    M = [[0 for i in range(n2)] for y in range(n1)]
    B = [[0 for i in range(n2 - 1)] for y in range(n1 - 1)]

    # iteration to fill the matrix M and B
    for row in range(1, n1):
        for col in range(1, n2):
            gap1 = M[row][col - 1] - d
            gap2 = M[row - 1][col] - d
            match = M[row - 1][col - 1] + scoring[seq1[row]][seq2[col]]
            max_score, max_path = find_max([gap1, gap2, match])
            M[row][col] = max_score
            B[row - 1][col - 1] = max_path

    # backtrace, only one path is printed
    total_score = 0
    for col in range(len(M[0]) - 1,-1,-1):
        if M[len(M) - 1][col] > total_score:
            total_score = M[len(M) - 1][col]
            end_pointer_col = col -1
            end_pointer_row = len(M) - 2
    for row in range(len(M) -1,-1,-1):
        if M[row][len(M[0]) - 1] > total_score:
            total_score = M[row][len(M[0]) - 1]
            end_pointer_row = row -1
            end_pointer_col = len(M[0]) - 2
    pointer_col = end_pointer_col
    pointer_row = end_pointer_row
    alignment = {"seq1":"", "seq2":""}
    while pointer_row != -1 or pointer_col != -1:
        backtrace = B[pointer_row][pointer_col]
        trace = backtrace[len(backtrace) - 1]
        if trace == 0:
            alignment["seq1"] = alignment["seq1"] + "-"
            alignment["seq2"] = alignment["seq2"] + seq2[pointer_col + 1]
            pointer_col += -1
        elif trace == 1:
            alignment["seq1"] = alignment["seq1"] + seq1[pointer_row + 1]
            alignment["seq2"] = alignment["seq2"] + "-"
            pointer_row += -1
        elif trace == 2:
            alignment["seq1"] = alignment["seq1"] + seq1[pointer_row + 1]
            alignment["seq2"] = alignment["seq2"] + seq2[pointer_col + 1]
            pointer_col += -1
            pointer_row += -1

    alignment["seq1"] = alignment["seq1"][::-1]
    alignment["seq2"] = alignment["seq2"][::-1]

    # TODO add terminal gaps to the sequences
    for i in range(end_pointer_col + 1, len(seq2) - 1):
        alignment["seq2"] += seq2[i]
        alignment["seq1"] += "-"
    for i in range(end_pointer_row + 1, len(seq1) - 1):
        alignment["seq2"] += "-"
        alignment["seq1"] += seq1[i]
    for i in range(pointer_col - 1, -1, -1):
        alignment[seq2] += seq2[i]
        alignment[seq1] += "-"
    for i in range(pointer_row - 1, -1, -1):
        alignment[seq2] += "-"
        alignment[seq1] += seq1[i]

    # print matrices
    prettyMatrix(M)
    prettyMatrix(B)

    # print results
    print("Total Score:", total_score)
    print(alignment["seq1"])
    print(alignment["seq2"])
