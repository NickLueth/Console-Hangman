#!/bin/python3
# Game mechanisms file
# Created by: Nicholas Lueth
# Last edited: 3/5/2020

import random
import Hangman
from os import system, name
from time import sleep

def turn():
    pass


def get_word(level):
    word = ""
    if level == 1:
        words = Hangman.get_easy_words()
        word = words[random.randint(0, len(words)-1)]
        print(word)
    elif level == 2:
        words = Hangman.get_medium_words()
        word = words[random.randint(0, len(words)-1)]
        print(word)
    elif level == 3:
        words = Hangman.get_hard_words()
        word = words[random.randint(0, len(words)-1)]
        print(word)
    elif level == 4:
        words = Hangman.get_custom_words()
        word = words[random.randint(0, len(words)-1)]
        print(word)




def level_select():
    while True:
        Hangman.clear()
        print("Select a difficulty:\n1. Easy\n2. Medium\n3. Hard\n4. Custom\n5. Main menu")
        try:
            level = int(input("Choice: "))
        except ValueError:
            Hangman.clear()
            print("INVALID OPTION!\nPlease type a number.")
            input("PRESS ENTER TO CONTINUE...")
        else:
            if level > 0 and level < 6:
                return level
            else:
                print("That value is not a valid option...")
                sleep(1.5)

def test_win():
    pass


def word_state():
    pass


def main():
    while True:
        tries = 0
        guessed_letters = []
        level = level_select()
        if level == 5:
            break
        word = get_word(level)
        while True:
            turn(word, tries)
            if test_win():
                break
