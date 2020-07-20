#!/bin/python3
# Game mechanisms file
# Created by: Nicholas Lueth
# Last edited: 7/20/2020

import random
import States
from os import system, name
from time import sleep


def turn(word, tries, guessed_letters):
    clear()
    print(States.stages[tries])
    check_word(word, guessed_letters)
    guess = input("Guess a letter: ")
    if guess.isalpha():
        guess = guess[0].lower()
    clear()
    if guess in word and not guess in guessed_letters:
        print(guess.upper(), "is in the word(s)!")
        guessed_letters.append(guess)
    elif not guess in word  and not guess in guessed_letters:
        print(guess.upper(), "is NOT in the word(s)!")
        tries += 1
    else:
        print("You already said that letter!")


def check_word(word, guessed_letters):
    for letter in range(len(word)):
        if word[letter] == " ":
            print(" ", end=" ")
        elif not word[letter].isalpha():
            print(word[letter], end=" ")
        elif not word[letter] in guessed_letters:
            print("_", end=" ")
        else:
            print(word[letter], end=" ")
    print()
    print("Guessed letters: ", end="")
    for i in range(len(guessed_letters)):
        print(guessed_letters[i], end=" ")
    print("\n" * 2)


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


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


def get_word(level):
    word = ""
    if level == 1:
        words = get_easy_words()
        word = words[random.randint(0, len(words)-1)]
        return word
    elif level == 2:
        words = get_medium_words()
        word = words[random.randint(0, len(words)-1)]
        return word
    elif level == 3:
        words = get_hard_words()
        word = words[random.randint(0, len(words)-1)]
        return word
    elif level == 4:
        words = get_custom_words()
        word = words[random.randint(0, len(words)-1)]
        return word


def level_select():
    while True:
        clear()
        print("Select a difficulty:\n1. Easy\n2. Medium\n3. Hard\n4. Custom\n5. Main menu")
        try:
            level = int(input("Choice: "))
        except ValueError:
            clear()
            print("INVALID OPTION!\nPlease type a number.")
            input("PRESS ENTER TO CONTINUE...")
        else:
            if level > 0 and level < 6:
                return level
            else:
                print("That value is not a valid option...")
                sleep(1.5)


# TODO Test to see if win or lose
def test_win():
    pass


# TODO Displaying the word as the game goes on
def word_state(tries):
    pass
#    return States.stages[tries]


def main():
    while True:
        tries = 0
        guessed_letters = []
        level = level_select()
        if level == 5:
            break
        word = get_word(level)
        while True:
            turn(word, tries, guessed_letters)
            if test_win():
                break
