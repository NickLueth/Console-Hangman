#!/bin/python3
# Console Hangman
# Created by: Nicholas Lueth
# Last edited: 3/5/2020

from random import randint
from os import system, name
from time import sleep
import webbrowser
import States
import Game


# This function clears the terminal screen
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def game():
    Game.main()


def get_easy_words():
    easy_words = []
    file = open("EasyWords.txt", "a+")
    file.close()
    with open("EasyWords.txt") as word_file:
        for word in word_file:
            easy_words.append(word[:-1])
    return easy_words


def get_medium_words():
    medium_words = []
    file = open("MediumWords.txt", "a+")
    file.close()
    with open("MediumWords.txt") as word_file:
        for word in word_file:
            medium_words.append(word[:-1])
    return medium_words


def get_hard_words():
    hard_words = []
    file = open("HardWords.txt", "a+")
    file.close()
    with open("HardWords.txt") as word_file:
        for word in word_file:
            hard_words.append(word[:-1])
    return hard_words 


def get_custom_words():
    custom_words = []
    file = open("CustomWords.txt", "a+")
    file.close()
    with open("CustomWords.txt") as word_file:
        for word in word_file:
            custom_words.append(word[:-1])
    return custom_words 

# Parses for letterless input
def check_letters(words):
    letters = ""
    for i in range(len(words)):
        if words[i].isalpha():
            letters += words[i]
    return letters


def add_words(c_words):
    file = open("CustomWords.txt", "a+")
    while True:
        clear()
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
            elif choice == 2:
                add_words(custom_words)
                break
            elif choice == 3:
                open_twitter()
                break
            elif choice == 4:
                exit(0)
            elif choice == 5:
                break
            else:
                print("That value is not a valid option...")
                sleep(1.5)


def init():
    main_menu()

easy_words = get_easy_words()
medium_words = get_medium_words()
hard_words = get_hard_words()
custom_words = get_custom_words()
states = States.stages
init()
