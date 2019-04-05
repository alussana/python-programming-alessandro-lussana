import numpy as np

def mergeSort(A):
    p = 0
    r = len(A) - 1
    return(divide(A, p, r))

def divide(A, p, r):
    if p < r:
        q = int((p + r) / 2)

        divide(A, p, q)
        divide(A, q + 1, r)
        
        return(conquer(A, p, q, r))

def conquer(A, p, q, r):
    L = A[p:q + 1]
    L.append(np.inf)
    R = A[q + 1:r + 1]
    R.append(np.inf)
    i = j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    return(A)


if __name__ == '__main__':
    A = [5,2,4,7,1,3,2,6]
    print ("in:", A)
    A = mergeSort(A) 
    print("out:", A)