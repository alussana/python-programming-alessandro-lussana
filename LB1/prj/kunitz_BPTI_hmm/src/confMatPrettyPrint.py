import sys
import gzip
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def feed_confusion_matrix(filename, th, sp = -2, cp = -1):
    f = gzip.open(filename)
    y_true = []
    y_pred = []
    for line in f:
        
        v = line.rstrip().split()
        y_true.append(int(v[cp]))
        if float(v[sp]) <= th:

            y_pred.append(1)

        else:

            y_pred.append(0)

    f.close()

    return(y_true, y_pred)

def print_confusion_matrix(confusion_matrix, class_names, figsize = (4,3), fontsize=14):
    """Prints a confusion matrix, as returned by sklearn.metrics.confusion_matrix, as a heatmap.
    
    Arguments
    ---------
    confusion_matrix: numpy.ndarray
        The numpy.ndarray object returned from a call to sklearn.metrics.confusion_matrix. 
        Similarly constructed ndarrays can also be used.
    class_names: list
        An ordered list of class names, in the order they index the given confusion matrix.
    figsize: tuple
        A 2-long tuple, the first value determining the horizontal size of the ouputted figure,
        the second determining the vertical size. Defaults to (10,7).
    fontsize: int
        Font size for axes labels. Defaults to 14.
        
    Returns
    -------
    matplotlib.figure.Figure
        The resulting confusion matrix figure
    """
    df_cm = pd.DataFrame(
        confusion_matrix, index=class_names, columns=class_names, 
    )
    fig = plt.figure(figsize=figsize)
    try:
        heatmap = sns.heatmap(df_cm, annot=True, fmt="d")
    except ValueError:
        raise ValueError("Confusion matrix values must be integers.")
    heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=fontsize)
    heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=fontsize)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
    return(fig)

if __name__ == '__main__':
    filename = sys.argv[1]
    th = float(sys.argv[2])
    figname = sys.argv[3]
    class_names = ["non-Kunitz", "Kunitz"]

    y_true, y_pred = feed_confusion_matrix(filename, th)
    # test
    #print(y_true)
    #print(y_pred)

    confMat = confusion_matrix(y_true, y_pred)
    # test
    #print(confMat)

    fig = print_confusion_matrix(confMat, class_names, fontsize=10)

    plt.savefig(figname, type="png", dpi=96)
    plt.show()
