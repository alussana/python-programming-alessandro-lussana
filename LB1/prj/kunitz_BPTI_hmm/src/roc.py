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
    import sys
    import numpy as np
    from sklearn.metrics import roc_curve
    from sklearn.metrics import roc_auc_score
    import gzip
    import matplotlib.pyplot as plt

    file = sys.argv[1]

    group, scores = get_examples(file)

    fpr, tpr, thresholds = compute_roc(group, scores)

    auc = compute_auc(group, scores)

    plt.plot(fpr, tpr)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC')
    plt.show()
