library(pROC)

args = commandArgs(trailingOnly=TRUE)

f = args[1] # filename
o = args[2] # outfile
aln = args[3] # aligner
L = args[4] # coverage param for blastclust
S = args[5] # identity param for blastclust
n = args[6] # sample size for random negative test set

pdf(o)

t = read.table(f, col.names=c("ID","score","class"))

roc_obj <- roc(t$class, t$score)
auc <- auc(roc_obj)

# TODO fix x axis: by default plot.roc does not plot the FPR and the axis orientation is from 1 to 0
plot.roc(t$class, t$score, main="Receiver Operating Characteristic Curve", xlab="False Positive Rate", ylab="True Positive Rate")
legend('bottomright',legend=c(paste("Aln:",aln), paste("L:",L),paste("S:",S),paste("n:",n),paste("auc =",auc)))

dev.off()
