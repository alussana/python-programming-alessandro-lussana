# TODO heapExtractMax() in prog
def heapExtractMax(A, heapsize):
    if heapsize < 0:
        print("heap underflow")
        exit
    maximum = A[0]
    A[0] = A[heapsize - 1]
    A = heapExtractMax(A, heapsize)
    return(maximum, A)

# TODO heapIncreaseKey() in prog
def heapIncreaseKey(A, i, key):
    if key < A[i]:
        print("New key is smaller than current key")
        exit
    A[i] = key
    while i > 0 and A[i // 2] < A[i]:
        current_value = A[i]
        A[i] = A[i // 2]
        A[i // 2] = current_value
        i = i // 2

def maxHeapify(A, i, heapsize):
    '''
    Solve a violation of the heap property 
    '''
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l <= heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if r <= heapsize and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        
        maxHeapify(A, largest, heapsize)

def buildMaxHeap(A):
    '''
    Build a heap from an unsorted array 
    '''
    heapsize = len(A) - 1

    for i in range(heapsize // 2, -1, -1):
        maxHeapify(A, i, heapsize)

def maxHeapSort(A):
    '''
    Efficiently sort an array using heap data structure
    '''
    heapsize = len(A) - 1
    
    buildMaxHeap(A)
    
    for i in range(heapsize, -1, -1):
        A[0], A[i] = A[i], A[0]
        maxHeapify(A, i, heapsize)
    
    return(A)

if __name__ == '__main__':
    A = [5,2,4,7,1,3,2,6]
    print("in:", A)
    sorted_A = maxHeapSort(A)
    print("out:", sorted_A)
