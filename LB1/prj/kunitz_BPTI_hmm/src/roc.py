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
    auc = roc_auc_score(group, scores)

    return(auc)

if __name__ == '__main__':
    file = str(sys.argv[1])
    S = round(float(sys.argv[2]),2)
    L = round(float(sys.argv[3]),2)
    aln = str(sys.argv[4])
    n = int(sys.argv[5])

    group, scores = get_examples(file)

    fpr, tpr, thresholds = compute_roc(group, scores)

    group = group[::-1]
    auc = compute_auc(group, scores)

    print("auc = ", auc)

    plt.plot(tpr, fpr)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC')
    text = '\n'.join((
        # TODO round does not work as expected
        'S = %f' % round(S),
        'L = %f' % round(L),
        'aln = %s' % (aln),
        'n = %i' % (n)))
    props = dict(boxstyle='round', facecolor='lightblue', alpha=0.5)
    plt.text(0.75, 0.00, text, bbox=props, fontsize=11)
    plt.show()
