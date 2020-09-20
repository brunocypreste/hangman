#em breve tera um banco de dados

import random 
import os

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

def take_word():
    with open("hangman\palavras.txt", "rt") as f:
        a = f.readlines()
    return a[random.randint(0, len(a))].strip()

class Game:
    def __init__(self, word):
        self.word = word
        self.right_word = []
        self.wrong_word = []
    
    def win(self):


if __name__ == "__main__":
    word = take_word()
    game = Game(word)
