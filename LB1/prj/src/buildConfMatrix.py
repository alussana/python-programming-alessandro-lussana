import sys
import numpy as np

#   Confusion matrix:
#   _________________________________________
#                  | 0:non-kunits  |  1:kunitz
#   __________________________________________
#   0:non-kunitz   |               |
#   1:kunitz       |               |
#   _________________________________________

def conf_mat(filename, th, sp = -2, cp = -1):
    cm = [[0.0, 0.0],[0.0, 0.0]]
    f = open(filename)
    for line in f:
        v = line.rstrip().split() # split the line on blank space
        if int(v[cp]) == 1:
            i = 1
        if int(v[cp]) == 0:
            i = 0
        if float(v[sp]) <= th:
            j = 1
        if float(v[sp]) > th:
            j = 0

    cm[i][j] += 1

    return(cm)

# TODO implement the ROC scores (see wikipedia)
# TODO implement calculation of area under the curve!!
# TODO scikit learn python library, matrices method
def print_performance(cm):
    # compute accuracy
    acc = (cm[0][0] + cm[1][1])
    # compute denominator of the matthew correlation coefficient
    d = np.sqrt( (cm[0][0] + cm[0][1]) * () )
    # compute matthew coefficient
    mc = (cm[0][0] * cm[1][1])

# TODO print matrix and assessment values
if __name__ == '__name__':
    filename = sys.argv[1]
    th = float(sys.argv[2])
