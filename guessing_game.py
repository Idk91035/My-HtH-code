#Beckham Jordan Johnny
import random

# Generate a random number between 1 and 100
def generate_random_number():
    return random.randint(1, 100)

# Tells the user if there guess is a valid one 
def get_user_guess():
    while True:
        try:
            guess = int(input("Enter a number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Please enter a valid integer.")

# Play a single round of the guessing game
def play_guessing_game():
    secret_number = generate_random_number()

    #keeps track of wrongful attempts
    attempts = 0

    #checks if the number guessed is low, high or right
    while True:
        guess = get_user_guess()
        attempts += 1

        if guess == secret_number:
            print(f"You guessed the right number {secret_number} in {attempts} attempts!")
            break
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")

# option to restart game
def game_loop():
    while True:
        play_guessing_game()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    game_loop()