import random

# generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# set the number of guesses to 0
num_guesses = 0

# loop until the player guesses the correct number or runs out of guesses
while num_guesses < 3:
    # get the player's guess
    guess = int(input("Guess a number between 1 and 10: "))

    # increment the number of guesses
    num_guesses += 1

    # check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    else:
        print("Sorry, that's not the right number. Please try again.")

# if the player runs out of guesses, reveal the secret number
if num_guesses == 3:
    print(f"Sorry, you didn't guess the secret number. It was {secret_number}.")
