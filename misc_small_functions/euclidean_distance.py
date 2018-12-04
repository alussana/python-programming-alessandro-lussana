import math

def euclidean_distance(x1, x2):
    squared_distance = 0
    for i in range(len(x1)):
        squared_distance = squared_distance + (x1[i] - x2[i]) ** 2
    return(math.sqrt(squared_distance))

x1 = [0,1,1]
x2 = [1,2,3]

print(euclidean_distance(x1, x2))
