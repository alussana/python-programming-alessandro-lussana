def getLeftChild(tree, key):
    l = 2 * key + 1
    if l >= len(tree):
        return('NULL')
    else:
        return(l)

def getRightChild(tree, key):
    r = 2 * key + 2
    if r >= len(tree):
        return('NULL')
    else:
        return(r)

# in prog
#def getLeftTree(tree, key):
#    l = getLeftChild(tree, key)
#    if l == 'NULL':
#        return(l:)