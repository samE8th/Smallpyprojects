# In Bagels, a deductive logic game, you
# must guess a secret three-digit number
# based on clues. The game offers one of
# the following hints in response to your guess:
# “Pico” when your guess has a correct digit in the
# wrong place, “Fermi” when your guess has a correct
# digit in the correct place, and “Bagels” if your guess
# has no correct digits. You have 10 tries to guess the
# secret number.

import random

NUM_DIGITS = 3  # Number of digits in the secret number.
MAX_GUESSES = 10  # Maximum number of guesses allowed.

def main():
    print('''Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com

    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:    That means:
    Pico           One digit is correct but in the wrong position.
    Fermi          One digit is correct and in the right position.
    Bagels         No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:  # Main game loop.
        secretNum = getSecretNum()  # Generate the secret number.
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')  # Get the player's guess.

            clues = getClues(guess, secretNum)  # Generate clues based on the guess.
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # Correct guess, exit the loop.
        
        if guess == secretNum:
            print('You got it!')
        else:
            print('You ran out of guesses.')
            print('The answer was {}.'.format(secretNum))

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break  # Exit the main game loop if the player doesn't want to play again.
    print('Thanks for playing!')

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')  # Correct digit in the correct place.
        elif guess[i] in secretNum:
            clues.append('Pico')  # Correct digit in the wrong place.

    if len(clues) == 0:
        return 'Bagels'  # No correct digits.
    else:
        clues.sort()  # Sort clues alphabetically.
        return ' '.join(clues)  # Join clues into a single string.

if __name__ == '__main__':
    main()
