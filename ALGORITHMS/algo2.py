# Create a function that accepts a string of 1’s and 0’s 
# and returns a count of all of the 1’s in that string. 
# Example: Given “1001011” return 4. Do NOT use built-in functions.

def count_ones(binary_string):
    count = 0
    
    for char in binary_string:
        if char == '1':
            count += 1
    
    return count

binary_string = "1001011"
print("The number of '1's is:", count_ones(binary_string))


print("---------------------------------------------------")

# Given an array of numbers create a function that returns a count of all of the numbers 
# that are greater than the number 1. 
# Example: Given [2,3,1,5,4] return 4. Do NOT use built-in functions.

def count_greater_than_one(arr):
    count = 0
    
    for num in arr:
        if num > 1:
            count += 1
    
    return count

array = [2, 3, 1, 5, 4]
print("The count of numbers greater than 1 is:", count_greater_than_one(array))
