#em breve tera um banco de dados

import random 
import os
import sys

def take_word():
    a = list(open("palavras.txt", "r").split(\n))
    return random.choice(a)
class Game():
    def __init__(self, word):
        self.word = word
        self.right_word = []
        self.wrong_word = []
    
    def gallows():
        gallows = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


if __name__ == "__main__":
    word = take_word()
    game = Game(word)
