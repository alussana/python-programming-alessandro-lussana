def mergeSort(A): 
    if len(A) > 1: 
        q = int(len(A) / 2)
        L = A[:q]  
        R = A[q:]
  
        mergeSort(L) 
        mergeSort(R)
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                A[k] = L[i] 
                i+=1
            else: 
                A[k] = R[j] 
                j+=1
            k+=1

        while i < len(L): 
            A[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            A[k] = R[j] 
            j+=1
            k+=1
  
# hard code some vars for testing
if __name__ == '__main__': 
    A = [5,2,4,7,1,3,2,6]
    print ("in:")  
    print(A) 
    mergeSort(A) 
    print("out") 
    print(A) 