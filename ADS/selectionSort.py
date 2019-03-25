'''
T(n) = n + T(n - 1)

number of recursions = n 

T(n) = $\sum_{i = 1}^{N}{i}$ = \frac{(n)(n+1)}{2} = \theta(n^2)$
'''

from numpy import inf

def recursiveSelectionSort(A):
    return(selectionSort(A, 0))

def selectionSort(A, i):
    if i < len(A):
        minimum = inf
        for p in range(i, len(A)):
            if A[p] <= minimum:
                minimum = A[p]
                min_pos = p
        A[min_pos] = A[i]
        A[i] = minimum
        i += 1
        selectionSort(A, i)
    return(A)

def iterativeSelectionSort(A):
    pass

if __name__ == '__main__':
    A = [5,2,4,7,1,3,2,6]
    print(A)
    sorted_A = recursiveSelectionSort(A)    
    print(sorted_A)