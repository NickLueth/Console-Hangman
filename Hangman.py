#!/bin/python3
# Console Hangman
# Created by: Nicholas Lueth
# Last edited: 3/5/2020

from random import randint
from os import system, name
from time import sleep
import webbrowser
import States




# This function clears the terminal screen
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

# TODO This can wait until we get the user word input sorted out
def game():
    pass

# TODO Load easy words from a text file
def get_easy_words():
    pass

# TODO Load medium words from a text file
def get_medium_words():
    pass

# TODO Load hard words from a text file
def get_hard_words():
    pass

# TODO Load custom words prior to addition
def get_custom_words():
    pass

# TODO Develope this!
def parse_input(words):
    parsed_input = ""
    for i in range(len(words)):
        if words[i].isalpha():
            parsed_input += words[i]
    return parsed_input


# TODO Focus on making this work
def add_words(c_words):
    file = open("custom_words.txt", "a+")
    while True:
        clear()
        new_word = input("New word(s): ").lower()
        if len(new_word) < 1 or len(parse_input(new_word)) < 1:
            print("BAD INPUT!")
            sleep(2)
        elif new_word in c_words:
            print("That word(s) already exists in the file.")
            sleep(2)
        else:
            break
    file.write(new_word + "\n")
    file.close()
    while True:
        choice = input("Would you like to add more words?[y/n]: ").lower()
        if choice == "y":
            add_words()
            break
        elif choice == "n":
            main_menu()
            break
        else:
            print("That value is not a valid option...")
            sleep(1.5)



def open_twitter():
    webbrowser.open("https://twitter.com/Secwit")
    print("Going to Nick Lueth's twitter!")
    print("[IGNORE THE ERROR WHEN THE BROWSER CLOSES]")
    print("Press enter to go back to the main menu...")
    input()
    main_menu()

# Main menu
def main_menu():
    while True:
        clear()
        print("WELCOME TO HANGMAN!\nCreated by: Nick Lueth")
        print("1. Play\n2. Add custom words or sentences\n3. About the author\n4. Quit")
        try:
            choice = int(input("Choice: "))
        except ValueError:
            clear()
            print("INVALID OPTION!\nPlease type a number.")
            input("PRESS ENTER TO CONTINUE...")
        else:
            if choice == 1:
                game()
                break
            elif choice == 2:
                add_words(custom_words)
                break
            elif choice == 3:
                open_twitter()
                break
            elif choice == 4:
                exit(0)
            else:
                print("That value is not a valid option...")
                sleep(1.5)


def init():
    main_menu()

easy_words = "Make a get easy words function that pulls words from a file"
medium_words = "Make a get medium words function that pulls words from a file"
hard_words = "Make a get hard words function that pulls words from a file"
custom_words = "Make a get custom words fucntion that pulls words from a file" 
states = States.stages
init()
