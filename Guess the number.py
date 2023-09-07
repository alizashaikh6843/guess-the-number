import random

def guess_the_number():
    print("Welcome to Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Set the difficulty level
    while True:
        try:
            difficulty = int(input("Choose the difficulty level (1 for Easy, 2 for Medium, 3 for Hard): "))
            if 1 <= difficulty <= 3:
                break
            else:
                print("Please enter a valid difficulty level (1, 2, or 3).")
        except ValueError:
            print("Please enter a valid difficulty level (1, 2, or 3).")

    max_attempts = 0
    if difficulty == 1:
        max_attempts = 15
    elif difficulty == 2:
        max_attempts = 10
    else:
        max_attempts = 5

    secret_number = random.randint(1, 100)
    
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

    if guess != secret_number:
        print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
