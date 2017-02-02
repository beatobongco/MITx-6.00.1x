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


"""
  Problem 1
"""

def isWordGuessed(secretWord, lettersGuessed):
  '''
  secretWord: string, the word the user is guessing
  lettersGuessed: list, what letters have been guessed so far
  returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
  '''
  # Break secretWord into its component parts
  sw_unique_letters = set([x for x in secretWord])

  # lettersGuessed has to contain all of them
  for letter in sw_unique_letters:
    if letter not in lettersGuessed:
      return False

  return True

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

assert isWordGuessed(secretWord, lettersGuessed) == False


"""
  Problem 2
"""


def getGuessedWord(secretWord, lettersGuessed):
  '''
  secretWord: string, the word the user is guessing
  lettersGuessed: list, what letters have been guessed so far
  returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
  '''
  # for letter in secretWord:
  #   if letter in lettersGuessed:
  #     out += letter
  #   else:
  #     out += "_ "

  # Use more efficient list comprehension, more or less equivalent to above code
  out = "".join([x if x in lettersGuessed else "_ " for x in secretWord])
  return out

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

assert getGuessedWord(secretWord, lettersGuessed) == "_ pp_ e"


"""
  Problem 3
"""


import string

def getAvailableLetters(lettersGuessed):
  '''
  lettersGuessed: list, what letters have been guessed so far
  returns: string, comprised of letters that represents what letters have not
    yet been guessed.
  '''
  return "".join([x if x not in lettersGuessed else "" for x in string.ascii_lowercase])

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
assert getAvailableLetters(lettersGuessed) == "abcdfghjlmnoqtuvwxyz"


"""
  Problem 4
"""

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
  guesses = 8
  lettersGuessed = []

  print("Welcome to the game, Hangman!")
  print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")

  while not isWordGuessed(secretWord, lettersGuessed):
    print("-------------")
    print("You have " + str(guesses) + " guesses left")
    print("Available letters:" + getAvailableLetters(lettersGuessed))
    guess = str(input("Please guess a letter: ")).lower()

    if len(guess) > 1:
      print("Invalid input. One character at a time!")
      continue

    if guess in lettersGuessed:
      print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
      continue
    else:
      lettersGuessed.append(guess)

    if guess in secretWord:
      print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
    else:
      print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
      guesses -= 1
      if guesses == 0:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
        return

  print("-------------")
  print("Congratulations, you won!")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)