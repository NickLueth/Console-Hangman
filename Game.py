#!/bin/python3
# Game mechanisms file
# Created by: Nicholas Lueth
# Last edited: 8/5/2020

import random
import States
import os
from os import system, name
from time import sleep


def turn(word, guessed_letters):
    """
    This function details what happens in each turn of the game
    :param (str) word: The selected word or phrase for the game
    :param (list) guessed_letters: A list of guessed letters
    """
    global tries
    # Show the initial unsolved word(s)
    word_state(word, guessed_letters)
    # Get the player's guess
    while True:
        guess = input("Guess a letter: ")
        # If the input is 1 character long and is a letter then let allow the guess
        if len(guess) > 0 and guess.isalpha():
            break
        # If the input is longer than one, tell the player the guess has too many characters
        elif len(guess) > 1:
            clear()
            print("\"" + guess + "\"", "is more than one character. Please try again.")
            input("[PRESS ENTER TO CONTINUE...]")
            clear()
            print(States.stages[tries])
            word_state(word, guessed_letters)
        # Otherwise, tell the player to input an alphabetical character
        else:
            clear()
            print("\"" + guess + "\"", "is not a letter. Please try again.")
            input("[PRESS ENTER TO CONTINUE...]")
            clear()
            print(States.stages[tries])
            word_state(word, guessed_letters)
    clear()
    # Change the letter to lowercase
    guess = guess[0].lower()
    # If the guess has not been guessed before and is in the word(s), add the guess to the list of guessed letters
    if guess in word and guess not in guessed_letters:
        print(guess.upper(), "is in the word(s)!")
        guessed_letters.append(guess)
    # If the guess has not been guessed before and isn't in the word(s), add 1 to tries and add the guess to the list
    # of guessed letters
    elif guess not in word and guess not in guessed_letters:
        print(guess.upper(), "is NOT in the word(s)!")
        guessed_letters.append(guess)
        tries += 1
    # Otherwise, tell the player that they've already guessed that letter
    else:
        print("You already said that letter!")
    # Print the current stage of the hangman
    print(States.stages[tries])


def word_state(word, guessed_letters):
    """
    This function displays which letters the player has guessed and fills in the corresponding blanks in the word.
    :param (str) word: The selected word or phrase for the game
    :param (list) guessed_letters: A list of guessed letters
    """
    # Increment through the word(s) letter by letter
    for letter in range(len(word)):
        # If the character is a space, print a space
        if word[letter] == " ":
            print(" ", end=" ")
        # If the character isn't an alphabetical letter, print that character
        elif not word[letter].isalpha():
            print(word[letter], end=" ")
        # If the the character is a letter and hasn't been guessed, replace is with an underscore "_"
        elif not word[letter] in guessed_letters:
            print("_", end=" ")
        # If the letter has been guessed, print the letter
        else:
            print(word[letter], end=" ")
    print()
    # Display all of the currently guessed letters
    print("Guessed letters: ", end="")
    for i in range(len(guessed_letters)):
        print(guessed_letters[i], end=" ")
    print("\n" * 2)


def clear():
    """
    This function produces a terminal clear dependent on which operating system you are using.
    """
    # If you are using a Windows system
    if name == "nt":
        _ = system("cls")
    # If you are using a unix-based system
    else:
        _ = system("clear")


def get_easy_words():
    """
    This function grabs all words and phrases found in EasyWords.txt
    :return (list) easy_words: All easy words from EasyWords.txt
    """
    easy_words = []
    # Creates an EasyWords.txt if one does not already exist, then opens the file in append mode
    file = open(script_path + "EasyWords.txt", "a+")
    # Then close the file
    file.close()
    # Increment through the file adding each line to the easy_words list
    with open(script_path + "EasyWords.txt") as word_file:
        for word in word_file:
            easy_words.append(word[:-1])
    return easy_words


def get_medium_words():
    """
    This function grabs all words and phrases found in MediumWords.txt
    :return (list) medium_words: All medium words from MediumWords.txt
    """
    medium_words = []
    # Creates a MediumWords.txt if one does not already exist, then opens the file in append mode
    file = open(script_path + "MediumWords.txt", "a+")
    # Then close the file
    file.close()
    # Increment through the file adding each line to the medium_words list
    with open(script_path + "MediumWords.txt") as word_file:
        for word in word_file:
            medium_words.append(word[:-1])
    return medium_words


def get_hard_words():
    """
    This function grabs all words and phrases found in HardWords.txt
    :return (list) hard_words: All hard words from HardWords.txt
    """
    hard_words = []
    # Creates a HardWords.txt if one does not already exist, then opens the file in append mode
    file = open(script_path + "HardWords.txt", "a+")
    # Then close the file
    file.close()
    # Increment through the file adding each line to the hard_words list
    with open(script_path + "HardWords.txt") as word_file:
        for word in word_file:
            hard_words.append(word[:-1])
    return hard_words 


def get_custom_words():
    """
    This function grabs all words and phrases found in CustomWords.txt
    :return (list) custom_words: All custom words from CustomWords.txt
    """
    custom_words = []
    # Creates a CustomWords.txt if one does not already exist, then opens the file in append mode
    file = open(script_path + "CustomWords.txt", "a+")
    # Then close the file
    file.close()
    # Increment through the file adding each line to the custom_words list
    with open(script_path + "CustomWords.txt") as word_file:
        for word in word_file:
            custom_words.append(word[:-1])
    return custom_words


def get_word(level):
    """
    This function selects a word based on the difficulty.
    :param (int) level: The level selected
    :return (str) word: The word or phrase selected
    """
    word = ""
    # If easy difficulty was selected, assign an easy word(s) to be the word(s) used in the game
    if level == 1:
        words = get_easy_words()
        word = words[random.randint(0, len(words)-1)]
        return word
    # If medium difficulty was selected, assign a medium word(s) to be the word(s) used in the game
    elif level == 2:
        words = get_medium_words()
        word = words[random.randint(0, len(words)-1)]
        return word
    # If hard difficulty was selected, assign a hard word(s) to be the word(s) used in the game
    elif level == 3:
        words = get_hard_words()
        word = words[random.randint(0, len(words)-1)]
        return word
    # If custom difficulty was selected, assign a custom word(s) to be the word(s) used in the game
    elif level == 4:
        # If there are no custom words available, give them an easy phrase.
        if len(get_custom_words()) == 0:
            clear()
            print("Oh no!\nYou have not entered any custom word(s).\nFor now you will be given an easy difficulty phrase.")
            input("[PRESS ENTER TO CONTINUE...]")
            words = get_easy_words()
            word = words[random.randint(0, len(words)-1)]
            return word
        # If there are custom word(s), assign a custom word(s) to be the word(s) used in the game
        else:
            words = get_custom_words()
            word = words[random.randint(0, len(words)-1)]
            return word


def level_select():
    """
    This function specifies which difficulty the game will be played in or if the player wants to return to the main
    menu.
    :return (int) level: What level or option was selected
    """
    while True:
        clear()
        # Print the difficulty menu
        print("Select a difficulty:\n1. Easy\n2. Medium\n3. Hard\n4. Custom\n5. Main menu")
        # Catch the ValueError that occurs when the user types something that isn't an integer
        try:
            level = int(input("Choice: "))
        # If the error is thrown, tell the user why the error occurred and prompt them again
        except ValueError:
            clear()
            print("INVALID OPTION!\nPlease type a number.")
            input("[PRESS ENTER TO CONTINUE...]")
        # Otherwise, process the user's selection
        else:
            if 0 < level < 6:
                return level
            else:
                print("That value is not a valid option...")
                sleep(1.5)


def test_win(word, letters):
    """
    This function tests to see if the game is over or not.
    :param (str) word: The selected word or phrase for the game
    :param (list) letters: A list of guessed letters
    :return (bool) True | False: Whether or not the game is over
    """
    global tries
    # If the player makes 8 wrong guesses, stop the game, and inform the player that they have lost
    if tries == 8:
        print("YOU LOSE!\nThe word(s) was:", word)
        input("[PRESS ENTER TO CONTINUE...]")
        return True
    elif tries < 8:
        word_list = []
        # Make a the alphabetical characters in the word a list
        for i in range(len(word)):
            if word[i].isalpha():
                word_list.append(word[i])
        # Then go through each letter in the word and check to see if all letters have been guessed
        for letter in word_list:
            # If a letter that hasn't been guessed is found, then return False, and continue with the game
            if letter not in letters:
                return False
        # If all letters have been guessed, stop the game, and inform the player that they have won
        print("YOU WIN!\nThe word(s) was:", word)
        input("[PRESS ENTER TO CONTINUE...]")
        return True


def main():
    """
    This function contains the game loop.
    :return: (NoneType)
    """
    global tries
    # Initiate game loop
    while True:
        # At the beginning of a game empty the guessed_letters list
        guessed_letters = []
        # Assign game difficulty
        level = level_select()
        # If the level is 5, return back to the main menu
        if level == 5:
            break
        # Get the word for the game according to the difficulty
        word = get_word(level)
        clear()
        # Preemptively post the empty gallows
        print(States.stages[tries])
        # Start the sub-game loop
        while True:
            # Start a turn
            turn(word, guessed_letters)
            # Test whether the player has won or lost and return to the main menu
            if test_win(word, guessed_letters):
                # If they've won or lost, reset the number of failed attempts
                tries = 0
                # Then return to the main menu
                return


# (str) script_path: is a variable that holds the directory in which the script is running
# Path for windows
if name == "nt":
    script_path = os.path.dirname(os.path.realpath(__file__)) + "\\"
# Path for unix-based systems
else:
    script_path = os.path.dirname(os.path.realpath(__file__)) + "/"
# (int) tries: is a variable that represents the number of failed guesses a player has made during a game
tries = 0
