import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'



def configure_range(low=1, high=10):
    '''Set the high and low values for the random number'''
    return low, high


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    return validate_guess()


def validate_guess(low=1, high=10):
    guess = -1
    while guess < 0:  # chick if guess is valid
        str_guess = input('Guess the secret number? ')
        try:
            guess = int(str_guess)
            if not low <= guess <= high:
                guess = -1
        except ValueError:
            guess = -1
            continue
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
    guesses = 0
    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guesses += 1
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            print("The number of guess: " + str(guesses))
            break


if __name__ == '__main__':
    main()
