import sys
import numpy as np
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
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
    fpr, tpr, thresholds = roc_curve(group, scores)
    
    return(fpr, tpr, thresholds)

def compute_auc(group, scores):
    group = group[::-1]
    
    auc = roc_auc_score(group, scores)

    return(auc)

def handcrafted_auc(fpr,tpr):
    auc = 0
    x = fpr[0]
    y = tpr[0]
    for i in range(1, len(fpr)):
        
        dx = fpr[i] - x
        h = (tpr[i] + y) / 2
        x = fpr[i]
        y = tpr[i]

        auc += h * dx
        print(h, dx, auc)

    return(auc)

if __name__ == '__main__':
    file = str(sys.argv[1])
    S = round(float(sys.argv[2]),2)
    L = round(float(sys.argv[3]),2)
    aln = str(sys.argv[4])
    n = int(sys.argv[5])

    group, scores = get_examples(file)

    fpr, tpr, thresholds = compute_roc(group, scores)

    print(fpr)
    print(tpr)
    print(thresholds)

    #auc = compute_auc(group, scores)
    auc = handcrafted_auc(fpr,tpr)

    print("auc = ", auc)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(tpr, fpr)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC')
    text = '\n'.join((
        # TODO round does not work as expected
        'S = %f' % round(S,2),
        'L = %f' % round(L,2),
        'aln = %s' % (aln),
        'n = %i' % (n),
        'auc = %f' % (auc)))
    props = dict(boxstyle='round', facecolor='lightblue', alpha=0.5)
    plt.text(1, 0, text, bbox=props, fontsize=11, horizontalalignment='right', verticalalignment='bottom')
    plt.show()
