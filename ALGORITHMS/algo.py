# Given an array of numbers create a function that returns the maximum value in that array.
# Given [2,3,1,5,4] return 5. Hint:What is the initial max value?​

def find_maximum(arr):
    max_value = arr[0]
    
    for num in arr[1:]:
        if num > max_value:
            max_value = num
    
    return max_value

array = [2, 3, 1, 5, 4]
print("The maximum value is:", find_maximum(array))

print("-------------------------------------------------------------")

# Given an array of numbers create a function that returns the minimum value in that array.
# Given [2,3,1,5,4] return 1. Hint:What is the initial min value?​

def find_minimum(arr):
    min_value = arr[0]
    
    for num in arr[1:]:
        if num < min_value:
            min_value = num
    
    return min_value

array = [2, 3, 1, 5, 4]
print("The minimum value is:", find_minimum(array))