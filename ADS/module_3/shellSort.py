def shellSort(a): 
	n = len(a) 
	gap = n//2
    # Gapped insertionSort:
	while gap > 0: 
		for i in range(gap,n): 
			temp = a[i] 
			j = i 
			while j >= gap and a[j-gap] >temp: 
				a[j] = a[j-gap] 
				j -= gap  
			a[j] = temp 
		gap //= 2

if __name__ == '__main__':
    a = [12, 34, 54, 2, 3]  
    print(a)
    shellSort(a) 
    print(a)