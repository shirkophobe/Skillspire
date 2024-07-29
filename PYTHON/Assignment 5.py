import random

def rock_paper_scissors():
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 1 for Rock, 2 for Paper, or 3 for Scissors.")
    
    try:
        user_choice = int(input("Your choice: "))
        if user_choice not in choices:
            print("Invalid choice. Please enter 1, 2, or 3.")
            return
        
        computer_choice = random.randint(1, 3)
        
        print(f"You chose: {choices[user_choice]}")
        print(f"Computer chose: {choices[computer_choice]}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print("You win!")
        else:
            print("You lose!")
    
    except ValueError:
        print("Invalid number! Please enter a number between 1 and 3.")

rock_paper_scissors()
