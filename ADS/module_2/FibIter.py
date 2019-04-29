from time import time

def FibIter(n):
    if(n <= 2):
        
        return(1)

    else:

        f = [0,1,1]
        for i in range(2, n):
            
            f[0] = f[1]
            f[1] = f[2]
            f[2] = f[0] + f[1]

        return(f[2])

if __name__ == '__main__':
    
    f = int(input("n = "))
    t1 = time()
    print(FibIter(f))
    t2 = time()
    print("execution time = %f" %(t2 - t1))
