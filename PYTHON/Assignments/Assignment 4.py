import random

def guessing_game():
    number_to_guess = random.randint(1, 10)
    guessed = False

    print("Welcome to the guessing game! Try to guess the number between 1 and 10.")

    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))

            if user_guess > number_to_guess:
                print("The number is too big, guess again.")
            elif user_guess < number_to_guess:
                print("The number is too small, guess again.")
            else:
                print("Congratulations! You guessed the correct number!")
                guessed = True
        except ValueError:
            print("Please enter a valid number between 1 and 10.")

guessing_game()
