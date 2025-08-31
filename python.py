import random

def play_guessing_game():
    """
    A number guessing game where the computer picks a number and the player
    tries to guess it. Hints are provided after each guess.
    """
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # The computer chooses a random number.
    secret_number = random.randint(1, 100)
    
    attempts = 0
    guess = 0
    
    # The game loop continues until the correct number is guessed.
    while guess != secret_number:
        try:
            # Get the player's guess from the command line.
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Provide feedback to the player.
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly.")
                print(f"It took you {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Run the game.
if __name__ == "__main__":
    play_guessing_game()
