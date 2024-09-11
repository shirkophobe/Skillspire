#Part 1
# Print the sum of all the numbers from 1-15

sum = 0
for i in range(1, 16):
    sum += i
print(sum)

# Part 2
# Use a for loop to count from 1-100. 
# For every number that is odd print “FIZZ” for every number that is even print “BUZZ”

for i in range(1, 101):
    if i % 2 == 0:
        print("BUZZ")
    else:
        print("FIZZ")

# Part 3
# Create a list variable with 5 numbers and 
# find the minimum, maximum and average of all those numbers. Then print them out.
        
numbers = [12, 25, 37, 42, 50]
min_num = min(numbers)
max_num = max(numbers)
total = sum(numbers)
avg = total / len(numbers) 

print("Minimum:", min_num)
print("Maximum:", max_num)
print("Average:", avg)     