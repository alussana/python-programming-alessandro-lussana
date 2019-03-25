def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            #A[i], A[j] = A[j], A[i]
            ith_elem = A[i]
            A[i] = A[j]
            A[j] = ith_elem
    
    #A[i + 1], A[r] = A[r], A[i + 1]
    rth_elem = A[r]
    A[r] = A[i + 1]
    A[i + 1] = rth_elem
    
    return(i + 1)
    
def qs(A, i, r):
    if i < r:
        middle_elem_index = partition(A, i, r)

        qs(A, 0, middle_elem_index - 1)

        qs(A, middle_elem_index + 1, r)

        return(A)

def quickSort(A):
    return(qs(A, 0, len(A) - 1))

if __name__ == '__main__':
    A = [5,2,4,7,1,3,2,6]
    print ("in:", A)
    sorted_A = quickSort(A) 
    print("out:", sorted_A)