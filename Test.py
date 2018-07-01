# This program was made by Nicholas Lueth
# Created on 7/1/2018
# "Console Hangman"
import random


def clear():
    print("\n" * 20)


def get_word(the_word):
    short_word = ""
    for i in range(len(the_word)):
        if the_word[i].isalpha():
            short_word += the_word[i]
    return short_word


def add_words():
    file = open("custom_words.txt", "a")
    adding = True
    while adding:
        new_word = input("New word(s): ").lower()
        if len(new_word) < 1 or len(get_word(new_word)) < 1:
            add_words()
            break
        file.write(new_word + "\n")
        crazy = True
        while crazy:
            choice = input("Would you like to add more words?(y/n): ").lower()
            if choice == "y":
                crazy = False
            elif choice == "n":
                crazy = False
                adding = False
    file = open("custom_words.txt", "r")
    for x in file:
        level_4_words.append(x[:-1])


def play_again():
    global playing
    global num_wrong
    dumb = True
    while dumb:
        playing = input("Would you like to play again?(y/n): ").lower()
        if playing == "y":
            guessed.clear()
            num_wrong = 0
            clear()
            game()
        elif playing == "n":
            exit(0)


def test_win():
    for i in range(len(get_word(word))):
        if not guessed.__contains__(get_word(word)[i]):
            return False
    return True


def check_word():
    for i in range(len(word)):
        if word[i] == " ":
            print(" ", end=" ")
        elif not word[i].isalpha():
            print(word[i], end=" ")
        elif not guessed.__contains__(word[i]):
            print("_", end=" ")
        else:
            print(word[i], end=" ")
    print()
    print("Guessed letters: ", end="")
    for i in range(len(guessed)):
        print(guessed[i], end=" ")
    print("\n" * 2)


def turn():
    global num_wrong
    global playing
    print(stages[num_wrong])
    check_word()
    idiot = True
    while idiot:
        guess = input("Guess a letter: ")
        if guess.isalpha():
            idiot = False
            guess = guess[0].lower()
    clear()
    if get_word(word).__contains__(guess) and not guessed.__contains__(guess):
        print(guess.upper(), "is in the word(s)!")
    elif not get_word(word).__contains__(guess) and not guessed.__contains__(guess):
        print(guess.upper(), "is NOT in the word(s)!")
        num_wrong += 1
    else:
        print("You already said that letter!")
    if not guessed.__contains__(guess):
        guessed.append(guess)
    if num_wrong == 8:
        print("\nYOU LOSE!\nThe word(s) was:", word)
        print(stages[num_wrong])
        play_again()
    elif test_win():
        print("\nYOU WIN!\nThe word(s) was:", word)
        print(stages[num_wrong])
        play_again()


def start():
    global word
    dumb = True
    while dumb:
        difficulty = input('''What difficulty would you like?
1. Easy
2. Medium
3. Hard
4. Custom
''')
        if not difficulty == "" and not difficulty.isalpha():
            dumb = False
    difficulty = int(difficulty[0])
    if difficulty == 1:
        word = level_1_words[random.randint(0, len(level_1_words) - 1)]
    elif difficulty == 2:
        word = level_2_words[random.randint(0, len(level_2_words) - 1)]
    elif difficulty == 3:
        word = level_3_words[random.randint(0, len(level_3_words) - 1)]
    elif difficulty == 4:
        if len(level_4_words) == 0:
            weird = True
            while weird:
                choice = input("You have no custom words. Would you like to add some?(y/n)").lower()
                if choice == "y":
                    weird = False
                    add_words()
                elif choice == "n":
                    quit(0)
        reeree = True
        while reeree:
            choice = input("Would you like to add more custom words?(y/n): ").lower()
            if choice == "y":
                reeree = False
                add_words()
            elif choice == "n":
                reeree = False
        word = level_4_words[random.randint(0, len(level_4_words) - 1)]
    else:
        start()
    clear()
    turn()


def game():
    start()
    while playing.lower() == "y":
        turn()


level_1_words = ["cat", "dog", "tick", "taco", "grape", "stick", "tree", "fork", "land", "work", "tan"]
level_2_words = ["island", "parrot", "pineapple", "orange", "pinecone", "applesauce", "landmine", "computer"
                 "goodbye"]
level_3_words = ["rhythm", "hyperactivity", "coleopterology", "ethnomethodology", "ktenology", "zoosemiotics"]
level_4_words = []
guessed = []
stages = ['''   
                ________
                |      |
                |      
                |    
                |      
                |     
                |
                |
              ———————''', '''
                ________
                |      |
                |      @
                |     
                |     
                |     
                |
                |
              ———————''', '''
                ________
                |      |
                |      @
                |      |
                |      |
                |     
                |
                |
              ———————''', '''
                ________
                |      |
                |      @
                |     \|
                |      |
                |     
                |
                |
              ———————''', '''
                ________
                |      |
                |      @
                |     \|/
                |      |
                |      
                |
                |
              ———————''', '''
                ________
                |      |
                |      @
                |     \|/
                |      |
                |     /  
                |
                |
              ———————''', '''
                ________
                |      |
                |      @
                |     \|/
                |      |
                |    _/  
                |
                |
              ———————''', '''
                ________
                |      |
                |      @
                |     \|/
                |      |
                |    _/ \ 
                |
                |
              ———————''', '''
                ________
                |      |
                |      @
                |     \|/
                |      |
                |    _/ \_ 
                |
                |
              ———————''']
level = 2
word = ""
num_wrong = 0
file = open("custom_words.txt", "a+")
file = open("custom_words.txt", "r")
for line in file:
    level_4_words.append(line[:-1])
print("WELCOME TO HANGMAN!")
stupid = True
while stupid:
    playing = input("Would you like to play hangman?(y/n): ").lower()
    if playing == "y":
        stupid = False
        game()
    elif playing == "n":
        exit(0)
