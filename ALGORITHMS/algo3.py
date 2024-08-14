'''Create a function that accepts a string of 1's and 0's and returns a new string 
where all of the 1's are replaced by 2's. 
Example: Given “1001011” return "2002022". Hint: Remember that strings are just an 
array of characters that can’t be altered. So you will have to create a new string 
from scratch and use that as your return string. No built in functions unless they 
are absolutely necessary.'''

def replace_ones_with_twos(binary_string):
    new_string = ""
    
    for character in binary_string:
        if character == "1":
            new_string += "2"
        else:
            new_string += character
    
    return new_string

binary_string = "1001011"
print("The new string is:", replace_ones_with_twos(binary_string))