import random
from art import logo


print(logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

# generate a random number to guess
GENERATED_NUMBER = random.randint(1, 100)
EASY_LEVEL_ATTEMPTS = 10
DIFFICULT_LEVEL_ATTEMPTS = 5

def choose_difficulty():
    """Gets user input and returns difficulty level"""
    _difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
    # prompt a user for input till the input is correct
    while _difficulty_level != 'easy' and _difficulty_level != 'hard':
        _difficulty_level = input("Please type 'easy' or 'hard': ").lower().strip()

    return _difficulty_level


def decide_num_attempts():
    """Gets difficulty level and returns number of attempts"""
    chosen_difficulty = choose_difficulty()
    if chosen_difficulty == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return DIFFICULT_LEVEL_ATTEMPTS


def ask_for_guess():
    """Prompts user for a guess"""
    _user_guess = input("Make a guess: ").strip()
    # prompt user for input till the input includes only numbers
    while not _user_guess.isdigit():
        print("The input should be a number. Please try again.")
    _user_guess = int(_user_guess)
    print()

    return _user_guess


def compare_numbers(user_input, generated_number):
    """Compares user input to the generated number and prints hints"""
    if user_input > 100 or user_input < 1:
        print("The number should be between 1 and 100. ")
    elif user_input > generated_number:
        print("Too high!")
    else:
        print("Too low")


def play_game():
    # initialize number of attempts
    num_attempts = decide_num_attempts()
    print()
    print(f"You have {num_attempts} attempts to guess the number.")
    # ask for the initial guess
    user_guess = ask_for_guess()


    # run the loop till number is guessed or no attempts left
    while user_guess != GENERATED_NUMBER and num_attempts != 0:
        # compare user input to generated number
        compare_numbers(user_guess, GENERATED_NUMBER)

        # decrease number of attempts if the guess was wrong
        num_attempts -= 1

        # check if user have any guesses left, otherwise break out of the function
        if num_attempts == 0:
            print(f"You're out of guesses. The guessed number was {GENERATED_NUMBER}.")
            return

        print("Guess again!")
        print()
        print(f"You have {num_attempts} {'attempt' if num_attempts == 1 else 'attempts'} left to guess the number.")

        # prompt a use for the next guess
        user_guess = ask_for_guess()

        # check if this is the correct number
        if user_guess == GENERATED_NUMBER:
            print(f"You guessed the right number - {GENERATED_NUMBER}!")
            return


play_game()
print("Restart the page if you'd like to play again.")