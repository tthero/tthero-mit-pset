# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    # For all characters in the word, if at least one is not found in the guessed, return false
    for c in secretWord:
        if c not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    # Initialises the result with "_ " of length of word
    result = ["_ " for _ in range(len(secretWord))]

    # For each character guessed, if correct, replace "_ " with that character
    # There may exist more than one slot for one character
    # temp to store found position, then temp + 1 to get next position
    for c in lettersGuessed:
        if c in secretWord:
            temp = secretWord.find(c)
            while temp >= 0:
                result[temp] = c
                temp = secretWord.find(c, temp + 1)

    # Returns string
    return ''.join(result)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    from string import ascii_lowercase
    result = [c for c in ascii_lowercase]

    for c in lettersGuessed:
        result.remove(c)

    return ''.join(result)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # INTRODUCTION =)
    print("Welcome to the game, Hangman!")

    # Length of word is?
    print("I am thinking of a word that is", len(secretWord), "letters long.")

    # Start the game
    guessMade = []

    # Initialising the guesses to be 8
    guessLeft = 8
    while True:
        print("-----------")

        # Guessed the word? Yes? No? Compare with the guess made
        if isWordGuessed(secretWord, guessMade):
            print("Congratulations, you won!")
            break
        else:
            if guessLeft > 0:
                print("You have {} guesses left.".format(guessLeft))
                print("Available Letters:", getAvailableLetters(guessMade))

                # Change to lowercase character 1st
                c = input("Please guess a letter: ").lower()

                # Main interpreter
                # Check if c is initially in available letters, if not, c is repeated
                if c not in getAvailableLetters(guessMade):
                    print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, guessMade))
                else:
                    # Add into guess entry, then check guess result, if c in result, then correct, else wrong
                    guessMade.append(c)
                    guessResult = getGuessedWord(secretWord, guessMade)

                    if c in guessResult:
                        print("Good guess:", guessResult)
                    else:
                        print("Oops! That letter is not in my word:", guessResult)
                        guessLeft -= 1
            else:
                print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))
                break



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
