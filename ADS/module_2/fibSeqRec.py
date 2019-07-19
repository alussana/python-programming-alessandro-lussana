def fibSeqRec(A, n):
    if n >= 0:
        if n == 0:
            A[n] = 0
            return(0)
        if n == 1:
            A[n] = 1
            return(1)
        if n > 1:
            f = fibSeqRec(A, n - 1) + fibSeqRec(A, n - 2)
            A[n] = f
            return(f)

if __name__ == '__main__' :
    n = 5
    A = [0] * n
    f = fibSeqRec(A, n - 1)
    print(A)