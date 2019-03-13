def insertionSort(numbers):
    for j in range(1,len(numbers)):
        key = numbers[j]
        i = j - 1
        while i > -1 and numbers[i] > key:
            numbers[i + 1] = numbers[i]
            i = i - 1
        numbers[i + 1] = key
    return(numbers)

if __name__ == '__main__':
    ## some variables are hard coded for testing
    numbers = [5,2,4,7,1,3,2,6]
    print(numbers)
    sorted_numbers = insertionSort(numbers)
    print(sorted_numbers)