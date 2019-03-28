import numpy as np

def visualGD(x, alpha, max_error):
    '''
    Dummy implementation of GD to find the local minimum of sinx + abs(x) + 1
    '''
    delta = 0.01
    e = np.inf
    while e > max_error:
        y1 = getY(x)
        y2 = getY(x + delta)
        d = (y2 - y1)
        x = x - alpha * d
        y = getY(x)
        e = abs(y1 - y)
        print("x = %f\ty = %f\te = %f\td = %f" %(x, y, e, d / delta))

def getY(x):
    '''
    Compute the value of sinx + abs(x) + 1, given x
    '''
    return(np.sin(x) + abs(x) + 1)

if __name__ == "__main__":
    print("\n\t=== Grandient Descent Dummy Demo ===\n")
    x = float(input("Insert the starting value for sinx + abs(x) + 1\nx = "))
    lr = float(input("Insert the learning rate parameter\nlr = "))
    print("Insert the maximum tolerated error to define convergence")
    maxE = float(input("maxE = "))
    visualGD(x, lr, maxE)
