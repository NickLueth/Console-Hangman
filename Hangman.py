#!/bin/python3
# Console Hangman
# Created by: Nicholas Lueth
# Last edited: 7/20/2020

from random import randint
from os import system, name
from time import sleep
import Game
import webbrowser


def game():
    Game.main()


def check_letters(words):
    letters = ""
    for i in range(len(words)):
        if words[i].isalpha():
            letters += words[i]
    return letters


def add_words(c_words):
    file = open("CustomWords.txt", "a+")
    while True:
        Game.clear()
        new_word = input("New word(s): ").lower().strip()
        if len(new_word) < 1 or len(check_letters(new_word)) < 1:
            print("BAD INPUT!")
            sleep(2)
        elif new_word in c_words:
            print("That word(s) already exists in the file.")
            sleep(2)
        else:
            break
    file.write(new_word + "\n")
    file.close()
    custom_words.append(new_word)
    while True:
        choice = input("Would you like to add more words?[y/n]: ").lower()
        if choice == "y":
            add_words(custom_words)
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
        Game.clear()
        print("WELCOME TO HANGMAN!\nCreated by: Nick Lueth")
        print("1. Play\n2. Add custom words or sentences\n3. About the author\n4. Quit")
        try:
            choice = int(input("Choice: "))
        except ValueError:
            Game.clear()
            print("INVALID OPTION!\nPlease type a number.")
            input("PRESS ENTER TO CONTINUE...")
        else:
            if choice == 1:
                game()
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

easy_words = Game.get_easy_words()
medium_words = Game.get_medium_words()
hard_words = Game.get_hard_words()
custom_words = Game.get_custom_words()
init()
