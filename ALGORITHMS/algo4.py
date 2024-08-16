'''Count Non-Spaces. Create a function that  accepts a string and returns the number 
of non-space characters found in the string. For example, given ”lol cool dude", 
return 11 (not 13). Remember NO BUILT IN FUNCTIONS.'''

def count_non_space_chars(input_string):
    count = 0
    
    for char in input_string:
        if char != ' ':
            count += 1
    
    return count


test_string = "lol cool dude"
print("The number of non-space characters is:", count_non_space_chars(test_string))