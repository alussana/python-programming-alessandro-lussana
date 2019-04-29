import sys
import gzip
import numpy as np

#   Confusion matrix:
#   __________________________________________
#                  | 0:non-kunits  |  1:kunitz
#   __________________________________________
#   0:non-kunitz   |      TN       |    FP
#                  |               | 
#   1:kunitz       |      FN       |    TP
#   __________________________________________

def conf_mat(filename, th, sp = -2, cp = -1):
    cm = [[0.0, 0.0],[0.0, 0.0]]
    f = gzip.open(filename)
    
    for line in f:
        v = line.rstrip().split()
        if int(v[cp]) == 1:
            i = 1
        
        if int(v[cp]) == 0:
            i = 0
        
        if float(v[sp]) <= th:
            j = 1
        
        if float(v[sp]) > th:
            j = 0

        cm[i][j] += 1

    f.close()

    return(cm)

# TODO implement calculation of area under the curve
# TODO scikit-learn python library, matrices method
def print_performance(cm):
    TP = cm[1][1]
    TN = cm[0][0]
    FP = cm[0][1]
    FN = cm[1][0]
    # compute accuracy
    acc = (TP + TN) / (TP + TN + FP + FN)
    # compute sensitivity
    tpr = TP / (TP + FN)
    # compute precision
    ppv = TP / (TP + FP)
    # compute matthews correlation coefficient
    mcc = ( TP * TN - FP * FN  )  / np.sqrt( (TP + FP) * (TP + FN) * (TN + FP) * (TN + FN) )
    print("TP\t%i\nTN\t%i\nFP\t%i\nFN\t%i" %(TP, TN, FP, FN))
    print("acc\t%f\ntpr\t%f\nppv\t%f\nmcc\t%f" %(acc, tpr, ppv, mcc))

if __name__ == '__main__':
    filename = sys.argv[1]
    th = float(sys.argv[2])

    conf_mat = conf_mat(filename, th)

    print_performance(conf_mat)
