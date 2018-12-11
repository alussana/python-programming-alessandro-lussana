# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3

L = []

for i in range(21, 40):
    L.append(i)

for i in L:
    if i % 2 == 0:
        print(i)

# Exercise 2
# Print the last two elements of L 

print(L[len(L)-1],L[len(L)-2])

# Exercise 3
# What's wrong with the following piece of code? Fix it and 
# modify the code in order to have it work AND to have "<i> is in the list" 
# printed at least once

L = ['1', '2', '3']
for i in range(10):
    if str(i) in L:
        print("i is in the list")
    else:
        print("i not found")    


# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list 

fasta = open("sprot_prot.fasta")
head = fasta.readline()
head_items = head.split("OS=")
print(head_items[1])

# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string

more_items = list(head_items[1])
print(more_items[0] + more_items[1])

# Exercise 6
# reverse the string 'asor rosa'

text = "asor rosa"
txet = text[::-1]

# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]

L.sort()

# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L

M = L
M.sort()

# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6

table = [[2,4],[3,6]]
out_file = open("out_file","w")

for line in table:
    print(" ".join([str(item) for item in line]))
