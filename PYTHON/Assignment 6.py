import random

def roll_the_dice():
    print("Welcome to the Roll The Dice game!")
    try:
        user_choice = int(input("Enter a number between 1 and 6: "))
        if user_choice < 1 or user_choice > 6:
            print("Invalid choice. Please enter a number between 1 and 6.")
            return
        
        roll_count = 0
        rolled_number = 0
        
        while rolled_number != user_choice:
            rolled_number = random.randint(1, 6)
            roll_count += 1
            print(f"Rolled: {rolled_number}")
        
        print(f"You have successfully rolled {user_choice}!")
        print(f"It took you {roll_count} tries to roll the number {user_choice}.")
    
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")

roll_the_dice()
