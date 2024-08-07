# Question 2: Generate Random Number
# Create a function generate_random_numbers(start, end) that generates a random number between start and end (inclusive) and returns it. 
# Use the random.randint() function from the random module to generate the random number.

import random

def generate_random_numbers(start, end):
    return random.randint(start, end)

random_number = generate_random_numbers(1, 20)
print(f"Here is your random number generated between 1 and 20: {random_number}")