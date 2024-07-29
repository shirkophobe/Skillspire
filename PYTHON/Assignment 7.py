def calculate_total_cost():
    price_per_package = 99.0

    # Prompt user for the number of units sold
    try:
        units_sold = int(input("Enter the number of units sold: "))
        if units_sold < 1:
            print("The number of units sold must be at least 1.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number of units.")
        return

    # Determine discount rate based on the quantity
    if 10 <= units_sold <= 19:
        discount_rate = 0.20
    elif 20 <= units_sold <= 49:
        discount_rate = 0.30
    elif 50 <= units_sold <= 99:
        discount_rate = 0.40
    elif units_sold >= 100:
        discount_rate = 0.50
    else:
        discount_rate = 0.0

    # Calculate total cost
    discount_amount = units_sold * price_per_package * discount_rate
    total_cost = (units_sold * price_per_package) - discount_amount

    # Round to two decimal places
    total_cost = round(total_cost, 2)

    # Print the result
    print(f"The total cost for {units_sold} units is ${total_cost}.")

calculate_total_cost()
