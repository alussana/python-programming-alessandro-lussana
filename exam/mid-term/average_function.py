# average_function.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a function that calculates the average of the values of
# any vector of 10 numbers 
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average 
# Define separate functions for the input and for calculating the average

'''
pseudo-code:
    
    function A:
    1) ask the user to write the numbers separated by " ")
    2) split the string provided by the user on " " and store it in a list

    function B:
    1) take in input the returning object of function A, i.e a list
    2) store in a variable l the length of the list
    3) store in a variable S the sum of the elements of the list, converted as
       floats (this may be done using sum(), or inizializing sum = 0 and then
       increasing sum for each element of the vector by the corresponding
       value)
    4) return that value

    function C:
    1) take in input the returning objects of function A (a) and function B (b)
    2) for each element of a, convert it in a float and print it
    3) print b

'''
