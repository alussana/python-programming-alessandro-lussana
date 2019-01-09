import matplotlib.pylab as pl
## 1) create ifuge objrect with figure()
## 2) plot data
## 3) save the figure with savefig()

length = [16,100,65,20,48,49,62,33]
neuron = [1,2,3,4,5,6,7,8]

pl.figure()
pl.title("Title")
pl.ylabel("ylab")
pl.xlab("xlab")
pl.yticks(neuron,neuron)
pl.barh(neuron, length)         ## barplot

pl.show()                       ## shows in a new window
pl.savefig("my_graph.png")      ## saves in a file

y1data = [600,700,500,400]
y2data = []

## there is a lot of work done
##  https://matplotlib.org/gallery/index.html
