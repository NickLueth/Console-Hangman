#!/bin/python3
# Console Hangman
# Created by: Nicholas Lueth
# Last edited: 8/4/2020

from random import randint
from os import system, name
from time import sleep
import Game
import webbrowser


def game():
    """
    Initiates the game loop found in the Game.py file.
    """
    Game.main()


def check_letters(words):
    """
    This function creates a string of the selected word or phrase that only has the alphabetical letters.
    :param (str) words: The selected word or phrase for the game
    :return (str) letters: A string containing only the alphabetical letters found in words
    """
    letters = ""
    # Iterates through the string and adds alphabetical letters to the empty string "letters"
    for i in range(len(words)):
        if words[i].isalpha():
            letters += words[i]
    return letters


def add_words(c_words):
    """
    This function adds custom phrases or words through user input and makes sure there are no duplicates.
    :param (list) c_words: A list of strings containing the saved phrases and words already found in CustomWords.txt
    """
    # Open the CustomWords.txt in append mode
    file = open(Game.script_path + "CustomWords.txt", "a+")
    while True:
        Game.clear()
        new_word = input("New word(s): ").lower().strip()
        # Don't add the user's input to CustomWords.txt if the string doesn't exist or doesn't have alphabetical letters
        if len(new_word) < 1 or len(check_letters(new_word)) < 1:
            print("BAD INPUT!")
            sleep(2)
        # Don't add the user's input to CustomWords.txt if it already exists in CustomWords.txt
        elif new_word in c_words:
            print("That word(s) already exists in the file.")
            sleep(2)
        # Otherwise allow the string to be added
        else:
            break
    file.write(new_word + "\n")
    file.close()
    custom_words.append(new_word)
    # Prompt the user if they want to add more custom word(s)
    while True:
        choice = input("Would you like to add more word(s)?[y/n]: ").lower()
        # If (y)es, then repeat the function
        if choice == "y":
            add_words(custom_words)
            break
        # If (n)o, then go back to main menu
        elif choice == "n":
            main_menu()
            break
        # If the user types something else, prompt them again
        else:
            print("That value is not a valid option...")
            sleep(1.5)
            Game.clear()


def open_linkedin():
    """
    This function opens up your web browser and loads my LinkedIn page.
    """
    webbrowser.open("https://www.linkedin.com/in/nicholaslueth/")
    print("Going to Nick Lueth's LinkedIn!")
    print("Press enter to go back to the main menu...")
    input()
    main_menu()


# Main menu
def main_menu():
    """
    This function displays the main menu and processes the user's decisions.
    """
    while True:
        Game.clear()
        print("WELCOME TO HANGMAN!\nCreated by: Nick Lueth")
        print("1. Play\n2. Add custom words or sentences\n3. About the author\n4. Quit")
        # Catch the ValueError that occurs when the user types something that isn't an integer
        try:
            choice = int(input("Choice: "))
        # If the error is thrown, tell the user why the error occurred and prompt them again
        except ValueError:
            Game.clear()
            print("INVALID OPTION!\nPlease type a number.")
            input("PRESS ENTER TO CONTINUE...")
        # Otherwise, process the user's selection
        else:
            # If 1, play the game
            if choice == 1:
                game()
            # If 2, add custom words to CustomWords.txt
            elif choice == 2:
                add_words(custom_words)
                break
            # If 3, open Nick Lueth's LinkedIn page
            elif choice == 3:
                open_linkedin()
                break
            # If 4, quit the game
            elif choice == 4:
                exit(0)
            # Otherwise, prompt the user again
            else:
                print("That value is not a valid option...")
                sleep(1.5)


easy_words = Game.get_easy_words()
medium_words = Game.get_medium_words()
hard_words = Game.get_hard_words()
custom_words = Game.get_custom_words()
main_menu()
