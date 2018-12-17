## Create a dummy DataFrame

import pandas as pd

genes = ["gene1","gene2","gene3","gene4"]
t1 = [1.0,2.0,1.3,0.5]
t2 = [2.0,2.1,1.0,0.8]
t3 = [2.5,1.9,0.8,1.4]
t4 = [2.7,1.9,0.7,1.9]

genexpr = pd.DataFrame(data = [t1,t2,t3,t4], index = ["expr1","expr2","expr3","expr4"],columns=genes)
genexpr = genexpr.T     ## transpose

'''
>>> genexpr
       expr1  expr2  expr3  expr4
gene1    1.0    2.0    2.5    2.7
gene2    2.0    2.1    1.9    1.9
gene3    1.3    1.0    0.8    0.7
gene4    0.5    0.8    1.4    1.9
'''

genexpr.columns     ## returns column names in an indexable object
genexpr.index       ## returns row names in an indexable object
genexpr.values      ## returns values in an indexable object

## Accessing DataFrame by column

expr1_column = genexpr.expr1 = genexpr["expr1"]    ## returns a Series

'''
>>> expr1_column
gene1    1.0
gene2    2.0
gene3    1.3
gene4    0.5
Name: expr1, dtype: float64
'''

## Accessing DataFrame by row

gene1_gene3 = genexpr[0:3:2]

'''
>>> gene1_gene3
       expr1  expr2  expr3  expr4
gene1    1.0    2.0    2.5    2.7
gene3    1.3    1.0    0.8    0.7
'''

## Useful functions for DataFrame

genexpr.describe()                              ## returns summary statistics for columns
genexpr.sort_index(axis=1, ascending=False)     ## axis=1: columns; axis=0: rows
genexpr.sort_values(by="expr2")                 ## sorts rows according to the value in col expr2

'''
>>> genexpr.sort_values(by="expr2")
       expr1  expr2  expr3  expr4
gene4    0.5    0.8    1.4    1.9
gene3    1.3    1.0    0.8    0.7
gene1    1.0    2.0    2.5    2.7
gene2    2.0    2.1    1.9    1.9
'''

## Reading data from a file

data = pd.read_table("GEUVADIS.expr.cutted.txt", header=0, index_col=0, sep="\t")

## This is a resized version of a real dataset (GEUVADIS, gene expression datai
## from EBV-lymphoblastoid cell lines) downloaded from 
## https://www.ebi.ac.uk/arrayexpress/files/E-GEUV-1/analysis_results/

## header: the number of the row in which col names are specified
## index_col: the number of the col(s) in which the indexes are specified (multi index is allowed)
## sep: field separator

'''
>>> data.head()
                                           Gene_Symbol  chr    Coord    HG00096    HG00097    ...         NA12348     NA12383    NA12399    NA12400    NA12413
TargetID                                                                                      ...
ENSG00000162408.10_6589054_6589231  ENSG00000162408.10    1  6614595  83.834815  64.014944    ...       58.649581   83.289535  68.193130  51.359173  43.097973
ENSG00000162408.10_6592028_6592139  ENSG00000162408.10    1  6614595  44.003241  39.387407    ...       34.152022   54.555446  26.265230  26.292065  28.394414
ENSG00000162408.10_6592523_6592820  ENSG00000162408.10    1  6614595  88.731652  62.839503    ...      107.977876  102.031253  43.642011  57.618344  63.549020
ENSG00000162408.10_6593340_6593501  ENSG00000162408.10    1  6614595  36.878233  25.444402    ...       40.068368   34.101011  31.072238  31.592056  21.811180
ENSG00000162408.10_6601890_6601987  ENSG00000162408.10    1  6614595  26.020655  24.026659    ...       18.361093   24.241592  16.272479  15.258299  16.190878
'''

## ============================
## Useful methods and functions

data.describe()             ## returns summary statistics for columns

## ====================
## Deleting a column

data = data.drop("Gene_Symbol", 1)  ## 1 for columns names; 0 for indexes (specify the axis)

## =======
## Merging

new_sample = pd.read_table("NA20828.txt", sep="\t", header=0, index_col=0)  

'''
>>> new_sample.head()
                                           NA20828
TargetID
ENSG00000162714.7_247460714_247464578  1257.080064
ENSG00000162714.7_247471777_247471890    40.075274
ENSG00000162714.7_247473001_247473108    53.058649
ENSG00000162714.7_247473626_247473758    65.187342
ENSG00000162714.7_247486000_247486107     2.676004
'''

## It is not needed to do the following prior to merge: 
data = data.sort_index()
new_sample = new_sample.sort_index()
## because pd.merge will auto align the data according to a col value (see on = "TargetID")

merged_data = pd.merge(data, new_sample, on = "TargetID")

## ======================
## Writing data to a file

merged_data = merged_data.drop(["Coord", "chr"], 1)
merged_data.to_csv("merged_data.csv")

## ================
## Boolean Indexing

## this filters records that refer to chr2 and with genomic coordinate > 100000000
selected_data = data[data.chr == 2][data.Coord > 100000000] 

## =========================
## Example of dummy analysis

## computing standard deviation of expr in the population for each gene
selected_data = selected_data.drop(["chr","Coord"],1)
selected_data = selected_data.T
expr_std = selected_data.std()

'''
>>> expr_std.head()
TargetID
ENSG00000162804.9_241976637_241976770    1.631483
ENSG00000162804.9_241979492_241979605    1.524546
ENSG00000162804.9_241979717_241979830    1.732765
ENSG00000162804.9_241987732_241987857    1.896867
ENSG00000162804.9_241988079_241988183    1.367311
dtype: float64
'''

## Computing the difference between quantiles
expr_quant_10 = selected_data.quantile(q=0.1, axis=1)
expr_quant_90 = selected_data.quantile(q=0.9, axis=1)
expr_quant_range = expr_quant_90 - expr_quant_10

'''
>>> expr_quant_range.head()
HG00096    195.997076
HG00097    190.084365
HG00099    145.578205
HG00100    189.320729
HG00101    173.758388
dtype: float64
'''

## ====================
## Plotting the results

## having scipy installed is also needed for this
import matplotlib.pyplot as plt             ## plt is needed since pd.plot is a wrapper of plt functions
std_plot = expr_std.plot.density()          ## create the object needed to plot the density
hist_plot = expr_quant_range.plot.hist()    ## create the object needed to plot the histogram
plt.show()                                  ## show the graph
