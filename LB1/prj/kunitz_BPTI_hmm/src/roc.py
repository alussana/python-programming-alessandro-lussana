import sys
import numpy as np
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import auc
import gzip
import matplotlib.pyplot as plt

def get_examples(file):
    group = []
    scores = []
    with gzip.open(file) as f:
        for line in f:
            line = line.strip().split()
            scores.append(float(line[1]))
            group.append(int(line[2]))
    
    return(np.array(group), np.array(scores))

def compute_roc(group, scores):
    fpr, tpr, thresholds = roc_curve(group, scores, pos_label = 0)
    
    return(fpr, tpr, thresholds)

def compute_roc_auc(group, scores):
    invertedLabels = []
    for lab in group:
        
        if lab == 0:
            invertedLabels.append(1)
        
        elif lab == 1:
            invertedLabels.append(0)

    area = roc_auc_score(invertedLabels, scores)

    return(area)

def show_roc_plot(tpr, fpr, auc, s, l, n, aln, bestTh):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(tpr, fpr)
    x = np.linspace(0,1,100)
    plt.plot(x,x,'gray')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC')
    plt.grid()
    #text = '\n'.join((
    #    # todo round does not work as expected
    #    's = %f' % round(s,2),
    #    'l = %f' % round(l,2),
    #    'aln = %s' % (aln),
    #    'n = %i' % (n),
    #    'auc = %f' % (area)))
    text = ('AUC = %f' % (area))
    props = dict(boxstyle='round', facecolor='lightblue', alpha=0.5)
    #plt.text(1, 0, text, bbox=props, fontsize=11, horizontalalignment='right', verticalalignment='bottom')
    plt.text(0.5, 0.5, text, bbox=props, horizontalalignment='center', verticalalignment='center', fontsize=15, color='red')
    plt.show()

def computeBestThresholds(fpr, tpr, thresholds):
    delta = tpr - fpr
    max_i = 0
    max_delta = 0
    indexes = []
    for i in range(0, len(tpr)):
        if tpr[i] - fpr[i] >= max_delta:
            max_delta = tpr[i] - fpr[i]
            max_i = i

    print(max_delta)
    th = []
    for i in range(0, len(delta)):
        if delta[i] == max_delta:
            th.append(thresholds[i])
    
    return(th[0], th[len(th) - 1])

def printRocResults(fpr, tpr, thresholds, bestTh):
    print("fpr\ttpr\tthreshold\toptimum")
    for i in range(0, len(fpr)):
        if thresholds[i] == bestTh[0]:
            print("%f\t%f\t%f\t1" %(fpr[i], tpr[i], thresholds[i]))
        else:
            print("%f\t%f\t%f\t0" %(fpr[i], tpr[i], thresholds[i]))

if __name__ == '__main__':
    file = str(sys.argv[1])
    S = round(float(sys.argv[2]),2)
    L = round(float(sys.argv[3]),2)
    aln = str(sys.argv[4])
    n = int(sys.argv[5])

    group, scores = get_examples(file)

    fpr, tpr, thresholds = compute_roc(group, scores)

    area = compute_roc_auc(group, scores)

    bestTh = computeBestThresholds(fpr, tpr, thresholds)

    printRocResults(fpr, tpr, thresholds, bestTh)

    show_roc_plot(tpr, fpr, auc, S, L, n, aln, bestTh)
