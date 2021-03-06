'''
BS(A, target, i, r):
    
    m = (i + r) // 2
    
    if A[m] == target then
        
        return(m)
    
    else if target < A[m] and i < r then
        
        i = BS(A, target, i, m - 1)
    
    else if target > A[m] and i < r then
        
        i = BS(A, target, m + 1, r)
    
    else
        
        i <- "NIL"
    
    return(i)
'''

def iterativeBinarySearch(A, target):
    i = 0
    r = len(A)
    while i < r - 1:
        m = (i + r) // 2
        if A[m] == target:
            return(m)
        elif target < A[m]:
            r = m
        elif target > A[m]:
            i = m
    return("NIL")

def recursiveBinarySearch(A, target):
    m = bs(A, target, 0, len(A) - 1)
    return(m)

def bs(A, target, i, r):
    m = (i + r) // 2
    print(A, i, r)
    if A[m] == target:
        return(m)
    elif target < A[m] and i < r:
        i = bs(A, target, i, m - 1)
    elif target > A[m] and i < r:
        i = bs(A, target, m + 1, r)
    else:
        i = "NIL"
    return(i)

if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9]
    print(A)
    target = int(input("Insert the target: "))
    m = recursiveBinarySearch(A, target)
    #m = iterativeBinarySearch(A, target)
    print("The index of %i in A is %s" %(target, str(m)))