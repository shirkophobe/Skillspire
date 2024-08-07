# Question 1: Temperature Conversion Program
# Use the input function to prompt the user for the current temperature in their area in Fahrenheit.  This program should convert and print the temperature given from Fahrenheit to both Celsius using the conversion formula below.

# The formulas for conversion are:

# Celsius: (Fahrenheit - 32) * 5/9

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 1)

fahrenheit = float(input("Enter the current temperature in Fahrenheit: "))

celsius = fahrenheit_to_celsius(fahrenheit)

print(f"The temperature in Celsius is: {celsius} degrees")