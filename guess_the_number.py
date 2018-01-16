import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range(low=1, high=10):
    '''Set the high and low values for the random number'''
    return ask_range()


def ask_range():
    """Asks the user for a range of numbers"""
    low = ask_low()
    high = ask_high(low)
    return low, high


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess(low=1, high=10):
    '''get user's guess'''
    return validate_guess(low, high)


def ask_low():
    low = -1
    while low < 0:
        numb = input("Please enter an integer grater than 0 for the lower number: ")
        if is_number(numb) and int(numb) > 0:
            low = int(numb)
    return low


def ask_high(low):
    high = -1
    while high < low:
        numb = input("Please enter an integer grater than {} for the higher number: ".format(low + 10))
        if is_number(numb) and int(numb) > low + 10:
            high = int(numb)
    return high


def is_number(numb):
    try:
        int(numb)
        return True
    except ValueError:
        return False


def validate_guess(low=1, high=10):
    """validates the guess """
    guess = -1
    while guess < 0:  # chick if guess is valid
        str_guess = input('Guess the secret number? (between {} and {})'.format(low, high))
        if is_number(str_guess):
            guess = int(str_guess)
            if not low <= guess <= high:
                guess = -1
        else:
            guess = -1
    return int(guess)


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    while True:
        # sets number of guesses to 0
        guesses = 0
        (low, high) = configure_range()
        secret = generate_secret(low, high)

        while True:
            # increments by 1
            guesses += 1
            guess = get_guess(low, high)
            result = check_guess(guess, secret)
            print(result)

            if result == correct:
                # prints number of guesses
                print("The number of guess: " + str(guesses))
                break

        play = input("Would you like to play again? Y/N ")
        if play == "Y" or play == "y":
            continue
        else:
            break


if __name__ == '__main__':
    main()
