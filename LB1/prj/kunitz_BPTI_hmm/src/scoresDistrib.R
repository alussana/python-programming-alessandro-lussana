args = commandArgs(trailingOnly=TRUE)

f = args[1] # filename
o = args[2] # outfile
aln = args[3] # aligner
L = args[4] # coverage param for blastclust
S = args[5] # identity param for blastclust
n = args[6] # sample size for random negative test set

pdf(o, height=5, width=5)

t = read.table(f, col.names=c("ID","score","class"))
neg <- t[t$class == 0,]
pos <- t[t$class == 1,]

plot(density(neg$score), col=3)
plot(density(pos$score), col=3)
