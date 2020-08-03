#!/bin/python3
# Hangman States
# Created by: Nicholas Lueth
# Last Edited: 8/3/2020

# Different stages of the hanging man
stages = stages = ['''   
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
