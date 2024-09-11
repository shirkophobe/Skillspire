#Part 1
def calculate_result(x, y):
    result = 3 * x + 5 * y
    return result

# Ask the user for input values for x and y
try:
    x = int(input("Enter the value for x: "))
    y = int(input("Enter the value for y: "))

    # Calculate the resulting value
    result = calculate_result(x, y)

    # Output the result
    print(f"The calculated result is {result}.")
except ValueError:
    print("Invalid input. Please enter integer values for x and y.")

#Part 2
def calculate_pay(hours_worked, hourly_rate):
    base_hours = 40
    overtime_multiplier = 1.5
    
    if hours_worked <= base_hours:
        regular_pay = hours_worked * hourly_rate
        print(f"Regular pay: {regular_pay}")
    else:
        regular_pay = base_hours * hourly_rate
        overtime_hours = hours_worked - base_hours
        overtime_pay = overtime_hours * hourly_rate * overtime_multiplier
        total_pay = regular_pay + overtime_pay
        print(f"Regular pay: {regular_pay}")
        print(f"Overtime pay: {overtime_pay}")
        print(f"Total pay: {total_pay}")

# Sample input
try:
    hours_worked = float(input("Enter the total hours worked: "))
    hourly_rate = float(input("Enter the hourly pay rate: "))
    calculate_pay(hours_worked, hourly_rate)
except ValueError:
    print("Invalid input. Please enter numerical values for hours worked and hourly rate.")
