def fibRec(n):
    if n > 0:
        if n == 1:
            return(0)
        if n == 2:
            return(1)
        if n > 2:
            f = fibRec(n - 1) + fibRec(n - 2)
            return(f)

if __name__ == '__main__' :
    f = fibRec(5)
    print(f)