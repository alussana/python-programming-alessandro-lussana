def countingSort(A):
    k = max(A)
    return(cs(A,k))

def cs(A, k):
    B = [0] * len(A)
    C = [0] * (k + 1) # k is the max in A
    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1 # C contains the # of elements equal to i

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1] # C contains the # of elements <= i

    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1
    
    return(B)

if __name__ == "__main__":
    A = [5,2,4,7,1,3,2,6]
    print ("in:", A)
    sorted_A = countingSort(A)
    print("out:", sorted_A)